from django.shortcuts import render
from .forms import EmpleadoForm

def manage_empleados(request):
	formset = EmpleadoForm()
	return render(request, 'page.html', {'formset': formset})