from django.db import models


# Create your models here.
class Facility(models.Model):
    """
    テストテーブル
    """

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
