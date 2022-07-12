from django import forms
from .models import ShortURL, LongURL

class DBCharField(forms.CharField):

    def validate(self, value: str):
        if len(ShortURL.objects.filter(short_url=value)) != 0:
            raise forms.ValidationError("Alias is already taken.")
        
        if value == "sitemap.xml":
            raise forms.ValidationError("Alias is already taken.")

        super().validate(value)

class URLForm(forms.Form):
    long_url = forms.URLField(label="Long URL", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "https://www.some-long-url.com"}))
    short_url = DBCharField(label="Alias", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "short-url"}))

    def add_url_pair(self):
        short_url = ShortURL(short_url=self.cleaned_data['short_url'])
        long_url = LongURL(short_url=short_url, long_url=self.cleaned_data['long_url'])

        short_url.save()
        long_url.save()