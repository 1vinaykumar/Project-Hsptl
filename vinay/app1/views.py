from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Register,Appoint,Appointment
from .forms import Login_form,Login,Forgot_pass,Edit_form,Book_app
import datetime
# Create your views here.



def home(request):
    if request.session.has_key('user_name'):
        return redirect('signin')
    con= {
        'title': 'Home'
    }
    return render(request, 'index.html',con)



def register(request):
    valid=""
    reg=False
    if request.session.has_key('user_name'):
        return redirect('signin')
    mform = Login_form(request.POST or None)
    if mform.is_valid():
        mform.save()
        valid="Registration Successful"
        reg=True
    con = {
        'form': mform,
        'title': 'Register',
        'val': valid,
        'regd':reg
    }
    return render(request, "register.html", con)



def signin(request):
    form1=Login(request.POST or None)
    stat=''
    if request.session.has_key('user_name') and request.session.has_key('priv'):
        user=request.session['user_name']
        priv=request.session['priv']
        if priv==1 or priv=='1':
            return redirect('user')
        elif priv==7 or priv=='7':
            return redirect('priv_user')
    elif request.method=='POST':
        if form1.is_valid():
            form2=form1.cleaned_data
            if Register.objects.filter(userName=form2['userName']).exists():
                list1=Register.objects.get(userName=form2['userName'])
                if list1.password==form2['password']:
                    if list1.priv==1 or list1.priv=='1':
                        response = redirect('user')
                        title='User Home'
                    elif list1.priv==7 or list1.priv=='7':
                        response = redirect('priv_user')
                        title='Priv User Home'
                    request.session['user_name']=form2['userName']
                    request.session['priv']=list1.priv
                    request.session['title']=title
                    return response
                else:
                    stat='Wrong Password'
            else:
                stat='Invalid User Name'
    try:
        return render(request,'signin.html', {'title': 'Login', 'form': form1, 'stat': stat})
    except:
        return redirect('register')



def forgot(request):
    form1= Forgot_pass(request.POST or None)
    
    valid=""
    if request.method=='POST':
        if form1.is_valid():
            form2=form1.cleaned_data
            
            if Register.objects.filter(userName=form2['userName']).exists():
                list1= Register.objects.get(userName=form2['userName'])
                if form2['mobile']==list1.mobile and form2['email']==list1.email:
                    valid="Authentication Sccessful User Name: "+list1.userName+" Password: "+list1.password
            else:
                valid="User Not available"
            
    con = {
        'title': 'Forgot Details',
        'form': form1,
        'val': valid
    }
    return render(request, 'forgot.html',con)



def user_base(request):
    user=request.session['user_name']
    priv=request.session['priv']
    if priv==7 or priv=='7':
        return redirect('priv_user')
    return render(request, 'user_base.html', {'user': user, 'title': 'User Home'})



def user_edit(request):
    reg=False
    suc=""
    priv=request.session['priv']
    if priv==7 or priv=='7':
        return redirect('priv_edit')
    user=request.session['user_name']
    mreg=Register.objects.get(userName=user)
    mform=Edit_form(request.POST or None,instance=mreg)
    if mform.is_valid():
        mform.save()
        reg=True
        suc="Successful"
    return render(request, 'user_edit.html',{'succ': suc, 'form': mform, 'title': 'Edit Details', 'user': user, 'stat': reg})



def priv_user(request):
    stat='No Appointments'
    user=request.session['user_name']
    priv=request.session['priv']
    if priv==1 or priv=='1':
        return redirect('user')
    a=[]
    b=[]
    if Appointment.objects.filter(app_status=1).exists():
        b=Appointment.objects.filter(app_status=1)
        stat='Appointments'

    if Appointment.objects.filter(app_status=2).exclude(app_date__lt=datetime.date.today()).exists():
        a=Appointment.objects.filter(app_status=2).exclude(app_date__lt=datetime.date.today())
        stat='Appointments'

    return render(request, 'priv_user.html', {'user': user, 'title': 'Priv User Home', 'form': a, 'form1':b, 'stat': stat})



