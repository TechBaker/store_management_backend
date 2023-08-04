from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.models import Product, Client, SaleItem, Sale, Receipt, Invoice
from .serializers import *

class ProductsList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class AddProduct(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductOperation(APIView):
    def get_product_by_id(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            return -1

    def get(self, request, pk):
        product = self.get_product_by_id(pk)
        if product == -1:
            return Response({
                'status': 'The product does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product_by_id(pk)
        if product == -1:
            return Response({
                'status': 'The product does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product_by_id(pk)
        if product == -1:
            return Response({
                'status': 'The product does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

class AddClient(APIView):
    def post(request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientOperation(APIView):
    def get_client_by_id(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except:
            return -1

    def get(self, request, pk):
        client = self.get_client_by_id(pk)
        if client == -1:
            return Response({
                'status': 'The client does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_client_by_id(pk)
        if client == -1:
            return Response({
                'status': 'The client does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_client_by_id(pk)
        if client == -1:
            return Response({
                'status': 'The client does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SaleItemList(APIView):
    def get(self, request):
        saleItems = SaleItem.objects.all()
        serializer = SaleItemSerializer(saleItems, many=True)
        return Response(serializer.data)

class AddSaleItem(APIView):
    def post(request):
        serializer = SaleItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleItemOperation(APIView):
    def get_sale_item_by_id(self, pk):
        try:
            return SaleItem.objects.get(pk=pk)
        except:
            return -1

    def get(self, request, pk):
        saleItem = self.get_sale_item_by_id(pk)
        if saleItem == -1:
            return Response({
                'status': 'The sale item does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = SaleItemSerializer(saleItem)
        return Response(serializer.data)

    def put(self, request, pk):
        saleItem = self.get_sale_item_by_id(pk)
        if saleItem == -1:
            return Response({
                'status': 'The sale item does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = SaleItemSerializer(saleItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saleItem = self.get_sale_item_by_id(pk)
        if saleItem == -1:
            return Response({
                'status': 'The sale item does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        saleItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SaleList(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

class AddSale(APIView):
    def post(request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleOperation(APIView):
    def get_sale_by_id(self, pk):
        try:
            return Sale.objects.get(pk=pk)
        except:
            return -1

    def get(self, request, pk):
        sale = self.get_sale_by_id(pk)
        if sale == -1:
            return Response({
                'status': 'The sale does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = SaleSerializer(sale)
        return Response(serializer.data)

    def put(self, request, pk):
        sale = self.get_sale_by_id(pk)
        if sale == -1:
            return Response({
                'status': 'The sale does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sale = self.get_sale_by_id(pk)
        if sale == -1:
            return Response({
                'status': 'The sale does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReceiptList(APIView):
    def get(self, request):
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

class AddReceipt(APIView):
    def post(request):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceiptOperation(APIView):
    def get_receipt_by_id(self, pk):
        try:
            return Receipt.objects.get(pk=pk)
        except:
            return -1

    def get(self, request, pk):
        receipt = self.get_receipt_by_id(pk)
        if receipt == -1:
            return Response({
                'status': 'The receipt does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data)

    def put(self, request, pk):
        receipt = self.get_receipt_by_id(pk)
        if receipt == -1:
            return Response({
                'status': 'The receipt does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = ReceiptSerializer(receipt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        receipt = self.get_receipt_by_id(pk)
        if receipt == -1:
            return Response({
                'status': 'The receipt does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        receipt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InvoiceList(APIView):
   def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

class AddInvoice(APIView):
    def post(request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceOperation(APIView):
    def get_invoice_by_id(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except:
            return -1

    def get(self, request, pk):
        invoice = self.get_invoice_by_id(pk)
        if invoice == -1:
            return Response({
                'status': 'The invoice does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice = self.get_invoice_by_id(pk)
        if invoice == -1:
            return Response({
                'status': 'The invoice does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        invoice = self.get_invoice_by_id(pk)
        if invoice == -1:
            return Response({
                'status': 'The invoice does not exist'
            }, status = status.HTTP_404_NOT_FOUND )
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)