from django.shortcuts import render, redirect
from .models import Prep
from . import forms
from django.shortcuts import get_object_or_404


def home(request):
    prep = Prep.objects.all()
    return render(request, 'prep/home.html', {'prep': prep})

def create(request):
    form = forms.CreatePrep()  # Instantiate the form outside of the conditional block
    if request.method == 'POST':
        form = forms.CreatePrep(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prep:home')

        # No need for else block here, as the form object will be passed to the template in any case
    return render(request, 'prep/create.html', {'form': form})

def delete(request, name):
    prep = get_object_or_404(Prep, name=name)
    if request.method == 'POST':
        prep.delete()
        return redirect('prep:home')  # Redirect after successful deletion