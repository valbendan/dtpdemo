from django.db import models


# Create your models here.

class DemoModel(models):
    title = models.TextField(verbose_name='w')
    world: str = models.CharField(max_length=23)

    def cool(self) -> "DemoModel":
        return self
