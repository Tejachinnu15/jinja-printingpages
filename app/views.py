from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'ashu','age':10,'name':'nikky'}
    return render(request,'wish.html',context=d)
