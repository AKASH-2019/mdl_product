from django.db import models

class Weather(models.Model):
    weather_type = models.IntegerField(null= True)
    title = models.CharField(max_length=20)
    low_range = models.FloatField()
    high_range = models.FloatField()

class Product(models.Model):
    # mainimage = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=264)
    weather_type = models.ForeignKey(Weather, on_delete=models.CASCADE, related_name='wetherType')
    # preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]
