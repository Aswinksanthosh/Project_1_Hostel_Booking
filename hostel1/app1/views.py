from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import HttpResponse
from . models import *
from . forms import *
import re
import math
from datetime import datetime
# Create your views here.
def display_session(request):       #display session datas here url-session
    context = {'session_data': request.session}
    return render(request, 'app1/session.html', context)
def userreg(request):
    print('user reg starts here')
    session_data = request.session
    print(session_data)
    if request.method=='POST':
        phno=request.POST['phno']   #for checking duplicates
        gmail=request.POST['gmail']
        pwd=request.POST['pwd']
        name=request.POST['name']
        # frm=user_reg_valid()
        # frm=frm(phno=phno,gmail=gmail,pwd=pwd,name=name)
        frm=user_reg_valid(request.POST)
        if frm.is_valid():
            if User_registration.objects.filter(gmail=gmail):
                return HttpResponse('Username already exists.')
            else:
                data=User_registration(phno=phno,gmail=gmail,pwd=pwd,name=name)
                data.save()
        else:
            return HttpResponse('invalid form')
    return render(request,'app1/login.html',)

def adminreg(request):      #url    adminreg
    if request.method=='POST':
        phno=request.POST['phno']
        gmail=request.POST['gmail']
        pwd=request.POST['pwd']
        name=request.POST['name']
        # frm=user_reg_valid()
        # frm=frm(phno=phno,gmail=gmail,pwd=pwd,name=name)
        frm=user_reg_valid(request.POST)
        if frm.is_valid():
            if admin_reg.objects.filter(gmail=gmail):
                return HttpResponse('admin already exists')
            else:
                data=admin_reg(phno=phno,gmail=gmail,pwd=pwd,name=name)
                data.save()
        else:
            return HttpResponse('invalid form')
    return render(request,'app1/admin_login.html',)


def login1234(request):#url - login1
    expire(request)
    print('login working'*10,'login1234')
    a2 = login12()  #empty model 'a2' created for insertion                        
    reg = User_registration.objects.all()# Multiple records from signup database inserted to 'reg'
    if request.method == 'POST':# Code works only after clicking 'SUBMIT' button
        a2 = login12(request.POST)# userinput inserted to a2 via POST---(username and password)
        if a2.is_valid():
            for i in reg:                  #all records from 'reg' extrated to 'i'
                print('login1234/ni----------------',i)
                print('data type---------',type(i))
                e = request.POST['gmail']   #from user
                p = request.POST['pwd']    #from user
                if e == i.gmail and p == i.pwd:    #checking match
                    request.session['login']=e      #setting session
                    # if 'user' in request.session:
                    #     del request.session['user']
                    request.session['user']='USER'
                    para={'login':request.session['login'],'user':request.session['user']}
                    return redirect('search')
    return render(request,'app1/login.html')

def adminlogin1234(request):#url - adminlogin
    print('/n/n','-'*50,'adminlogin1234')
    a2 = login12()  #empty model 'a2' created for insertion                        
    reg = admin_reg.objects.all()# Multiple records from signup database inserted to 'reg'
    if request.method == 'POST':# Code works only after clicking 'SUBMIT' button
        a2 = login12(request.POST)# userinput inserted to a2 via POST---(username and password)
        if a2.is_valid():
            for i in reg:                  #all records from 'reg' extrated to 'i'
                print('adminlogin1234i----------------',i)
                print('data type---------',type(i))
                e = request.POST['gmail']   #from user
                p = request.POST['pwd']    #from user
                if e == i.gmail and p == i.pwd:    #checking match
                    request.session['login']=e      #setting session
                    # if 'user' in request.session:
                    #     del request.session['user']
                    request.session['user']='ADMIN'
                    return redirect('admin_hostel')
            print('/nno match ADMINLOGIN')
    return render(request,'app1/admin_login.html')

def base(request):      #url-   base
    return render(request,'app1/base.html')

def base2(request):     #url-   base2
    return render(request,'app1/base2.html')

