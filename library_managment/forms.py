from django.forms import ModelForm

from clients.widget import DatePicketInput
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {'return_date': DatePicketInput}