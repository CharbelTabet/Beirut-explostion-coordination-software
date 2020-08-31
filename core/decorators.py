from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from app import models

def user_owns_position(function):
    def wrap(request, *args, **kwargs):
        position = models.position.objects.get(pk=kwargs['pk'])
        if position.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def user_owns_damage(function):
    def wrap(request, *args, **kwargs):
        damage = models.position.objects.get(pk=kwargs['pk'])
        if damage.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
