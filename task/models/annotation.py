from django.db import models


class Annotation(models.Model):
    label = models.CharField(max_length=255)
    left = models.FloatField()
    top = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    image = models.ForeignKey(
        to='task.Image',
        on_delete=models.CASCADE,
    )
