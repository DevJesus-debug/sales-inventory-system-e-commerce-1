from django.core.validators import *
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.urls import reverse
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField



class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_list", kwargs={"slug": self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    brand_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    model = models.CharField(max_length=250)
    product_image = models.ImageField(default="default.png", upload_to="product_image/")
    # product_image = CloudinaryField("profile_image")
    product_description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    in_stock = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(1)])
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "product"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


class OrderHistory(models.Model):
    Delivert_Status = (
        (1, "Pending"),
        (2, "Out for Delivery"),
        (3, "Delivered"),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.BigIntegerField(default=1, validators=[MinValueValidator(1)])
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    payment_status = models.BooleanField(default=True)
    paystack_order_id = models.CharField(max_length=250)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    delivery_status = models.CharField(
        choices=Delivert_Status, default="Pending", max_length=100)
    phone_no = PhoneField(blank=True, help_text="contact phone number")

    def __str__(self):
        return self.product.name
