from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from libraryapp.models import Student, Course, Book, Issue_book


# Create your views here.
def login_fun(request):
    return render(request,'login.html')


def readlog_fun(request):
    name=request.POST['tbname']
    password=request.POST['tbpwd']
    request.session['n'] = name
    user=authenticate(username=name,password=password)
    if user is not None:
        if user.is_superuser:
            return render(request,'adminhome.html')
        else:
            return render(request,'login.html',{'data':'user is not super user'})
    elif Student.objects.filter(Q(s_name=name) | Q(s_password=password)).exists():
        request.session['n']=name
        return render(request,'stdhome.html',{'data':name})
    else:
        return render(request,'login.html',{'data':'wrong username and password'})


def adminreg_fun(request):
    return render(request,'adminreg.html')


def adminread_fun(request):
    name=request.POST['adname']
    email=request.POST['ademail']
    pas=request.POST['adpas']
    if User.objects.filter(Q(username=name) | Q(email=email)).exists():
        return render(request,'adminreg.html',{'data':'username and email is alreday exists'})
    else:
        d=User.objects.create_superuser(username=name,email=email,password=pas)
        d.save()
        return redirect('login')


def stdregread_fun(request):
    d = Course.objects.all()
    return render(request, 'studentreg.html', {'data': '', 'data':d})


def stdread_fun(request):
    xname = request.POST['stname']
    xphone = request.POST['stph']
    c1 = Course.objects.all()
    if Student.objects.filter(Q(s_phone=xphone) | Q(s_name=xname)).exists():
        return render(request, 'studentreg.html', {'data1': 'username and email is alreday exists', 'data': c1})
    else:
        s = Student()
        s.s_name = request.POST['stname']
        s.s_phone = request.POST['stph']
        s.s_password = request.POST['stpass']
        s.s_semester = request.POST['stsem']
        s.s_course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
        s.save()
        return redirect('login')

def addbk_fun(request):
    c=Course.objects.all()
    return render(request,'addbook.html',{'data':c})


def readbook_fun(request):
    c=Book()
    c.b_name=request.POST['bkname']
    c.a_name=request.POST['atname']
    c.course_id=Course.objects.get(course_name=request.POST['ddlcourse'])
    c.save()
    return redirect('addbk')


def display_fun(request):
    s=Book.objects.all()
    return render(request,'display.html',{'data':s})


def update_fun(request,id):
    s = Book.objects.get(id=id)
    c = Course.objects.all()
    if request.method == 'POST':
        s.b_name = request.POST['bkname']
        s.a_name = request.POST['atname']
        s.course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
        s.save()
        return redirect('dis')
    return render(request,'update.html', {'data': s, 'datac': c})


def delete_fun(request,id):
    c=Book.objects.get(id=id)
    c.delete()
    return redirect('dis')


def log_out_fun(request):
    return redirect('log_out')


def assign_fun(request):
    c=Course.objects.all()
    return render(request,'assignbook.html',{'data':c,'data1':'','data2':''})


def readassign_fun(request):
    name=Student.objects.filter(Q(s_semester=request.POST['stsem'])
                                | Q(s_course_id=Course.objects.get(course_name=request.POST['crs'])))
    B=Book.objects.filter(course_id=Course.objects.get(course_name=request.POST['crs']))
    return render(request,'assignbook.html',{'data2':name,'data1':B,'data':''})


def issuebk_fun(request):
    c=Issue_book.objects.all()
    return render(request,'displayissuebook.html',{'data':c})


def delete1_fun(request,id):
    f=Issue_book.objects.get(id=id)
    f.delete()
    return redirect('issuebk')


def update2_fun(request,id):
    i1=Issue_book.objects.get(id=id)
    s=Student.objects.all()
    b=Book.objects.all()
    if request.method == 'POST' :
        i1.std_name=Student.objects.get(s_name=request.POST['stname'])
        i1.bk_name = Book.objects.get(b_name=request.POST['bkname'])
        i1.i_date = request.POST['st_date']
        i1.e_date = request.POST['end_date']
        i1.save()
        return redirect('issuebk')
    return render(request,'update2.html',{'data1':i1,'s':s,"b":b})


def call_fun(request):
    s=Issue_book.objects.filter(std_name=Student.objects.get(s_name=request.session['n']))
    return render(request,'studentissuebook.html',{'data':s})


def stdhome_fun(request):
    return render(request,'stdhome.html')


def assinred(request):
     i=Issue_book()
     i.std_name=Student.objects.get(s_name=request.POST['stname'])
     i.bk_name = Book.objects.get(b_name=request.POST['bkname'])
     i.i_date=request.POST['st_date']
     i.e_date=request.POST['end_date']
     i.save()
     return redirect('assign')


def profile_fun(request):
    s=Student.objects.get(s_name=request.session['n'])
    return render(request,'profile.html',{'data':s})


def profupdate_fun(request):
    k=Student.objects.get(s_name=request.session['n'])
    return render(request,'profileupdate.html',{'data':k})


def updatepro_fun(request):
    v=Student.objects.get(s_name=request.session['n'])
    v.s_name=request.POST['name']
    v.s_phone=request.POST['phone']
    v.s_password=request.POST['pass']
    v.s_semester=request.POST['sem']
    v.save()
    return redirect('prof')