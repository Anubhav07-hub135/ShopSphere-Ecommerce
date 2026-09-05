from django.db import models
from django.contrib.auth.models import User


# -------------------------
# Category Model
# -------------------------

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# -------------------------
# Product Model
# -------------------------

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='products/'
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    available = models.BooleanField(
        default=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


# -------------------------
# Order Model
# -------------------------

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    created = models.DateTimeField(
        auto_now_add=True
    )

    paid = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Order {self.id} - {self.name}"

    def get_total_cost(self):
        return sum(
            item.get_cost()
            for item in self.items.all()
        )


# -------------------------
# Order Item Model
# -------------------------

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.SET_NULL,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        if self.product:
            return f"{self.quantity} x {self.product.name}"

        return f"{self.quantity} x Deleted Product"

    def get_cost(self):
        return self.price * self.quantity