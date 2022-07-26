from django.db import models


class Test(models.Model):
    title = models.CharField(null=False, max_length=200)
    description = models.TextField(null=False, max_length=400)
    duration = models.TimeField(null=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(null=False, max_length=200)
    description = models.TextField(null=False, max_length=400)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
