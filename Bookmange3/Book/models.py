from django.db import models

# Create your models here.


class Bookinfo(models.Model):
    name=models.CharField(max_length=20)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    isDelete=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table='bookinfo'


class peopleInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.BooleanField(default=True)
    description=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(Bookinfo)

    def __str__(self):
        return self.name


    class Meta:
        db_table='peopleinfo'


class AreaInfo(models.Model):

    name=models.CharField(max_length=30) #,verbose_name="区域名称")
    parent = models.ForeignKey('self', null=True, blank=True)#verbose_name='上级区域')  # 关系

    def __str__(self):
        return self.name

    def title(self):
        return self.name

    class Meta:
        db_table='areainfo'

    # 指定方法作为列的排序依据
    title.admin_order_field = 'name'
    # 修改模型title方法作为列的标题名称
    title.short_description = '区域名称'


class PictureInfo(models.Model):
    path=models.ImageField(upload_to='Book/')


    class Meta:
        db_table='pictureinfo'




































