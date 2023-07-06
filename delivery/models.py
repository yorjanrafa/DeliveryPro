from sys import version
from django.db import models

from django.contrib.auth.models import User

from clients.models import Client
from workers.models import Worker
from .choices import service_type, service_type_amount, service_type2
from generate import password

# Create your models here.


class Delivery(models.Model):
    origin = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name="Origen"
    )
    addressee_data = models.CharField(
        max_length=50, verbose_name="Datos del consumidor"
    )
    destiny = models.TextField(
        verbose_name="Dirección de destino"
    )
    type_delivery = models.CharField(
        choices=service_type(), max_length=30, verbose_name="Tipo de delivery"
    )
    type_delivery_amount = models.FloatField(
        max_length=3,
        verbose_name="Tipo de delivery"
    )
    preferred_price = models.FloatField(
        max_length=3,
        verbose_name="Precio preferencial",
        blank=True,
        null=True
    )
    type_service = models.CharField(
        choices=service_type2(),
        max_length=12,
        verbose_name="Tipo de servicio",
        default='Delivery'
    )
    date = models.DateField(
        verbose_name="Fecha"
    )
    time = models.TimeField(
        auto_now_add=True, verbose_name="Hora"
    )
    status_delivery = models.BooleanField(
        verbose_name="¿Ha sido pagado el servicio?"
    )
    recieved_money = models.FloatField(
        verbose_name="Dinero recibido", default=0
    )
    status_recieved_money = models.BooleanField(
        verbose_name="¿Ha sido entregado al cliente el dinero recibido?"
    )
    # CASCADE, DO_NOTHING, PROTECT, RESTRICT, SET, SET_DEFAULT, SET_NULL,
    distributing = models.ForeignKey(
        Worker, on_delete=models.SET_NULL, null=True, verbose_name='Repartidor'
    )
    centralist = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name='Centralista'
    )
    serial = models.CharField(
        max_length=70,
        unique=True,
    )

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliverys"

    def __str__(self):
        return f'Envio {self.type_service} de {self.origin} hacia {self.destiny}'

    def setDeliveryTypeMount(self, delivery_type):
        self.type_delivery_amount = service_type_amount(delivery_type)
        return None
