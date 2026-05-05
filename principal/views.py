from django.shortcuts import render, redirect
from .models import Registro

def lista_registros(request):
    if request.method == 'POST':
        # Capturamos los datos del formulario
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        fecha = request.POST.get('fecha')
        
        # Guardamos en SQL Server
        Registro.objects.create(
            descripcion=descripcion,
            monto=monto,
            fecha=fecha
        )
        return redirect('lista_registros')

    # Obtenemos todos los registros para mostrarlos
    registros = Registro.objects.all().order_by('-fecha')
    return render(request, 'principal/index.html', {'registros': registros})