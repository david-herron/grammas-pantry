from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.features, name='features')
    # url(r'^(?P<recipe_id>[0-9]+)/$', views.recipe_detail, name='recipe_detail'),
    # url(r'^recipes/$', views.recipes, name='recipes'),
    # url(r'^about/$', views.about, name='about')
    ]