def priv_edit(request):
    reg=False
    suc=""
    priv=request.session['priv']
    if priv==1 or priv=='1':
        return redirect('user_edit')
    user=request.session['user_name']
    try:
        mreg=Register.objects.get(userName=user)
        mform=Edit_form(request.POST or None,instance=mreg)
        if mform.is_valid():
            mform.save()
            reg=True
            suc="Successful"
        return render(request, 'priv_edit.html',{'succ': suc, 'form': mform, 'title': 'Edit Details', 'user': user, 'stat': reg})
    except:
        return render(request, 'priv_edit.html', {'stat': True, 'title': 'Edit Details', 'succ': suc})



def app_show(request):
    a=[]
    b={
        1: '09:00 AM',
        2: '09:20 AM',
        3: '09:40 AM',
        4: '10:00 AM',
        5: '10:20 AM',
        6: '10:40 AM',
        7: '11:00 AM',
        8: '11:20 AM',
        9: '11:40 AM',
        10: '02:00 PM',
        11: '02:20 PM',
        12: '02:40 PM',
        13: '03:00 PM',
        14: '03:20 PM',
        15: '03:40 PM',
        16: '04:00 PM',
        17: '04:20 PM',
        18: '04:40 PM',
        19: '05:00 PM',
        20: '05:30 PM' }
    user=request.session['user_name']
    priv=request.session['priv']
    if Appointment.objects.filter(app_user=user).exclude(app_date__lt=datetime.date.today()).exists():
        a=Appointment.objects.filter(app_user=user).exclude(app_date__lt=datetime.date.today())
        stat="Appointments"
    return render(request, 'apps.html',{'user': user, 'form': a, 'time_list':b})



def book_app(request):
    user=request.session['user_name']
    priv=request.session['priv']
    if priv==7 or priv=='7':
        return redirect('priv_user')
    form1=Book_app(request.POST or None)
    stat=""
    
    if form1.is_valid() and form1.cleaned_data['app_date']>=datetime.date.today():
        #form1.cleaned_data['app_user']=user
        form2=form1.cleaned_data
        if not Appoint.objects.filter(app_dat=form2['app_date']).exists():
            a=Appoint(app_dat=form2['app_date'],slots=1)
            a.save()
            b=form1.save(commit=False)
            b.app_user=user
            b.app_slot=1
            b.save()
            stat="Morning 9"
            request.session['stat']=stat
            return redirect('app_show')
            
        elif Appoint.objects.get(app_dat=form2['app_date']).slots<=20:
            a=Appoint.objects.get(app_dat=form2['app_date'])
            a.slots+=1
            a.save()
            b=form1.save(commit=False)
            b.app_user=user
            b.app_slot=a.slots
            b.save()
            stat="Successful slot"+str(a.slots)
            request.session['stat']=stat
            return redirect('app_show')
        else:
            stat="Appointments not available"
    return render(request, 'appoint.html', {'form': form1,'title': 'Book Appointment', 'stat': stat, 'user': user})



def cancel_app(request):
    user=request.session['user_name']
    priv=request.session['priv']
    if request.method=='POST':
        id1=request.POST['id']
        b12=Appointment.objects.get(id=id1)
        if request.POST['confirm']=='confirm':
            b12.app_status=1
            b12.app_doct=user
        elif request.POST['confirm']=='cancel':
            b12.app_status=0
        b12.save()
    if priv==1 or priv=='1':
        return redirect('book_app')
    elif priv==7 or priv=='7':
        return redirect('priv_user')



def logout(request):
    response=redirect("signin")
    try:
        del request.session['user_name']
    except:
        pass
    return redirect('signin')



def contact(request):
    us1=False
    user=""
    if request.session.has_key('user_name'):
        us1=True
        user=request.session['user_name']
    con={
        'title': 'Contact',
        'uss': us1,
        'user': user,
    }
    return render(request, 'contact.html',con)



def about(request):
    user=""
    us1=False
    if request.session.has_key('user_name'):
        user=request.session['user_name']
        us1=True
    con = {
        'title': 'About',
        'usss': us1,
        'user': user,
    }
    return render(request, 'about.html',con)



