
import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Singer(models.Model):
    """docstring for Singer"""
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    region = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Concert(models.Model):
    """docstring for Concert"""
    concert_name = models.CharField(max_length=200)
    buy_ticket_date = models.DateTimeField('buy ticket time')
    address = models.CharField(max_length=200)
    buy_ticket_address = models.URLField(max_length=200,blank=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    launch_date = models.DateTimeField('launch time')
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.concert_name
    def was_baught_recently(self):
        now = timezone.now()
        return now <= self.buy_ticket_date <= now + datetime.timedelta(days=10)


class Ticket_price (models.Model):
    """docstring for Ticket_price """
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

class FavoriteConcert(models.Model):
	"""docstring for FavoriteConcert"""
	concert_name = models.ForeignKey(Concert, on_delete=models.CASCADE)




class Photo(models.Model):
	title = models.CharField(max_length=200)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
	concert_name = models.ForeignKey(Concert, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp"]
# Create your models here.