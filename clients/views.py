from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Client, Addressee, Payment
from .forms import ClientForm, AddresseeForm, PaymentForm
from delivery.models import Delivery

from .fixes import checkDuplicity

# Create your views here.


@login_required
def listClient(request):
    clients = Client.objects.all()
    checkDuplicity()
    context = {'clients': clients}
    return(render(request, 'clients/list_clients.html', context))


@login_required
def newClient(request):
    form = ClientForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'title_form': 'Añadiendo cliente',
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Añadido correctamente')
            return redirect('/clients/list')

    return render(request, 'clients/form_client.html', context)


@login_required
def editClient(request, id):
    client = get_object_or_404(Client, id=id)
    context = {
        'form': ClientForm(instance=client),
        'title_form': 'Editando cliente',
    }

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado correctamente')
            return redirect('/clients/list')

        context['form'] = form
    return render(request, 'clients/form_client.html', context)


@login_required
def allDelivery(request, id):
    deliverys = Delivery.objects.filter(origin=id)
    client = get_object_or_404(Client, id=id)
    context = {
        'title': f'Todos los envios de "{client}"',
        'deliverys': deliverys,
        'title_deliverys_not_found': f'No hay envios registrados para "{client}"',
    }
    return render(request, 'clients/list_deliverys.html', context)


@login_required
def notPaidDelivery(request, id):
    deliverys = Delivery.objects.filter(origin=id, status_delivery=False)
    client = get_object_or_404(Client, id=id)
    context = {
        'title': f'Envios sin pagar de {client}',
        'deliverys': deliverys,
        'title_deliverys_not_found': f'No hay envios sin pagar para "{client}"',
    }
    return render(request, 'clients/list_deliverys.html', context)


@login_required
def paidDelivery(request, id):
    deliverys = Delivery.objects.filter(origin=id, status_delivery=True)
    client = get_object_or_404(Client, id=id)
    context = {
        'title': f'Envios pagos de {client}',
        'deliverys': deliverys,
        'title_deliverys_not_found': f'No hay envios pagos para "{client}"',
    }
    return render(request, 'clients/list_deliverys.html', context)


@login_required
def listAddressee(request, id):
    name_local = get_object_or_404(Client, id=id)
    addressees = Addressee.objects.filter(local=id)
    context = {
        'addressees': addressees,
        'title': f'Listado de consumidores de "{name_local}"',
    }
    return(render(request, 'clients/list_addressee.html', context))


@login_required
def listAllAddressee(request):
    addressees = Addressee.objects.all()
    context = {
        'addressees': addressees,
        'title': f'Listado de todos los consumidores frecuentes',
    }
    return(render(request, 'clients/list_addressee.html', context))


# Nuevo destinatario al cual se le asigna el local ForeignKey de manera manual
@login_required
def newAddressee(request, id):
    name_local = get_object_or_404(Client, id=id)
    form = AddresseeForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        'title_form': f'Añadiendo consumidor de "{name_local}"',
    }

    # Asignacion manual del ForeignKey
    if request.method == 'POST':

        if form.is_valid():
            print('as\nd\nk\nj\nf\nl\nh\na\ns\nk\nd\nf\na\ns\nd\nf\nasdflahsdfljahsldk')
            instance = form.save(commit=False)
            instance.local = get_object_or_404(Client, id=id)
            messages.success(request, 'Añadido correctamente')
            instance.save()
            return redirect('/clients/list')

    return render(request, 'clients/form_addressee.html', context)


# from django.views.generic import CreateView
# class NewAddressee(CreateView):
#     form_class = AddresseeForm
#     model = Addressee
#     success_url = '/clients/list'

#     def get_context_data(self, **kwargs):
#         print(self.get_context_data(**kwargs))
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'view_type': 'create',
#             })
#         return context

@login_required
def editAddressee(request, id):
    addressee = get_object_or_404(Addressee, id=id)
    context = {
        'form': AddresseeForm(instance=addressee),
        'title_form': 'Editando consumidor',
    }

    if request.method == 'POST':
        form = AddresseeForm(request.POST, request.FILES, instance=addressee)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado correctamente')
            return redirect(f'/clients/list-addressee/{addressee.local.id}')

        context['form'] = form
    return render(request, 'clients/form_addressee.html', context)


@login_required
def deleteAddressee(request, id):
    addressee = get_object_or_404(Addressee, id=id)
    title = addressee.data_addressee
    id_local = addressee.local.id
    context = {
        'title': f'consumidor {addressee}',
        'list': f'/clients/list-addressee/{id_local}',
    }
    if request.method == 'POST':
        addressee.delete()
        messages.success(request, 'Eliminado correctamente')
        return redirect(f'/clients/list-addressee/{id_local}')
    return render(request, 'clients/delete-confirm.html', context)


@login_required
def newPayment(request, id):
    from .process import paid

    client = get_object_or_404(Client, id=id)
    form = PaymentForm(request.POST or None)
    context = {
        'form': form,
        'title_form': f'Añadiendo pago de "{client}"',
    }

    # Se hace el pago por abono y se cobra iterando los datos uno a uno
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        instance.centralist = request.user
        deliverys = Delivery.objects.filter(origin=id, status_delivery=False)

        # se pasan los datos a una de lass funciones del el archivo
        # "process.py" para haccer lo corresondiente al pago por abono
        data = paid(client, deliverys, instance, request)
        data['message']
        return data['redirect_a']
    return render(request, 'clients/form_payment.html', context)


@login_required
def dateFilter(request, id):
    client = get_object_or_404(Client, id=id)
    context = {'client': f'"{client}"', }
    if request.method == 'GET' and request.GET:
        if not request.GET['date_init'] or not request.GET['date_finish']:
            messages.error(
                request, 'Alguna de las fechas esta vacia o es invalida')
            return redirect(f'/clients/date-filter/{id}')

        date_init = request.GET['date_init']
        date_finish = request.GET['date_finish']
        deliverys = Delivery.objects.filter(
            date__range=[date_init, date_finish, ], origin=id
        )
        if not deliverys:
            messages.info(
                request, 'No hay pagos correspondientes a estas fechas')
            return redirect(f'/clients/date-filter/{id}')

        debit = 0
        for delivery in deliverys:
            if not delivery.status_delivery:
                debit += delivery.type_delivery_amount

        context = {
            'client': f'"{client}"',
            'deliverys': deliverys,
            'date_init': date_init,
            'date_finish': date_finish,
            'debit': f'La deuda arrojada es de {debit}$'
        }
        return render(request, 'clients/list_deliverys_datatable.html', context)
    return render(request, 'clients/list_deliverys_date_filter.html', context)


@login_required
def listPayment(request, id):
    client = get_object_or_404(Client, id=id)
    payments = Payment.objects.filter(client=id)
    context = {
        'payments': payments,
        'client': f'"{client}"',
    }
    return(render(request, 'clients/list_payments.html', context))
