from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from os.path import join

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username}"

def product_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"product_{instance.id}.{ext}"
    return join('products', filename)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    barcode = models.CharField(max_length=25, unique=True)
    reference = models.CharField(max_length=25, unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=product_image_path, blank=True, null=True)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    value_added_tax = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product_name}"

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f" Product: {self.product.product_name}, quantity: {self.quantity}, total: {self.total_amount}"
 
class Order(models.Model):
    TYPES = [
        ("1", "IN"),
        ("-1", "OUT"),
    ]
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_type =  models.CharField(max_length=3, choices=TYPES)
    is_quote = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.order_date}"
   
class Receipt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    receipt_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Receipt for Order {self.order_id} - {self.receipt_date}"

class Supplier(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    details = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
     
class PaymentMethod(models.Model):
    METHODS = [
        ("1", "Cash"),
        ("2", "On Account"),
        ("3", "Check"),
        ("4", "Bank Card"),
    ]
    method = models.CharField(max_length=2, choices=METHODS)

class Invoice(models.Model):
    supplier = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice for Customer {self.id} - {self.invoice_date}"
   
class PaymentIn(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)

class PaymentOut(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.OneToOneField(PaymentMethod, on_delete=models.CASCADE)