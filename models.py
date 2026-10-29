from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
