from django.urls import path
from . import views

urlpatterns = [
    path('client', views.getClients),
    path('client/add', views.addClient),

    path('product', views.getProducts),
    path('product/add', views.addProduct),

    path('sale_item', views.getSaleItems),
    path('sale_item/add', views.addSaleItem),

    path('sale', views.getSales),
    path('sale/add', views.addSale),

    path('receipt', views.getReceipts),
    path('receipt/add', views.addReceipt),

    path('invoice', views.getInvoices),
    path('invoice/add', views.addInvoice),
]