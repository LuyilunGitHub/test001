from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Book.models import Bookinfo,peopleInfo,PictureInfo,AreaInfo
from django.conf import settings
from django.core import paginator
# Create your views here.


def booklist(request):
    booklist=Bookinfo.objects.all()
    context={'booklist':booklist}
    return render(request,'Book/booklist.html',context)

def showImg(request):
    return  render(request,'Book/showImg.html')

def upImg(request):

    return render(request,'Book/upImg.html')

def shangchuanImg(request):

   pic=request.FILES.get('pic')
   picname=pic.name
   path='%s/Book/%s'%(settings.MEDIA_ROOT,picname)
   with open(path,'wb') as p:
       for c in pic.chunks():
           p.write(c)
   pictureInfo =PictureInfo()
   pictureInfo.path='Book/%s'%(picname)
   pictureInfo.save()
   # imgUrl={"imgUrl":picname}
   # print(imgUrl)
   return HttpResponse(picname)


def test(request):
    return render(request, 'Book/test.html')


def upload_avatar(request):
    file_obj = request.FILES.get('avatar')
    picname = file_obj.name
    file_path ='%s/Book/%s'%(settings.MEDIA_ROOT,picname)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse(file_path)


def pageinfo(request,index):
    areainfo=AreaInfo.objects.filter(parent__isnull=True)
    paginator1 = paginator.Paginator(areainfo, 10)
    if index=="":
        index=1
    page=paginator1.page(index)

    context={"page":page}

    return render(request,"Book/pageinfo.html",context)

def pagecanshu(request):
    p= request.GET.get("p",1)

    areainfo = AreaInfo.objects.filter(parent__isnull=True)
    paginator1 = paginator.Paginator(areainfo, 10)


    page = paginator1.page(int(p))

    context = {"page": page}

    return render(request, "Book/pageFYcanshu.html", context)