def search(request):      #url-   search
    expire(request)
    param={}    
    user=request.session['user']
    param['user']=user    
    login=request.session['login']
    param['login']=login
    try:
        userdet = User_registration.objects.get(gmail=login)
    except User_registration.DoesNotExist as e:
        print("Exception:", e)
        return redirect(userreg)

    print('-'*50)
    print('userdethid',userdet.h_id)
    if userdet.h_id:
        formdet=hostels.objects.get(h_id=userdet.h_id)
        param.update({'userdet':userdet,'formdet':formdet})
    if request.method =='POST':
        place=request.POST['address']
        data = hostels.objects.filter(address__regex=r'{}'.format(place)).exclude(share4='0', share6='0', share8='0', share10='0')
        # data = hostels.objects.filter(Q(address__regex=r'{}'.format(place)) & ~Q(share4='0') & ~Q(share6='0') & ~Q(share8='0') & ~Q(share10='0')) both are working
        param['data']=data
        print('-'*50,param,'\n',data)
        return render(request,'app1/search.html',param)
    if 'data' in param:
        del param['data']
    return render(request,'app1/search.html',param)

def logout(request):
    if 'login' in request.session:
        del request.session['login']
    if 'user' in request.session:
        del request.session['user']
    return redirect(userreg)

def admin_hostel(request):
    expire(request)
    admin=request.session['login']
    print('admin_hostel','-'*59,admin)
    para={'login':request.session['login'],'user':request.session['user']}
    context={'data':hostels.objects.filter(gmail=admin)}
    para.update(context)
    return render(request,'app1/admin_page.html',para)
def hosteladd(request):     #-url 
    print('-'*50,'hosteladd')
    if request.method == 'POST':
        a2 = hostel_add(request.POST, request.FILES)
        name=request.POST['name']
        if hostels.objects.filter(name=name).count()>0:
            return HttpResponse('Name already exist')
        if a2.is_valid():   
            print(a2.data)
            print('hosteladd')
            print(request.session['login'])
            a2.save()
            print('-'*50)
            print('saved succefully')
            return HttpResponse('data saved')
        else:
            print('-'*50)
            print(a2.errors)
            return render(request,'app1/hosteladd.html',{'error':a2.errors})
    else:
        form=hostel_add()
    gmail=request.session['login']
    print('-'*50,'hosteladd------end')
    para={'login':request.session['login'],'user':request.session['user'],'gmail':gmail,'form':form}
    return render(request,'app1/hosteladd.html',para)
def hostel_update(request, h_id):
    data = get_object_or_404(hostels, h_id=h_id)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return render(request,'app1/updatesucces.html')
    else:
        print('invalid')
        form = EditForm(instance=data)
        para={'login':request.session['login'],'user':request.session['user'],'form': form, 'data': data}
    return render(request, 'app1/hostel_update.html', para)
