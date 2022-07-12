from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortURL, LongURL
from .forms import URLForm
from django.template import loader


def index(request):

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            form.add_url_pair()
            template = loader.get_template("app/confirm.html")
            context = {
                "short_url": request.POST["short_url"],
                "long_url": request.POST["long_url"]
            }

            print(context)
            return HttpResponse(template.render(context, request))
    else:
        form = URLForm()

    return render(request, 'app/index.html', {'form': form})

def get_long_url(request, short_url):

    try:
        long_url = LongURL.objects.get(
            short_url=ShortURL.objects.get(short_url=short_url)
        )

        return redirect(str(long_url))

    except:

        template = loader.get_template("app/404.html")
        return HttpResponse(template.render({}, request))