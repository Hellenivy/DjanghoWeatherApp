from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def _str_(self): #shows actual city name on  dashboard
        return self.name

    class Meta: #shows plural of city as cities instead of citys
        verbose_name_plural = 'cities'