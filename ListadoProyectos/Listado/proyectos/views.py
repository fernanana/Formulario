from django.shortcuts import render, redirect
from proyectos.forms import PrincipalProyecto
from proyectos.models import Proyecto

def index(request):
    return render(request, 'index.html')


def listadoProyecto(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'listado_proyectos.html', data)
    
def agregarProyecto(request):
    form = PrincipalProyecto()
    if request.method == 'POST' :
        form = PrincipalProyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)


def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect('/listado_proyectos')


def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = PrincipalProyecto(instance=proyecto)
    if request.method == 'POST' :
        form = PrincipalProyecto(request.POST, instance=proyecto)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)

