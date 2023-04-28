from django.shortcuts import render, redirect
from .forms import MainForm
import time
# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
      form = MainForm(request.POST)
      if form.is_valid():
         form.save()
      else:
         error = "Форма заполнена неверно"


    form = MainForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'mainpage/index.html', context)