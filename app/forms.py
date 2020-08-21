from django.forms import ModelForm
from . import models

class NeedForm(ModelForm):
    class Meta:
        model = models.need
        exclude = ['inNeed']
