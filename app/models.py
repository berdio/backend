from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sms_code = models.IntegerField(blank=True, null=True)
    sms_status = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='category')
    slug = models.SlugField(max_length=125, db_index=True, unique=True)

class SubCategory(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):

    TYPE = (
        ('dona', 'шт'),
        ('m2', 'м2'),
    )
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(SubCategory(), on_delete=models.CASCADE)
    count = models.IntegerField()
    rate = models.IntegerField(default=0)
    best = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    text = models.TextField(blank=True, null=True)

class Image(models.Model):
    image = models.ImageField(upload_to='photo')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

class Colors(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=125)

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=125)


class Rate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_rate")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rate")
    comment = models.TextField(blank=True, null=True)
    rate = models.IntegerField()

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_like")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")


class OrderItem(models.Model):
    STATUS = (
        ("basket", 'basket'),
        ('wait', 'wait'),
        ('done', 'done')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=125, choices=STATUS, default='basket')

class Order(models.Model):
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="user_order", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_order")
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, related_name="color_order", blank=True, null=True)
    count = models.IntegerField()
    created_at = models.DateField(auto_created=True, auto_now_add=True)


class OrderAddress(models.Model):
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="order_address", blank=True, null=True)
    name = models.CharField(max_length=125, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    lat = models.IntegerField(blank=True, null=True)
    lng = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=125)
    comment = models.CharField(max_length=125)
    date = models.DateField(blank=True, null=True)
    deliver = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)



class Pay(models.Model):
    text = models.TextField()


class Deliver(models.Model):
    text = models.TextField()
