from django.urls import path, re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap
}

urlpatterns = [
    path('', views.index, name='main'),
    re_path(r"(?P<short_url>(^| )(?!sitemap\.xml)[^ ]*)", views.get_long_url, name="get-long-url"),
    path("sitemap.xml/", sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.vites.sitemap")
]