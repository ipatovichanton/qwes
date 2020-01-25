from django.shortcuts import render
from .models import Details

def categories(request):
    return render(request,)

def moscow_detail(request):
    moscow_detail= Details.objects.Filter(option='moscow_detail')
    context = {
        'products':moscow_detail
    }
    return render(request,context,)

def sliva_detail(request):
    sliva_detail=Details.objects.Filter(option='sliva_detail')
    context= {
        'products':sliva_detail
    }
    return render(request,context,)

def volga_detail(request):
    volga_detail= Details.objects.Filter(option='volga_detail')
    context= {
        'products':volga_detail
    }
    return render(request,context,)