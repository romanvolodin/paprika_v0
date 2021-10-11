from django.db import models


class Project(models.Model):
    title = models.CharField('Название проекта', max_length=255)
    code = models.CharField('Код проекта', max_length=5)
    preview = models.ImageField('Превью', blank=True, null=True)
    deadline = models.DateTimeField('Дедлайн', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
        related_name='created_projects'
    )

    def __str__(self):
        return self.code
