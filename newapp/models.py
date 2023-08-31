from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class test(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    OPTION_CHOICES = (
        ('option1', 'Option One'),
        ('option2', 'Option Two'),
        ('option3', 'Option Three'),
        ('option4', 'Option Four'),
    )

    category = models.ForeignKey(test, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=8, choices=OPTION_CHOICES)


    def __str__(self):
        return self.question

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='article_files/')
 # Define the upload_to directory

    def __str__(self):
        return self.title
    
from django.conf import settings
from django.db import models

class fquestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(fquestion, on_delete=models.CASCADE)
    text = models.TextField()
