from django.views.generic.list import ListView

from projects.models import Project

from .models import Shot


class ShotListView(ListView):
    # model = Shot
    context_object_name = 'shot_groups'
    template_name = 'shots/shot_list.html'

    def get_queryset(self):
        project_code = self.kwargs.get('project_code', None)
        project = Project.objects.get(code=project_code)
        return project.shot_groups.all()