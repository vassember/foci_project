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
	csapat1.pont = models.IntegerField()
	csapat2.pont = models.IntegerField()
	date = models.DateTimeField()
	eredmeny = models.CharField(max_length=10)
	#name = models.CharField(default=csapat1.name+" Vs "+csapat2.name,max_length=150)
	def __unicode__(self):
		return self.csapat1.name+" Vs "+self.csapat2.name
