from django.db import models

# Create your models here.

class Csapat(models.Model):
	name = models.CharField(max_length=100)
	pont = models.IntegerField()
	def __unicode__(self):
		return self.name

class Meccs(models.Model):
	csapat1 = models.ForeignKey(Csapat)	
	csapat2 = models.ForeignKey(Csapat,related_name='csapat2')
	date = models.DateTimeField()
	eredmeny = models.CharField(max_length=10)
	
