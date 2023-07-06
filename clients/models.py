from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    name_local = models.CharField(
        max_length=50,
        verbose_name='Local'
    )
    direction = models.TextField(
        verbose_name='Dirección'
    )
    photo = models.ImageField(
        verbose_name='Foto',
        null=True, blank=True
    )
    google_map = models.URLField(
        verbose_name='Direccion de google map',
        null=True,
        blank=True
    )
    local_phone = models.CharField(
        max_length=11, verbose_name='Número de teléfono'
    )
    debit = models.FloatField(
        verbose_name='Deuda', default=0
    )

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name_local

    def updateDebit(self, deliverysClient):
        debit = 0
        for dc in deliverysClient:
            debit += dc.type_delivery_amount
        self.debit = debit
        self.save()
        return None


class Payment(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name='Cliente')
    amount = models.FloatField(
        verbose_name='Monto'
    )
    date = models.DateField(
        auto_now_add=True, verbose_name="Fecha"
    )
    time = models.TimeField(
        auto_now_add=True,
        verbose_name="Hora"
    )
    centralist = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True,
        verbose_name='Centralista'
    )

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return super(Payment, self).__str__()


class Addressee(models.Model):
    local = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        verbose_name='Cliente'
    )
    data_addressee = models.CharField(
        max_length=50,
        verbose_name='Datos del consumidor'
    )
    destiny = models.TextField(
        verbose_name='Dirección'
    )
    photo = models.ImageField(
        verbose_name='Foto',
        null=True,
        blank=True)
    google_map = models.URLField(
        verbose_name='Direccion de google map',
        null=True, blank=True
    )

    class Meta:
        verbose_name = "Addressee"
        verbose_name_plural = "Addressees"

    def __str__(self):
        return self.data_addressee
