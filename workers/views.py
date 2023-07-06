
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Worker
from .forms import WorkerForm

from delivery.models import Delivery

# Create your views here.


@login_required
def listWorker(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return(render(request, 'workers/list_workers.html', context))


@login_required
def newWorker(request):
    form = WorkerForm(request.POST or None)
    context = {
        'form': form,
        'title_form': 'Añadiendo trabajador',
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.status = True
        instance.save()
        messages.success(request, 'Añadido correctamente')
        return redirect('/workers/list')

    return render(request, 'workers/form_worker.html', context)

    # if request.method == 'POST':

    #     if form.is_valid():
    #         print('as\nd\nk\nj\nf\nl\nh\na\ns\nk\nd\nf\na\ns\nd\nf\nasdflahsdfljahsldk')
    #         instance = form.save(commit=False)
    #         instance.local = get_object_or_404(Client, id=id)
    #         messages.success(request, 'Añadido correctamente')
    #         instance.save()
    #         return redirect('/clients/list')


@login_required
def editWorker(request, id):
    worker = get_object_or_404(Worker, id=id)
    context = {
        'form': WorkerForm(instance=worker),
        'title_form': 'Editando trabajador',
    }

    if request.method == 'POST':
        form = WorkerForm(data=request.POST, instance=worker)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado correctamente')
            return redirect('/workers/list')

        context['form'] = form
    return render(request, 'workers/form_worker.html', context)


@login_required
def deleteWorker(request, id):
    worker = get_object_or_404(Worker, id=id)
    context = {
        'title': f'trabajador {worker}',
        'list': f'/workers/list',
    }
    if request.method == 'POST':
        # worker.status = False
        worker.delete()
        messages.success(request, 'Eliminado correctamente')
        return redirect(f'/workers/list')
    return render(request, 'workers/delete-confirm.html', context)


@login_required
def listActivityWorker(request, id):
    worker = get_object_or_404(Worker, id=id)
    activity_worker = Delivery.objects.filter(distributing=id)
    context = {
        'activity_worker': activity_worker,
        'title': f'Lista de actividad de {worker}'
        }
    return(render(request, 'workers/list_activity_workers.html', context))

