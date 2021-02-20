from django.db import models

class Placas (models.Model):
    nombre = models.CharField(max_length=50)
    chasis = models.CharField(max_length=15)
    No_cedula = models.CharField(max_length=15)
    noPlaca = models.CharField(max_length=20, blank=True)
    compania = models.CharField(max_length=50,blank=True)
    fechaOrden = models.CharField(max_length=20, blank=True)
    endoso = models.CharField(max_length=20, blank=True)
    FechaEndoso = models.CharField(max_length=20, blank=True)
    Estado = [
         ('Pendiente de Placa', 'Pendiente de Placa'),
        ('placa y matricula', 'placa y matricula'),
        ('placa y copia M.', 'placa y copia M.'),
        ('placa entregada', 'placa entregada'),
        ('Endosando', 'Endosando'),
        ('Matricula Lista', 'Matricula Lista'),
        ('placa y M. Entregada', 'placa y M. Entregada'),

    ]
    Estado = models.CharField(
        max_length=22,
        choices=Estado,
        default=None,
    )

    fecha =  models.DateTimeField(auto_now_add=True)
    cedula = models.BooleanField(default=True)
    Comentario=models.TextField(max_length=50)
    
class Autor (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank = False, null=False)
    apellidos = models.CharField(max_length=220, blank = False, null=False)
    nacionalidad = models.CharField(max_length=100, blank = False, null=False)
    descripcion = models.TextField( blank = False, null=False)

    class meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
    
    def __str__(self) :
        return self.nombre

class Libro (models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion=models.DateField('Fecha de publicacion', blank = False, null=False)
    autor_id= models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=True,auto_now_add=False)

    class meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
    
    def __str__(self) :
        return self.titulo
