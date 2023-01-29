from django.db import models

# Create your models here.

class Noticias(models.Model):
    Titulo = models.CharField(max_length=120)
    Imagen = models.ImageField(blank=True, null=True, upload_to="terceraWeb", default='botan.jpeg')
    Contenido = models.CharField(max_length=360)
    Creada = models.DateTimeField(auto_now_add=True)
    Actualizadas = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Noticia'
        verbose_name_plural='Noticias'
    
    def __str__(self):
        return self.Titulo

# class Horarios(models.Model):
#     Titulo = models.CharField(max_length=120)
#     Imagen = models.ImageField(blank=True, null=True, upload_to="terceraWeb", default='botan.jpeg')
#     Creada = models.DateTimeField(auto_now_add=True)
#     Actualizadas = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name='Horario'
#         verbose_name_plural='Horarios'
    
#     def __str__(self):
#         return self.Titulo

class Personal(models.Model):
    Titulo = models.CharField(max_length=120)
    Imagen = models.ImageField(blank=True, null=True, upload_to="terceraWeb", default='botan.jpeg')
    Creada = models.DateTimeField(auto_now_add=True)
    Actualizadas = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Personal'
        verbose_name_plural='Personal'
    
    def __str__(self):
        return self.Titulo

class Instalaciones(models.Model):
    Titulo = models.CharField(max_length=120)
    Imagen = models.ImageField(blank=True, null=True, upload_to="terceraWeb", default='botan.jpeg')
    Creada = models.DateTimeField(auto_now_add=True)
    Actualizadas = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Instalación'
        verbose_name_plural='Instalaciones'
    
    def __str__(self):
        return self.Titulo
