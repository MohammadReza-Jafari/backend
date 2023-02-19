from django.db import models

from django.contrib.postgres import fields as psql_fields



class Task(models.Model):
    instruction = models.CharField(max_length=255)
    author_id = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    annotator_id = models.CharField(max_length=255)
    annotator_name = models.CharField(max_length=255)
    labels = psql_fields.ArrayField(
        base_field=models.CharField(max_length=255),
    )

    def __str__(self):
        return f'{self.instruction[:50]}-{self.author_name}'
