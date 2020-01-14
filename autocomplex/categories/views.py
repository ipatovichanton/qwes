from django.shortcuts import render
from .models import Details

def categories(request):
    return render(request,)

def moscow_detail(request):
    moscow_detail=Details.object.filter(option='moscow_detail')
    context={
        'product': moscow_detail
    }
    return render(request,context)

def sliva_detail(request):
    sliva_detail=Details.object.filter(option='sliva_detail')
    context={
        'product':sliva_detail
    }
    return render (request,context)

def volga_detail(request):
    volga_detail=Details.object.filter(option='volga_detail')
    context={
        'product':volga_detail
    }
    return render (request,context)

