from django.urls import path
from django.contrib.auth import views as views_auth

from .views import deleteDelivery,notPaidDelivery, allDelivery, paidDelivery, newDelivery, editDelivery, newDeliveryAddressee, toPaidIndividualDelivery, deleteLessThanDateDelivery


urlpatterns = [
    path('all', allDelivery, name="all"),
    path('paid', paidDelivery, name="paid"),
    path('edit/<id>', editDelivery, name="edit"),
    path('not-paid', notPaidDelivery, name="not-paid"),
    path('new/<id>', newDelivery, name="new"),
    path('delete/<id>', deleteDelivery, name="delete"),
    path('new-delivery-to-addressee/<id>', newDeliveryAddressee, name="new-delivery-to-addressee"),
    path('to-pay/<id>', toPaidIndividualDelivery, name="to-pay"),
    path('delete-less-than-date/<id>', deleteLessThanDateDelivery, name="delete-less-than-date"),
]
