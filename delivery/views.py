from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db import transaction

from django.contrib.auth.decorators import login_required

from .models import Delivery
from .forms import DeliveryForm, DeliveryEditForm, DeliveryAddresseeForm
from clients.models import Client, Addressee
from generate import password

from clients.fixes import checkDuplicity

# Create your views here.


@login_required
def newDelivery(request, id):
    checkDuplicity()
    client = get_object_or_404(Client, id=id)
    deliverys = Delivery.objects.filter(origin=client, status_delivery=False)
    form = DeliveryForm(request.POST or None)
    context = {
        'form': form,
        'title_form': f'Añadiendo envio de {client}',
        'accept_and_continue': f'/delivery/new/{client.id}',
    }
    
    serial = password()
    # Aca se incrementa la deuda del cliente en base al status_delivery
    # sea True o False

    
    if request.method == 'POST':

        if form.is_valid():

            with transaction.atomic():
                with transaction.atomic():
                    check_existence = Delivery.objects.filter(serial=serial)
                    if not check_existence:
                        instance = form.save(commit=False)
                        instance.serial = serial
                        instance.origin = client
                        instance.centralist = request.user
                        if instance.type_delivery != 'Preferencial':
                            instance.setDeliveryTypeMount(instance.type_delivery)

                        if instance.type_delivery == 'Preferencial':
                            instance.type_delivery_amount = instance.preferred_price

                        if instance.status_delivery:
                            instance.type_delivery_amount = 0

                        instance.save()

                        client.updateDebit(deliverys)
                        messages.success(request, f'Añadido correctamente a "{client}"')

                        if request.POST['accept'] == 'Aceptar y continuar':
                            return redirect(f'/delivery/new/{client.id}')


            return redirect('/clients/list')

    return render(request, 'delivery/form_delivery.html', context)


@login_required
def deleteDelivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    client = get_object_or_404(Client, id=delivery.origin.id)
    deliverys = Delivery.objects.filter(origin=client, status_delivery=False)
    context = {
        'title': f'delivery {delivery}',
        'list': f'/clients/all-delivery/{delivery.origin.id}',
    }
    if request.method == 'POST':
        # worker.status = False
        delivery.delete()
        messages.success(request, 'Eliminado correctamente')
        client.updateDebit(deliverys)
        return redirect(f'/clients/all-delivery/{delivery.origin.id}')
    return render(request, 'delivery/delete-confirm.html', context)


# esta vista se trae los datos del destinatario
# existente y los mete de forma manual
@login_required
def newDeliveryAddressee(request, id):
    checkDuplicity()
    addressee = get_object_or_404(Addressee, id=id)
    client = get_object_or_404(Client, id=addressee.local.id)
    deliverys = Delivery.objects.filter(origin=client, status_delivery=False)
    form = DeliveryAddresseeForm(request.POST or None)
    context = {
        'form': form,
        'title_form': f'Añadiendo envio de {client} hacia {addressee}',
    }
    serial = password()
    # Aca se incrementa la deuda del cliente en base al status_delivery
    # sea True o False

    if request.method == 'POST':

        if form.is_valid():
            with transaction.atomic():
                with transaction.atomic():
                    check_existence = Delivery.objects.filter(serial=serial)

                    if not check_existence:
                        instance = form.save(commit=False)
                        instance.origin = client
                        instance.centralist = request.user
                        instance.addressee_data = addressee.data_addressee
                        instance.destiny = addressee.destiny
                        instance.setDeliveryTypeMount(instance.type_delivery)

                        if instance.status_delivery:
                            instance.type_delivery_amount = 0

                        instance.save()
                        client.updateDebit(deliverys)
                        messages.success(request, 'Añadido correctamente')
            return redirect('/clients/list')

    return render(request, 'delivery/form_delivery.html', context)


@login_required
def allDelivery(request):
    deliverys = Delivery.objects.all()
    context = {
        'deliverys': deliverys,
        'title_list': 'Todos los envios',
    }
    return(render(request, 'delivery/list_delivery.html', context))


@login_required
def paidDelivery(request):
    deliverys = Delivery.objects.filter(status_delivery=True)
    context = {
        'deliverys': deliverys,
        'title_list': 'Envios pagados',
        'title_not_delivery': 'pagados',
    }
    return(render(request, 'delivery/list_delivery.html', context))


@login_required
def notPaidDelivery(request):
    deliverys = Delivery.objects.filter(status_delivery=False)
    context = {
        'deliverys': deliverys,
        'title_list': 'Envios sin pagar',
        'title_not_delivery': 'sin pagar',
    }
    return(render(request, 'delivery/list_delivery.html', context))


@login_required
def editDelivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    context = {
        'form': DeliveryEditForm(instance=delivery),
        'title_form': 'Editando envio',
    }

    if request.method == 'POST':
        form = DeliveryEditForm(data=request.POST, instance=delivery)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.type_delivery != 'Preferencial':
                instance.setDeliveryTypeMount(instance.type_delivery)

            if instance.type_delivery == 'Preferencial':
                instance.type_delivery_amount = instance.preferred_price

            if instance.status_delivery:
                instance.type_delivery_amount = 0

            instance.save()
            client = get_object_or_404(Client, id=delivery.origin.id)
            deliverys = Delivery.objects.filter(origin=client, status_delivery=False)
            client.updateDebit(deliverys)

            form.save()
            messages.success(request, 'Editado correctamente')
            return redirect(f'/clients/all-delivery/{delivery.origin.id}')

        context['form'] = form
    return render(request, 'delivery/form_delivery.html', context)



def toPaidIndividualDelivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    context = {
        'title': f'envio {delivery}',
        'list': f'/clients/all-delivery/{delivery.origin.id}',
    }

    if request.method == 'POST':
        delivery.type_delivery_amount = 0
        delivery.status_delivery = True
        delivery.save()

        client = get_object_or_404(Client, id=delivery.origin.id)
        deliverys = Delivery.objects.filter(origin=client, status_delivery=False)
        client.updateDebit(deliverys)
        client.save()

        messages.success(request, 'Pagado correctamente')
        return redirect(f'/clients/all-delivery/{delivery.origin.id}')

        context['form'] = form
    return render(request, 'delivery/to-pay-confirm.html', context)



@login_required
def deleteLessThanDateDelivery(request, id):
    client = get_object_or_404(Client, id=id)
    context = {
        'client': client
    }
    if request.method == 'GET' and request.GET:
        date = request.GET['date']
        if not date:
            messages.error(request, 'Debe especificar una fecha')
            return redirect('delivery:delete-less-than-date', client.id)

        # worker.status = False
        deliverys = Delivery.objects.filter(
            date__lte=date, status_delivery=True, origin=client.id
        )
        count = deliverys.count()
        if not deliverys:
            messages.info(request, 'No hay envios sin pagar correspondientes o anterior a esta fecha')
            return redirect('delivery:delete-less-than-date', client.id)

        for delivery in deliverys:
            delivery.delete()

        messages.success(request, f'Se han eliminado un total de {count} envios antiguos correspondientes a "{client}"')
        return redirect('clients:list')
    return render(request, 'delivery/delete-deliverys-less-than-date.html', context)



