from django.urls import path
from .views import *

urlpatterns = [
    path('clients', ClientList.as_view()),   
    path('client/add', AddClient.as_view()),
    path('client/<int:pk>', ClientOperation.as_view()),

    path('products', ProductsList.as_view()),
    path('product/add', AddProduct.as_view()),
    path('product/<int:pk>', ProductOperation.as_view()),
    path('product/barcode/<str:barcode>', ProductByBarcode.as_view()),

    path('order_items', OrderItemList.as_view()),
    path('order_item/add', AddOrderItem.as_view()),
    path('order_item/<int:pk>', OrderItemOperation.as_view()),

    path('orders', OrderList.as_view()),
    path('order/add', AddOrder.as_view()),
    path('order/<int:pk>', OrderOperation.as_view()),

    path('receipts', ReceiptList.as_view()),
    path('receipt/add', AddReceipt.as_view()),
    path('receipt/<int:pk>', ReceiptOperation.as_view()),

    path('invoices', InvoiceList.as_view()),
    path('invoice/add', AddInvoice.as_view()),
    path('invoice/<int:pk>', InvoiceOperation.as_view()),
]