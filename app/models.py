from django.db import models

# Create your models here.

class Csapat(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Meccs(models.Model):
	hely = models.CharField(max_length=30)
	date = models.DateTimeField()
	def __unicode__(self):
		return self.hely
	
class Eredmeny(models.Model):
	meccs = models.ForeignKey(Meccs)
	csapat = models.ForeignKey(Csapat)
	pont = models.IntegerField()
	def __unicode__(self):
		return self.meccs.hely+" "+self.csapat.name+" "+str(self.pont)
