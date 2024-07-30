from .models import Artista, Grupo, Artista_Grupo, Albun
from datetime import datetime

def crear_artista(nombre,apellido,cantante,instrumento):
    artista = Artista(
        nombre=nombre,
        apellido=apellido,
        cantante=cantante,
        instrumento=instrumento
    )
    artista.save()
    return artista

def crear_grupo(nombre):
    grupo = Grupo(nombre=nombre)
    grupo.save()
    return  grupo

def relacion_artista_grupo(id_artista,id_grupo,fecha_ingreso,agregado_por=None):
    artista = Artista.objects.get(id_artista=id_artista)
    grupo = Grupo.objects.get(id_grupo=id_grupo)
    artista_grupo = Artista_Grupo(
        id_artista = artista,
        id_grupo = grupo,
        fecha_ingreso = fecha_ingreso,
        agregado_por=agregado_por
    )
    artista_grupo.save()
    return artista_grupo

def agregar_album(titulo,anio,id_grupo):
    grupo = Grupo.objects.get(id_grupo=id_grupo)
    fecha_anio = datetime.strptime(anio, "%Y-%m-%d").date()
    album = Albun(
        titulo=titulo,
        anio=fecha_anio,
        id_grupo=grupo
    )
    album.save()
    return grupo

def obtiene_artista():
    artista = Artista.objects.all()
    return artista

def obtiene_grupo():
    grupo = Grupo.objects.all()
    return grupo

