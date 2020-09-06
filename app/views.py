from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from core.decorators import user_owns_position, user_owns_damage, user_owns_need
from django import forms
from . import models
from . import forms
from . import queries

# Errors
def handler404(request, exception, template_name="errors/404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

# Map views
class Map(TemplateView):
    template_name = 'maps/mainMap.html'

class userMap(View):
    template_name='maps/userMap.html'

    def get(self, request, username):
        return render(request, self.template_name, {'username': username})

class MapsList(TemplateView):
    template_name ='maps/mapsList.html' 

    def get(self, request):
        stats = queries.queries()
        usersStats = {}
        users = User.objects.all()
        for user in users:
            usersStats[user.username] = stats.userStats(user.id)
        context = {}
        context["usersStats"] = usersStats
        context["users"] = users
        return render(request, self.template_name, context)

# Dashboard views
class mainDashboard(View):
    template_name = 'dashboards/dashboard.html'

    def get(self, request):
        stats = queries.queries()
        context = stats.allData()
        return render(request, self.template_name, context)

class userDashboard(View):
    template_name = 'dashboards/dashboard.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        stats = queries.queries()
        context = stats.userData(user.id)
        context["title"] = "{}'s dashboard".format(user.username)
        return render(request, self.template_name, context)

class DashboardsList(View):
    template_name = 'dashboards/dashboardsList.html'

    def get(self, request):
        stats = queries.queries()
        usersStats = {}
        users = User.objects.all()
        for user in users:
            usersStats[user.username] = stats.userStats(user.id)
        context = {}
        context["usersStats"] = usersStats
        context["users"] = users
        return render(request, self.template_name, context)

# Create views
@method_decorator(login_required(login_url="/login"), name="dispatch")
class CreatePosition(CreateView):
    model = models.position
    fields = '__all__'
    success_url ='/'
    template_name = 'forms/createPosition.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)

@method_decorator(login_required(login_url="/login"), name="dispatch")
class CreateDamage(CreateView):
    model = models.damage
    fields = '__all__'
    success_url ='/'
    template_name = 'forms/createDamage.html'

# Read views
@method_decorator(login_required(login_url="/login"), name="post")
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
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(self.request.path_info)

@method_decorator(login_required(login_url="/login"), name="post")
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
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(self.request.path_info)

# Update views
@method_decorator(user_owns_position, name="dispatch")
class UpdatePosition(UpdateView):
    model = models.position
    fields = '__all__'
    template_name = 'forms/updatePosition.html'

    def get_success_url(self):
        return '/position/{}'.format(self.object.pk)

@method_decorator(user_owns_damage, name="dispatch")
class UpdateDamage(UpdateView):
    model = models.damage
    fields = '__all__'
    template_name = 'forms/updateDamage.html'

    def get_success_url(self):
        return '/damages/{}'.format(self.object.pk)

@method_decorator(user_owns_need, name="dispatch")
class UpdateNeedStatus(UpdateView):
    model = models.need
    fields = ['status']
    template_name = 'forms/updateneedstatus.html'

    def get_success_url(self):
        return '/position/{}'.format(self.object.inNeed)

# Delete view
@method_decorator(user_owns_position, name="dispatch")
class DeletePosition(DeleteView):
    model = models.position
    fields = '__all__'
    success_url = '/'
    template_name = 'forms/deletePosition.html'

@method_decorator(user_owns_damage, name="dispatch")
class DeleteDamage(DeleteView):
    model = models.damage
    fields = '__all__'
    success_url = '/'
    template_name = 'forms/deleteDamage.html'

@method_decorator(user_owns_need, name="dispatch")
class DeleteNeed(DeleteView):
    model = models.need
    fields = '__all__'
    success_url = '/'
    template_name = 'forms/deleteNeed.html'

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
        for element in objects:
            userId = element['user_id']
            user = User.objects.get(id=userId)
            element['user'] = user.username
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

class userPositions(View):
    data = queries.queries()
    def objects(self, request):
        user = User.objects.get(username = self.kwargs['username'])
        dic = self.data.userPositions(user.id)
        positions = dic['positions']
        return list(positions)

    def get(self, request, username):
        return JsonResponse(self.objects(request), safe=False)

class userDamages(View):
    data = queries.queries()
    def objects(self, request):
        user = User.objects.get(username = self.kwargs['username'])
        dic = self.data.userDamages(user.id)
        damages = dic['damages']
        return list(damages)  

    def get(self, request, username):
        return JsonResponse(self.objects(request), safe=False)

class csvTest(View):
    def get(self, request):
        return HttpResponse('')

# User views
class userView(View):
    template_name = 'usersviews/userView.html'
    def get(self, request, username):
        stats = queries.queries()
        user = get_object_or_404(User.objects.filter(username=username))
        userStats = stats.userStats(user.id)
        return render(request, 'userviews/userView.html', {'username': self.kwargs['username'], 'userStats': userStats})
