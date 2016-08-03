from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Recipe, Feature

# Create your views here.

def features(request):
    # latest_feature = Feature.objects.order_by('-id')[0]
    # second_feature = Feature.objects.order_by('-id')[1]
    # third_feature = Feature.objects.order_by('-id')[2]
    # fourth_feature = Feature.objects.order_by('-id')[3]
    # fifth_feature = Feature.objects.order_by('-id')[4]
    # past_features = Feature.objects.all().order_by('-pub_date')
    # context = {'latest_feature': latest_feature,
    #            'past_features': past_features,
    #            'second_feature': second_feature,
    #            'third_feature': third_feature,
    #            'fourth_feature': fourth_feature,
    #            'fifth_feature': fifth_feature}
    return render(request, 'gp/features.html')