from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db import connection
from accounts.models import *

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup2.html'

def login(request):
    return render(request,'login.html')



def thanks(request):
    return render(request,'thanks.html')

def see_book(request):
    #print("ASFDFasdfsdfsd")
    cursor=connection.cursor()
    if request.method=="POST":
        flying_from = request.POST['flying_from']
        flying_to=request.POST['flying_to']
        departing=request.POST['departing']
        returning=request.POST['returning']
        adults=request.POST['adults']
        children=request.POST['children']
        travel_class=request.POST['travel_class']
        cursor.execute('select id from auth_user where last_login = (select max(last_login) from auth_user)')
        user_id=(cursor.fetchall())[0][0]
        print(user_id)
        lst = book()
        lst.flying_from=flying_from
        lst.flying_to=flying_to
        lst.departing=departing
        lst.returning=returning
        lst.adults=adults
        lst.children=children
        lst.travel_class=travel_class
        lst.user_id=user_id
        cursor=connection.cursor()
        fl=Flights.objects.filter(Departure_City=flying_from,Arrival_City=flying_to)
        if len(fl)!=0:
            lst.save()

        
        #print(departing,returning,"ASDF")
        

        c = {'c':fl}
        print(len(fl))
        if len(fl)==0:
            return render(request,'thanks.html')
        else:
            return render(request,'confirmation.html',c)
        
    else:
        
        return render(request,'book.html')

def see_logout(request):
     return render(request,'index_v3_lo.html')
    
def confirmation(request):
    if request.method=="POST":
        departing=request.POST['departing']
        returning=request.POST['returning']
        
        fl=Flights.objects.get(Departure_City=departing,Arrival_City=returning)
        c = {'c':fl}

        return render(request,'confirmation.html',{'c':fl})

'''def see_book2(request):
    if request.method=="POST":
        Name=request.POST['Name']
        Person=request.POST['Person']
        Phone=request.POST['Phone']
        Email=request.POST['Email']
        lst2=book2()
        lst2.Name=Name
        lst2.Person=Person
        lst2.Phone=Phone
        lst2.Email=Email
        ls2.save()
        return render(request,'book2.html')

    else:
        return render(request,'book2.html')'''
        
#request.session['name']=value -to access var across fns
def history(request):
    cursor=connection.cursor()
    cursor.execute('select id from auth_user where last_login = (select max(last_login) from auth_user)')
    user_id2=(cursor.fetchall())[0][0]
    print(user_id2)
    cursor.execute('select * from accounts_book where user_id={}'.format(user_id2))
    h=(cursor.fetchall())
    print(h)
    if len(h)==0:
        return render(request,'thanks.html')
    else:
        fl=book.objects.filter(user_id=h[0][8])
        print(fl)
        c = {'c':fl}
        return render(request,'history.html',{'c':fl})  


    
    
        
    
        
    


    
    '''for a in h_list(len(h)):
        print(h_list)
    return render(request,'history.html')'''
    


