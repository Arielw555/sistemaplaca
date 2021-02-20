from django.urls import path
from .views  import Home
from .views  import crearAutor,listarAutor,editarAutor,eliminarAutor,documentos
urlpatterns = [ 
    path('index/', Home, name='index'),
    path('crear_autor/', crearAutor, name = 'crear_autor' ),
    path('listar_autor/', listarAutor, name = 'listar_autor'),
     path('documentos/', documentos, name = 'documentos'),
    path('editar_autor/<int:pk>', editarAutor.as_view(), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>', eliminarAutor.as_view(), name = 'eliminar_autor'),
    
   
]
