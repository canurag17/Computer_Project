from django.shortcuts import render

# Create your views here.
#def seehome(request):
 #   return render(request,'index_v3')

'''def survey(request, num):
    if num==1:
        return render(request,'index_v3.html')
    else:
        return render(request,'PageNotFound.html')'''

def seepayment(request):
    if request.method =="POST":

        amount=request.POST['amount']
        cardno=request.POST['cardno']
        #code to save data to the database
        lst = Payment()
        lst.pno=1
        lst.pcardno =cardno
        lst.pamount = amount
        lst.save()
        return render(request,'thankyou.html')

    else:

        return render(request,'payment.html')


