from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
  ('biomedical equipment', 'biomedical equipment'),
  ('pharmacy', 'pharmacy'),
  ('lab', 'lab'),
  ('admin', 'admin'),
]

# Product model
class Product(models.Model):
  name = models.CharField(max_length=100, null=False)
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=False)
  quantity = models.PositiveIntegerField(null=False)

  class Meta:
    verbose_name_plural = 'Productos'

  def __str__(self):
    return f'{self.name} ({self.quantity})'

# Order model
class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  staff = models.ForeignKey(User, models.CASCADE, null=True)
  quantity = models.PositiveIntegerField(null=True)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Ordenes'

  def __str__(self):
    return f'{self.product} ordenada por {self.staff.username}'
