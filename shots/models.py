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


class Shot(models.Model):
    title = models.CharField('Название шота', max_length=50)
    group = models.ForeignKey(
        ShotGroup,
        on_delete=models.CASCADE,
        related_name='shots'
    )
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='shots'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
