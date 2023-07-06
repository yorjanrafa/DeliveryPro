from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=16, verbose_name="Nombre")
    last_name = models.CharField(max_length=16, verbose_name="Apellido")
    status = models.BooleanField(verbose_name="Estado")

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "workers"
  
    def __str__(self):
            return f'{self.name} {self.last_name}'
