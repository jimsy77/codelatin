from django.contrib import admin
from app.models import Alumnos, Cursos, Docentes

class alumno_admin(admin.ModelAdmin):
    list_display = ('nombre','pais','correo')
    search_fields = ('nombre','pais',)

class curso_admin(admin.ModelAdmin):
    list_display = ('nombre','modalidad',)
    search_fields = ('nombre','modalidad')

class docente_admin(admin.ModelAdmin):
    list_display = ('nombre','pais','correo')
    search_fields = ('nombre','pais')

admin.site.register(Alumnos, alumno_admin)
admin.site.register(Cursos, curso_admin)
admin.site.register(Docentes, docente_admin)


# Register your models here.
