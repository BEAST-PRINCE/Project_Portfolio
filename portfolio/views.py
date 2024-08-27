from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, ProjectImage

def home_page(request):
    projects = Project.objects.order_by('title')
    tags = Tag.objects.all()
    
    return render(request, 'home_page.html', {'projects': projects, 'tags': tags})

def contact_me(request):
    return render(request, 'contact_me.html')

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'project.html', {'project': project})