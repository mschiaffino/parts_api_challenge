from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=30)
    description = models.CharField(max_length=1024)
    weight_ounces = models.PositiveIntegerField()
    is_active = models.SmallIntegerField()

    def __repr__(self) -> str:
        return f"<Part: {self.name} ({self.id})>"
