from django.db import models

class Alumnos(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )

    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    curso = models.CharField(max_length=100)
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombre
    
class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=100)
    duración = models.CharField(max_length=50)
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre
    
class Docentes(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
