from django.views.generic.list import ListView

from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project_list.html'
