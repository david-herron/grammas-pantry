from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Recipe, Feature

# Create your views here.

def features(request):
    latest_feature = Feature.objects.order_by('-id')[0]
    second_feature = Feature.objects.order_by('-id')[1]
    third_feature = Feature.objects.order_by('-id')[2]
    fourth_feature = Feature.objects.order_by('-id')[3]
    fifth_feature = Feature.objects.order_by('-id')[4]
    past_features = Feature.objects.all().order_by('-pub_date')
    context = {'latest_feature': latest_feature,
               'past_features': past_features,
               'second_feature': second_feature,
               'third_feature': third_feature,
               'fourth_feature': fourth_feature,
               'fifth_feature': fifth_feature}
    return render(request, 'gp/features.html', context)

def feature_detail(request, pk):
    selected_feature = get_object_or_404(Feature, pk=pk)
    latest_feature = Feature.objects.order_by('-id')[0]
    past_features = Feature.objects.order_by('-pub_date')[5:10]
    third_feature = Feature.objects.exclude(id=selected_feature.id).exclude(id=latest_feature.id).order_by('-id')[0:1]
    fourth_feature = Feature.objects.exclude(id=selected_feature.id).exclude(id=latest_feature.id).order_by('-id')[1:2]
    fifth_feature = Feature.objects.exclude(id=selected_feature.id).exclude(id=latest_feature.id).order_by('-id')[2:3]    
    context = {'selected_feature': selected_feature,
               'latest_feature': latest_feature,
               'past_features': past_features,
               'third_feature': third_feature,
               'fourth_feature': fourth_feature,
               'fifth_feature': fifth_feature}
    return render(request, 'gp/feature_detail.html', context)

def about(request):
    return render(request, 'gp/about.html')

def recipes(request):
    all_recipes = Recipe.objects.all().order_by('-pub_date')
    most_recent_recipe = Recipe.objects.order_by('-id')[0]
    context = {'all_recipes': all_recipes,
               'most_recent_recipe': most_recent_recipe}
    return render(request, 'gp/recipes.html', context)

def recipe_detail(request, recipe_id):
    selected_recipe = get_object_or_404(Recipe, pk=recipe_id)
    all_recipes = Recipe.objects.all().order_by('-pub_date')
    return render(request, 'gp/recipe_detail.html', {'selected_recipe': selected_recipe, 'all_recipes': all_recipes})