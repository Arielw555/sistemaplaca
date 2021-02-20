
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView,DeleteView
from django.db.models import Q
from .forms import PlacasForm1
from .models import Placas
from django.urls import reverse_lazy


def Home (request):
    return render (request, 'libro/index.html')


def crearAutor (request):
    if request.method == 'POST':
        autor_form = PlacasForm1(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect ('libro:listar_autor')
    
    else:
        autor_form = PlacasForm1()
    return render (request,'libro/crear_autor.html', {'autor_form':autor_form})

  
    #chasis
    #noPlaca
    #compania
    #Estado

def listarAutor (request):
    busqueda = request.POST.get("buscar")
    placas=Placas.objects.all()
    
    if busqueda:
        placas = Placas.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(chasis__icontains = busqueda) |
            Q(noPlaca__icontains = busqueda) |
            Q(compania__icontains = busqueda) |
            Q(Estado__icontains = busqueda) 

        ).distinct()

    return render (request,  "libro/listar_autor.html", {"placas": placas})


def documentos (request):
    busqueda = request.POST.get("buscar")
    placas=Placas.objects.all()
    
    if busqueda:
        placas = Placas.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(chasis__icontains = busqueda) |
            Q(noPlaca__icontains = busqueda) |
            Q(compania__icontains = busqueda) |
            Q(Estado__icontains = busqueda) 

        ).distinct()

    return render (request,  "libro/documentos.html", {"placas": placas})


class editarAutor( UpdateView):
    model = Placas
    form_class = PlacasForm1  
    template_name = 'libro/libro.html'
    success_url = reverse_lazy('libro:listar_autor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Autor'] = Placas.objects.filter(id = True)
        return context

class eliminarAutor( DeleteView):
    model = Placas
    form_class = PlacasForm1  
    template_name = 'libro/eliminar_autor.html'
    success_url = reverse_lazy('libro:listar_autor')