def user_submit(request,h_id):
    param={}    
    user=request.session['user']
    param['user']=user    
    login=request.session['login']
    param['login']=login
    form=hostels.objects.get(h_id=h_id)
    user = User_registration.objects.get(gmail=login)
    print(user.h_id)
    if user.h_id:
        param.update({'userdet':user,'formdet':form})
        param['error']='User already booked'
        # pr4=int(form.price4)
        # made by Aswin K Santhosh
        # pr6=int(form.price6)
        # pr8=int(form.price8)
        # pr10=int(form.price10)
        # print('form.price4:',form.price4,type(form.price4))
        # print('pr4:',pr4,type(pr4))
        # param.update({'pr4':pr4,'pr6':pr6,'pr8':pr8,'pr1':pr10})
    elif request.method=='POST':
        print('-'*50,'post started')
        # Get the selected room type from the input field
        field = request.POST.get('room-type')
        print('field:',field)
        # Get the hostel object from the hostels table using the h_id
        hostel = hostels.objects.get(h_id=h_id)
        
        # Decrement the value of the selected room type field in the hostels table by 1
        current_value = getattr(hostel, field)
        if current_value > 0:
            setattr(hostel, field, current_value - 1)
        else:
            return HttpResponse('room fully booked')

        # Get the User_registration object using the login email

        # Get the price and sharing values from the respective dictionaries
        prices = {'share4': form.price4, 'share6': form.price6, 'share8': form.price8, 'share10': form.price10}
        price = prices[field]
        sharing=field

        # Get the ck_in and ck_out from the input fields
        ck_in = request.POST.get('ck_in')
        ck_out = request.POST.get('ck_out')
        ck_ind=datetime.strptime(ck_in,'%Y-%m-%d')
        ck_outd=datetime.strptime(ck_out,'%Y-%m-%d')
        day=(ck_outd-ck_ind).days
        print('*'*50)
        print('dayspassed:',day,type(day))
        if day>30:
            priceday=math.ceil(price/30*day)
            print('true')
        else:
            print('false')
            priceday=price
            print('monthpassed')
        print('-'*50,'checking datas',ck_in,'\n',ck_out,'\n',sharing,'\n',h_id,'\n',priceday)
        # Update the ck_in, ck_out, sharing, h_id, price fields in the User_registration table
        print('_'*50)
        print('price:',price)
        print('priceday:',priceday)
        print('share:',sharing)
        print('diff:',(ck_outd-ck_ind).days)
        user.ck_in = ck_in
        user.ck_out = ck_out
        user.sharing = sharing
        user.h_id = h_id
        user.price = priceday
        par={'ck_in':ck_in,'ck_out':ck_out,'sharing':sharing,'h_id':h_id,'price':priceday,'hname':form.name,'field':field}
        return render(request,'app1/confirm.html',par)
    # Pass the form variable to the template context
    param['form']=form
    print(param)
    return render(request,'app1/user_submit.html',param)
def del_booking(request,field):
    print('del start')
    user=request.session['user']
    login=request.session['login']
    user = User_registration.objects.get(gmail=login)
    hostel = hostels.objects.get(h_id=user.h_id)
    # Increment the value of the selected room type field in the hostels table by 1
    current_value = getattr(hostel, field)
    setattr(hostel, field, current_value + 1)
    hostel.save()
    User_registration.objects.filter(gmail=login).update(ck_in=None,ck_out=None,price_paid=None,sharing=None,h_id=None,price=None)
    print('-'*50)
    print('delete success')

def expire(request):
    users = User_registration.objects.all()
    print(type(datetime.today().date()))
    for user in users:
        print('-'*50)
        print(type(user.ck_out))
        # date_object = datetime.datetime.strptime(user.ck_out, "%Y-%m-%d").date()
        if user.ck_out:
            if user.ck_out <= datetime.today().date():
                del_booking(request, user.sharing)
                print('user deleted')

def confirm(request):      #-url-confirm 
    param={}    
    user=request.session['user']
    param['user']=user    
    login=request.session['login']
    param['login']=login
    if request.method=='POST':
        print('8'*50,'request starts here')
        ck_in = request.POST.get('ck_in')
        print('ck_in:',ck_in)
        ck_out = request.POST.get('ck_out')
        print('ck_out:',ck_out)
        h_id = request.POST.get('h_id')
        print('h_id:',h_id)
        sharing = request.POST.get('sharing')
        print('sharing:',sharing)
        price = request.POST.get('price')
        print('price:',price)
        field = request.POST.get('field')
        print('field:',field)
        user = User_registration.objects.get(gmail=login)
        user.ck_in = ck_in
        user.ck_out = ck_out
        user.sharing = sharing
        user.h_id = h_id
        user.price = price
        form = hostels.objects.get(h_id=h_id)
        # Decrement the value of the selected room type field in the hostels table by 1
        current_value = getattr(form, field)
        setattr(form, field, current_value - 1)
        user.save()
        form.save()
        return HttpResponse("BOOKED SUCCESSFULLY<br> <a class='btn btn-info' href='/a1/search'>BACK</a>")
    return HttpResponse('no post')

def del_booking_single(request,HName):
    print('-'*50)
    print('del single  start')
    print(HName)
    del_booking(request,HName)
    print('-'*50)
    print('single delete success')
    return redirect('search')