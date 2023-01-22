import re
from django.db import models

SPACE_HYPHEN_REGEX = r"\s+|-"


class Part(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=30)
    description = models.CharField(max_length=1024)
    weight_ounces = models.PositiveIntegerField()
    is_active = models.SmallIntegerField()

    def __repr__(self) -> str:
        return f"<Part: {self.name} ({self.id})>"

    def save(self, *args, **kwargs):
        old_description = Part.objects.get(pk=self.pk).description if self.pk else ""
        new_description = self.description
        DescriptionWordCount.update_word_counts(
            old_description=old_description, new_description=new_description
        )
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        old_description = Part.objects.get(pk=self.pk).description if self.pk else ""
        DescriptionWordCount.update_word_counts(
            old_description=old_description, new_description=""
        )
        return super().delete(*args, **kwargs)


class DescriptionWordCount(models.Model):
    word = models.CharField(primary_key=True, max_length=50)
    count = models.IntegerField(default=0)

    def __repr__(self) -> str:
        return f"<DescriptionWordCount: {self.word} [{self.count}]>"

    def update_word_counts(old_description: str, new_description: str) -> None:
        """Given an old and new description, updates word count records appropriately"""
        word_count_delta = DescriptionWordCount._calculate_word_count_delta(
            old_description, new_description
        )
        word_count_batch: list[DescriptionWordCount] = []

        # Update or create DescriptionWordCount records
        for word in word_count_delta.keys():
            word_count, _ = DescriptionWordCount.objects.get_or_create(pk=word)
            word_count.count += word_count_delta[word]
            word_count_batch.append(word_count)

        DescriptionWordCount.objects.bulk_update(word_count_batch, ["count"])

    def _calculate_word_count_delta(
        old_description: str, new_description: str
    ) -> dict[str, int]:
        old_description_words = DescriptionWordCount._split_description(old_description)
        new_description_words = DescriptionWordCount._split_description(new_description)
        word_count_delta = {}

        # Subtract count for words present in old description
        for word in old_description_words:
            if not word in word_count_delta:
                word_count_delta[word] = 0
            word_count_delta[word] -= 1

        # Add count for words present in old description
        for word in new_description_words:
            if not word in word_count_delta:
                word_count_delta[word] = 0
            word_count_delta[word] += 1

        return word_count_delta

    def _split_description(description: str) -> list[str]:
        return (
            re.split(SPACE_HYPHEN_REGEX, description.lower())
            if description is not ""
            else []
        )
