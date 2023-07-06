from clients.models import Client
from delivery.models import Delivery

clients = Client.objects.all()

def updateAll():
	for c in clients:
		deliverys = Delivery.objects.filter(origin=c, status_delivery=False)
		if deliverys:
			c.updateDebit(deliverys)
			print('OK')

