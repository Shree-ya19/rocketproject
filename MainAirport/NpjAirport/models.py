from django.db import models

# Create your models here.
class Csit(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)


    class Meta:
        db_table = "csit"

    def __str__(self)-> str:
        return self.name
