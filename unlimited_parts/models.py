from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=30)
    description = models.CharField(max_length=1024)
    weight_ounces = models.PositiveIntegerField()
    is_active = models.SmallIntegerField()

    def __repr__(self) -> str:
        return f"<Part: {self.name} ({self.id})>"


class DescriptionWordCount(models.Model):
    word = models.CharField(primary_key=True, max_length=50)
    count = models.IntegerField(default=0)

    def __repr__(self) -> str:
        return f"<DescriptionWordCount: {self.word} [{self.count}]>"
