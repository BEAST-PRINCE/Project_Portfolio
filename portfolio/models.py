from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag , related_name='projects', blank=True)
    link = models.URLField(blank=True, max_length=500)

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_image/')

    def __str__(self):
        return f"{self.project.title} Image"