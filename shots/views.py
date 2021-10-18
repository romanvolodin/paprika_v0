from django.views.generic.list import ListView
from django.shortcuts import render

from projects.models import Project

from .models import Shot, Version


class ShotListView(ListView):
    # model = Shot
    context_object_name = 'shot_groups'
    template_name = 'shots/shot_list.html'

    def get_queryset(self):
        project_code = self.kwargs.get('project_code', None)
        project = Project.objects.get(code=project_code)
        return project.shot_groups.all()


def shot_detail(request, project_code, shot_title):
    shot = Shot.objects.get(title=shot_title)
    try:
        latest_version = shot.versions.latest('created_at')
    except Version.DoesNotExist:
        latest_version = None
    context = {
        'shot': shot,
        'latest_version': latest_version,
    }
    return render(request, 'shots/shot_detail.html', context)