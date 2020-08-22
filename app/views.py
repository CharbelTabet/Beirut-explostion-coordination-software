from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django import forms
from . import models
from . import forms
from . import queries

# Dashboard sections
class Map(TemplateView):
    template_name = 'maps/mainMap.html'

class MapsList(TemplateView):
    template_name ='maps/mapsList.html' 

class DashboardsList(TemplateView):
    template_name = 'dashboards/dashboardsList.html'

class ChartsList(TemplateView):
    template_name = 'analytics/charts.html'

class TablesList(TemplateView):
    template_name = 'analytics/tables.html'

# Sections
class Dashboard(TemplateView):
    template_name = 'dashboards/mainDashboard.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        stats = queries.queries()
        data['cardsData'] = stats.cards
        data['tablesData'] = stats.tables
        return data

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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['needs'] = models.need.objects.filter(inNeed=self.kwargs['pk'])
        data['needForm'] = forms.NeedForm
        return data

    def post(self, request, pk):
        form = forms.NeedForm(request.POST)
        obj = form.save(commit=False)
        obj.inNeed = pk
        obj.save()
        return HttpResponseRedirect(self.request.path_info)

class DamageDetail(DetailView):
    model = models.damage
    template_name = 'detailviews/damage.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['needs'] = models.need.objects.filter(inNeed=self.kwargs['pk'])
        data['needForm'] = forms.NeedForm
        return data

    def post(self, request, pk):
        form = forms.NeedForm(request.POST)
        obj = form.save(commit=False)
        obj.inNeed = pk
        obj.save()
        return HttpResponseRedirect(self.request.path_info)


# Update views
class UpdatePosition(UpdateView):
    model = models.position
    fields = '__all__'
    template_name = 'forms/updatePosition.html'

    def get_success_url(self):
        return '/position/{}'.format(self.object.pk)

class UpdateDamage(UpdateView):
    model = models.damage
    fields = '__all__'
    template_name = 'forms/updateDamage.html'

    def get_success_url(self):
        return '/damages/{}'.format(self.object.pk)


# Delete view
class DeletePosition(DeleteView):
    model = models.position
    fields = '__all__'
    success_url = '/'
    template_name = 'forms/deletePosition.html'

class DeleteDamage(DeleteView):
    model = models.damage
    fields = '__all__'
    success_url = '/'
    template_name = 'forms/deleteDamage.html'


# Data json response
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


# Development views
class FullScreenMap(TemplateView):
    template_name = 'maps/fullscreenMap.html'
