from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

#class Study(models.Model):

class WordList(models.Model):
	word= models.CharField(max_length=30)
	definition= models.CharField(max_length=200)
	word_id=models.CharField(max_length=100,primary_key=True)

	def __str__(self):
		return self.word_id


class Progress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	word_id= models.ForeignKey(WordList,on_delete=models.CASCADE)
	learned= models.BooleanField(default=False)
	correct=models.IntegerField(default=0)
	wrong=models.IntegerField(default=0)
	interval= models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str((word_id,learned,correct,wrong))
