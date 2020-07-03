from django.db import models

class Objective(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class KeyResult(models.Model):
    title = models.CharField(max_length=128)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
