import csv
from django.views.generic import ListView

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO WORLD")
def mydate(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))
def myyear(request,year):
    return render(request,'myyear.html')
def myyear_dict(request,year,month):
    return render(request,'myyear_dict.html',{'month':month})
def download(request):
    response=HttpResponse(content_type='text/csv')
    response['Content_Disposition']='attachment;filename="somefilename.csv"'
    writer=csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    return response
def index(request):
    return render(request,'indexl.html',context={'title':'首页'},status=500)

def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        return redirect('/')  #重定向，跳转首页
    else:
        if request.GET.get('name') :
            name=request.GET.get('name')
            return HttpResponse('username is ' + name)
        else:
            name=1
            return redirect('/')
'''class ProductList(ListView):
    context_object_name = 'type_list' #设置html模板变量名称
    template_name = 'index_view.html' #设定html模板
    queryset=Product.objects.values('type').distinct#查询数据
    def get_queryset(self):
        type_list=Product.objects.values('type').distinct
        return type_list
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name_list']=Product.objects.values('type','name').distinct
        return context'''
