from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.id} {self.model} {self.year}"
