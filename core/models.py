from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    barcode = models.CharField(max_length=25, unique=True)
    category = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='images/products')
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    #supplier_id = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    value_added_tax = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product_name}"

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    sale_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.id} - {self.sale_date}"

class Receipt(models.Model):
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)
    receipt_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Receipt for Sale {self.sale_id} - {self.receipt_date}"

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice for Customer {self.customer_id} - {self.invoice_date}"