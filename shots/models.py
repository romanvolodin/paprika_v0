from django.db import models


class ShotGroup(models.Model):
    title = models.CharField('Название группы шотов', max_length=50)
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='shot_groups'
    )

    def __str__(self) -> str:
        return self.title
