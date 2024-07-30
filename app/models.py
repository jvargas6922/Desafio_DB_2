from django.db import models

# Create your models here.
class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50, null=False)

    class Meta:
        managed = False
        db_table = 'artista'

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'grupo'

    def __str__(self):
        return  self.nombre

class Artista_Grupo(models.Model):
    id_artista_grupo = models.AutoField(primary_key=True)
    id_artista = models.ForeignKey(Artista, on_delete=models.CASCADE, db_column='id_artista')
    id_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, db_column='id_grupo')
    fecha_ingreso = models.DateField(null=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    agregado_por = models.DateField()

    class Meta:
        managed = False
        db_table = 'fecha_ingreso'

    def __str__(self):
        return self.id_artista_grupo

class Albun(models.Model):
    id_album = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=True)
    anio = models.DateField()
    id_grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE, db_column='id_grupo')

    class Meta:
        managed = False
        db_table = 'album'

    def __str__(self):
        return self.titulo


