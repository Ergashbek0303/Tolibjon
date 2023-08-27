from django.db import models
from django.utils.translation import gettext as _
from users.models import User


# Create your models here.


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(_("name"),max_length=50)
    surname=models.CharField(_("surname"),max_length=50)
    phone_number=models.CharField(_("tel"),max_length=13)
    birthday=models.DateField(_("birth"))
    gender=models.CharField(_("gender"),max_length=6)




class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name


class Orders(models.Model):
    order_status = models.BooleanField(_("status"),default=True)
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"Order #{self.order_id} - {self.user.username}"



class Basket(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"shop for {self.user.username} | product {self.product.name} "
    
    def sum(self):
        return self.product.price*self.quantity


