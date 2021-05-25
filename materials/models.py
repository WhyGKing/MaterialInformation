from django.db import models


# Create your models here.
class MaterialInfo(models.Model):
    MaterialName = models.CharField(max_length=30, null=False)
    maker = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    ChemName = models.CharField(max_length=200)
    TechInfo = models.TextField(max_length=1000)
    # TechLink = models.URLField('Site URL')
    # Attach = models.FileField

    def __str__(self):
        return self.MaterialName + " / " + self.maker


