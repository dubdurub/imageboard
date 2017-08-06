from django.db import models
from django.utils import timezone
# Create your models here.
class board(models.Model):
	ID = models.AutoField(primary_key=True)
	bumplimit= models.IntegerField()
	title = models.CharField(max_length=5)
	name = models.CharField(max_length=15)
	def __str__(self):
		return self.title
class thread(models.Model):
	ID = models.AutoField(primary_key=True)
	board = models.ForeignKey('board',
		on_delete=models.CASCADE)
	def __str__(self):
		return str(self.ID)
class Post(models.Model):
	ID = models.AutoField(primary_key=True)
	thread= models.ForeignKey('thread',
		on_delete=models.CASCADE,)
	text = models.TextField()
	published_date = models.DateTimeField(
		blank=True, null=True)
	img = models.FileField(upload_to='documents/',  blank=True)
	def __str__(self):
		return str(self.ID)
	def publish(self):
		self.published_date = timezone.now()
		self.save()