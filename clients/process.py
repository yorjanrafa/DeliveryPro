from django.shortcuts import redirect
from django.contrib import messages


def paid(client, deliverys, instance, request):
    amount = instance.amount
    if amount > client.debit:
        message = messages.error(request, 'El monto de pago no puede ser superior a la deuda del cliente.')
        redirect_a = redirect('/clients/list')
        return {'message': message, 'redirect_a': redirect_a}

    if client.debit == amount:
        for d in deliverys:
            d.status_delivery = True
            d.type_delivery_amount = 0
            d.save()

        client.updateDebit(deliverys)
        instance.save()
        message = messages.success(request, 'Pago realizado correctamente')
        redirect_a = redirect('/clients/list')
        return {'message': message, 'redirect_a': redirect_a}

    for d in deliverys:
        if amount >= d.type_delivery_amount:
            amount -= d.type_delivery_amount
            d.type_delivery_amount = 0
            d.status_delivery = True
            d.save()
        elif amount < d.type_delivery_amount and amount > 0:
            d.type_delivery_amount -= amount
            amount = 0
            d.save()

    client.updateDebit(deliverys)
    instance.save()
    message = messages.success(request, 'Pago realizado correctamente')
    redirect_a = redirect('/clients/list')
    return {'message': message, 'redirect_a': redirect_a}



