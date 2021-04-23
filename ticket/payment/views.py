from django.shortcuts import render

# Create your views here.
import csv
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the payments index.")
    if request.method=='POST':
        amount=request.POST['amount']
        print(amount)
        with open('edchemdata.csv','a') as csvfile:
            wcs=csv.writer(csvfile)
            wcs.writerow({'amount',amount})
        return render(request,'thanks.html')
    else:
        return render(request,'payment.html')

'''def survey(request, num):
    if num==1:
        return render(request,'Survey1.html')
    else:
        return render(request,'PageNotFound.html')'''
