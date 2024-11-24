from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
  ('biomedical equipment', 'biomedical equipment'),
  ('pharmacy', 'pharmacy'),
  ('lab', 'lab'),
  ('admin', 'admin'),
]

class Product(models.Model):
  name = models.CharField(max_length=100, null=False)
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=False)
  quantity = models.PositiveIntegerField(null=False)

  def __str__(self):
    return f'{self.name}'