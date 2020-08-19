from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django import forms
from . import models

# Dashboard sections
class Map(TemplateView):
    template_name = 'maps/mainMap.html'

class MapsList(TemplateView):
    template_name ='maps/mapsList.html' 

class Dashboard(TemplateView):
    template_name = 'dashboards/mainDashboard.html'

class DashboardsList(TemplateView):
    template_name = 'dashboards/dashboardsList.html'

class ChartsList(TemplateView):
    template_name = 'analytics/charts.html'

class TablesList(TemplateView):
    template_name = 'analytics/tables.html'

# Forms
class CreatePosition(CreateView):
    model = models.position
    fields = '__all__'
    success_url ='/'
    template_name = 'forms/createPosition.html'

class CreateDamage(CreateView):
    model = models.damage
    fields = '__all__'
    success_url ='/'
    template_name = 'forms/createDamage.html'


# Detail views
class PositionDetail(DetailView):
    model = models.position
    template_name = 'detailviews/position.html'

class DamageDetail(DetailView):
    model = models.damage
    template_name = 'detailviews/damage.html'

# Data
class Locations(View):
    model = models.pin
    def objects(self, request):
        objects = self.model.objects.values()
        return list(objects)

    def get(self, request):
        return JsonResponse(self.objects(request), safe=False)

class Areas(View):
    model = models.area
    def objects(self, request):
        objects = self.model.objects.values()
        return list(objects)

    def get(self, request):
        return JsonResponse(self.objects(request), safe=False)

class Positions(View):
    model = models.position
    def objects(self, request):
        objects = self.model.objects.values()
        return list(objects)

    def get(self, request):
        return JsonResponse(self.objects(request), safe=False)

class Damages(View):
    model = models.damage
    def objects(self, request):
        objects = self.model.objects.values()
        return list(objects)

    def get(self, request):
        return JsonResponse(self.objects(request), safe=False)


# Development
class FullScreenMap(TemplateView):
    template_name = 'maps/fullscreenMap.html'
