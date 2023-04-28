from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax = 15

def index(request):
 return render(request, 'taxapp/index.html')


def anyNumber(request, num):
  total = num + num*tax/100
  
  return render(request, 'taxapp/anyNumber.html', context={"total":total, "initial":num, "tax":tax})

def taxrate(request):
    return render(request, 'taxapp/taxrate.html', context={"tax_rate":0.15})