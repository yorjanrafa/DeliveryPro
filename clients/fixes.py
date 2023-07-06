from django.shortcuts import get_object_or_404
from delivery.models import Delivery
from clients.models import Client


def checkDuplicity():
    d = Delivery.objects.order_by('-id')[:2]
    if (d[0].addressee_data == d[1].addressee_data) and (d[0].destiny == d[1].destiny) and (d[0].distributing == d[1].distributing):
        d[0].delete()
        client_id = d[1].origin.id
        client = get_object_or_404(Client, id=client_id)
        client.updateDebit(Delivery.objects.filter(
            origin=client, status_delivery=False))


    d = Delivery.objects.order_by('-id')[:2]
    if (d[0].addressee_data == d[1].addressee_data) and (d[0].destiny == d[1].destiny) and (d[0].distributing == d[1].distributing):
        d[0].delete()
        client_id = d[1].origin.id
        client = get_object_or_404(Client, id=client_id)
        client.updateDebit(Delivery.objects.filter(
            origin=client, status_delivery=False))
    return None
