from django.forms import ModelForm

from .models import Client
from .widget import DatePicketInput


class ClientCreationForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {'date_of_birth': DatePicketInput}
