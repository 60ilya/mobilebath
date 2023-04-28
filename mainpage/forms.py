from .models import Form
from django.forms import ModelForm, TextInput, DateInput, Select, TimeInput
import datetime

CHOICES_LOCATION = [("1", "Локация 1"), ("2", "Локация 2"), ("3", "Локация 3")]
CHOICES_RATE = [("1", "Базовый"), ("2", "Расширенный")]



class MainForm(ModelForm):
    class Meta:
        model = Form
        fields = ["fullname", "phone", "time", "date", "location", "rate"]
        widgets = {
            "phone": TextInput(attrs={
                'type': 'tel',
                'name': 'phone',
                'id': 'phone',
                'class': 'form-input',
                'pattern': '[0-9]{4}[0-9]{3}[0-9]{4}',
                'placeholder': '89001231234',
                'required': True
            }),

            "fullname": TextInput(attrs={
                'class': 'form-input',
                'name': 'phone',
                'type': 'text',
                'required': True
            }),

            "time": TimeInput(attrs={
                'type': 'time',
                'name': 'time',
                'min': '09:00',
                'max': '23:59',
                'class': 'form-input',
                'required': True
            }),

            "date": DateInput(attrs={
                'type': 'date',
                'name': 'date',
                'min': datetime.date.today(),
                'id': 'davaToday',
                'class': 'form-input',
                'required': True
            }),

            "location": Select(attrs={
                'class': 'select'
            },
            choices = CHOICES_LOCATION),

            "rate": Select(attrs={
                'class': 'select'
            },
            choices = CHOICES_RATE)

                   
        }