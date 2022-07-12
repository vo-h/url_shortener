from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):

    changefreq = 'monthly'

    def items(self):
        return ["main"]

    def location(self, item):
        return reverse(item)