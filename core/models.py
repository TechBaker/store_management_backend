from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    barcode = models.CharField(max_length=25, unique=True)
    reference = models.CharField(max_length=25, unique=True)
    category = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='products', blank=True, null=True)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    #supplier_id = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    value_added_tax = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product_name}"

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class SaleItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f" Product: {self.product.product_name}, quantity: {self.quantity}, total: {self.total}"
 
class Sale(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    items = models.ForeignKey(SaleItem, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.id} - {self.sale_date}"
   
class Receipt(models.Model):
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)
    receipt_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Receipt for Sale {self.sale_id} - {self.receipt_date}"

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice for Customer {self.customer_id} - {self.invoice_date}"