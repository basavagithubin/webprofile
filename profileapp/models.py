from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)

    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    # Education
    education = models.TextField(blank=True, null=True)

    # Work Experience
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.title

