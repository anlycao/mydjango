from django.db import models
class Product(models.Model):
    id=models.IntegerField('序号',primary_key=True)
    name=models.CharField('名称',max_length=50)
    type=models.CharField('类型',max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='产品信息'
        verbose_name_plural="产品信息"

