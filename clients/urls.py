from django.urls import path
from django.contrib.auth import views as views_auth

from .views import (
    editAddressee, editClient,      listClient, listPayment,   newClient, 
    newPayment,    notPaidDelivery, paidDelivery,
    allDelivery,   listAddressee,   newAddressee, dateFilter, deleteAddressee,
    listAllAddressee
)

urlpatterns = [
    # basic client views
    path("list", listClient, name="list"),
    path("new", newClient, name="new"),
    path("edit/<id>", editClient, name="edit"),

    # client views delivery asociated
    path("all-delivery/<id>", allDelivery, name="all-delivery"),
    path("paid-delivery/<id>", paidDelivery, name="paid-delivery"),
    path("not-paid-delivery/<id>", notPaidDelivery, name="not-paid-delivery"),

    # client addressee view
    path("list-addressee/<id>", listAddressee, name="list-addressee"),
    path("list-all-addressee", listAllAddressee, name="list-all-addressee"),
    path("new-addressee/<id>", newAddressee, name="new-addressee"),
    path("edit-addressee/<id>", editAddressee, name="edit-addressee"),
    path("delete-addressee/<id>", deleteAddressee, name="delete-addressee"),

    # Amount process view
    path("new-payment/<id>", newPayment, name="new-payment"),
    path("date-filter/<id>", dateFilter, name="date-filter"),

    # payment view
    path("list-payment/<id>", listPayment, name="list-payment"),
]
