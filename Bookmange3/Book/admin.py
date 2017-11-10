from django.contrib import admin

# Register your models here.

from Book import models

admin.site.register(models.Bookinfo)


class peopleAdminShow(admin.ModelAdmin):
    list_display=['id','name','description','isDelete','book']


admin.site.register(models.peopleInfo,peopleAdminShow)


class AreaStackedInline(admin.StackedInline):
    model = models.AreaInfo  # 关联子对象
    extra = 2  # 额外编辑2个子对象

#areainfo站点管理
class AreainfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_bottom = True
    actions_on_top= False
    list_display = ['id','name','parent','title']
    #右侧兰过滤器
    list_filter = ['name']
    #查找
    search_fields = ['name','id']
    #编辑页面排序
    # fields = ['parent','name']
   #分组
    fieldsets = (
        ('子区域',{'fields':('name',)}),
        ('父区域',{'fields':('parent',)})
    )
    inlines = [AreaStackedInline]




admin.site.register(models.AreaInfo,AreainfoAdmin)

admin.site.register(models.PictureInfo)