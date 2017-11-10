from django.conf.urls import url
from Book import views

urlpatterns = [

    url(r'^boolist/$',views.booklist),

    #静态页面显示图片
    url(r'showImg/$',views.showImg),

    #上传图片
    url(r'^upImg/$',views.upImg),
    url(r'^shangchuanImg/$',views.shangchuanImg),

    url(r'^upload_avatar/$', views.upload_avatar),  # 上传头像
    url(r'^test/$', views.test),  # 测试页面

    url(r'^page(\d*)/$',views.pageinfo),

    url(r'pagecanshu/$',views.pagecanshu)
]