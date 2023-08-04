from django.urls import path
from .views import *

urlpatterns = [
    path('client', ClientList.as_view()),
    path('client/add', AddClient.as_view()),
    path('client/<int:pk>', ClientOperation.as_view()),

    path('product', ProductsList.as_view()),
    path('product/add', AddProduct.as_view()),
    path('product/<int:pk>', ProductOperation.as_view()),

    path('sale_item', SaleItemList.as_view()),
    path('sale_item/add', AddSaleItem.as_view()),
    path('sale_item/<int:pk>', SaleItemOperation.as_view()),

    path('sale', SaleList.as_view()),
    path('sale/add', AddSale.as_view()),
    path('sale/<int:pk>', SaleOperation.as_view()),

    path('receipt', ReceiptList.as_view()),
    path('receipt/add', AddReceipt.as_view()),
    path('receipt/<int:pk>', ReceiptOperation.as_view()),

    path('invoice', InvoiceList.as_view()),
    path('invoice/add', AddInvoice.as_view()),
    path('invoice/<int:pk>', InvoiceOperation.as_view()),
]