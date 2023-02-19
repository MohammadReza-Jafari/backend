from django.db import models


class Image(models.Model):
    url = models.URLField(max_length=1000)
    status = models.CharField(max_length=20)
    task = models.ForeignKey(
        to='task.Task',
        on_delete=models.CASCADE,
        related_name='images',
    )

    def __str__(self):
        return f'{self.status}-{self.task_id}'
