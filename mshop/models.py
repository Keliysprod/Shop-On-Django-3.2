from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#Продукты в мазагизе (ассортимент)
class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    mini_description=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)
    digital=models.BooleanField(default=False, null=True)
    image=models.ImageField(null=True, blank=True)

    slug=models.SlugField(unique=True, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

#Покупатель (может добавлять в корзину)
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Customer'
        verbose_name_plural='Customers'


#Заказ не до конца понял мб корзина
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    date_order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True, blank=False)
    transaction_id=models.CharField(max_length=200, null=True)

#Пункт заказа?
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True )
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

#Выдача айтема
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    zipcode=models.CharField(max_length=10, null=True)
    date_added=models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True, null=True,related_name='priducts_comment' )
    text=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)