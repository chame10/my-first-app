from django.db import models

# Create your models here.

class Equipo(models.Model):
	IdEquipo = models.PositiveSmallIntegerField()
	Nombre = models.CharField(max_length=150)
	Logo = models.CharField(max_length=300)
	Descripcion = models.CharField(max_length=150)
	Patrocinador = models.CharField(max_length=150)
	Dueno = models.CharField(max_length=150)
	Facebook = models.CharField(max_length=300)
	Foto = models.CharField(max_length=300)

	def __str__(self):
		return self.Nombre

class Entrenador(models.Model):
	idEntrenador = models.PositiveSmallIntegerField()
	Nombre = models.CharField(max_length=150)
	Foto = models.CharField(max_length=300)
	Edad = models.PositiveSmallIntegerField()
	Telefono = models.CharField(max_length=10)
	Equipo = models.ForeignKey(Equipo,null=False,blank=False,on_delete=models.CASCADE)

	def __str__(self):
		return (self.Nombre)

class Jugador(models.Model):
	idJugador = models.PositiveSmallIntegerField()
	Nombre = models.CharField(max_length=150)
	Foto = models.CharField(max_length=300)
	Edad = models.PositiveSmallIntegerField()
	Telefono = models.CharField(max_length=10)
	Facebook = models.CharField(max_length=300)
	NumeroJugador = models.PositiveSmallIntegerField()
	Equipo = models.ForeignKey(Equipo,null=False,blank=False,on_delete=models.CASCADE)

	def __str__(self):
		return (self.Nombre)
