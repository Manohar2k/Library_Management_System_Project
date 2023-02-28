from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import forms
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache
from LMSApp.models import Course, Student, Book, Issue_Book
from django.contrib.auth.decorators import login_required

# Create your views here.

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def home_fun(request):
    return render(request, 'home.html', {'msg': ''})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def adminreg_fun(request):
    return render(request, 'adminreg.html', {'msg': ''})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def adminregread_fun(request):
    User_Name = request.POST['uname']
    Email_id = request.POST['uemail']
    Password = request.POST['upswd']
    if User.objects.filter(Q(username=User_Name) | Q(email=Email_id)).exists():
        return render(request, 'adminreg.html', {'msg': 'User Name or Email already exists'})
    else:
        u1 = User.objects.create_superuser(username=User_Name,email=Email_id,password=Password)
        u1.save()
        return render(request, 'home.html', {'msg': 'Admin Account Created Successfully'})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def adminhome_fun(request):
    return render(request, 'adminhome.html', {'aname': request.session['aname']})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def studreg_fun(request):
    c1 = Course.objects.all()
    sems = list(range(1,9))
    return render(request, 'studreg.html', {'data': c1, 'sems': sems, 'msg': ''})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def studreread_fun(request):
    Stud_Name = request.POST['sname']
    Stud_Phn_No = request.POST['sphnno']
    Stud_Course = request.POST['scourse']
    Stud_Sem = request.POST['ssem']
    Stud_Password = request.POST['spswd']
    c1 = Course.objects.all()
    sems = list(range(1,9))
    if Student.objects.filter(Stud_Name=Stud_Name).exists():
        return render(request, 'studreg.html', {'msg': 'Student Account already Exists', 'data': c1, 'sems': sems})
    else:
        s1 = Student()
        s1.Stud_Name = Stud_Name
        s1.Stud_Phn_No = Stud_Phn_No
        s1.Stud_Course = Course.objects.get(Course_Name=Stud_Course)
        s1.Stud_Sem = Stud_Sem
        s1.Stud_Password = Stud_Password
        s1.save()
        return render(request, 'home.html', {'msg': 'Student Account Created Successfully'})


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def readlog_fun(request):
    User_Name = request.POST['uname']
    Password = request.POST['upswd']
    u1 = authenticate(username=User_Name, password=Password)
    if u1 is not None:
        if u1.is_superuser:
            request.session['aname'] = User_Name
            return render(request, 'adminhome.html', {'aname': request.session['aname']})
        else:
            return render(request, 'home.html', {'msg': 'User is not a SuperUser'})
    elif Student.objects.filter(Q(Stud_Name=User_Name) & Q(Stud_Password=Password)).exists():
        request.session['sname'] = User_Name
        log_stud = Student.objects.get(Stud_Name=User_Name)
        log_stud.is_logged_in = 'Yes'
        log_stud.save()
        return render(request, 'shome.html', {'sname': request.session['sname']})
    elif Student.objects.filter(Q(Stud_Name=User_Name)).exists() | User.objects.filter(Q(username=User_Name)).exists():
        return render(request, 'home.html', {'msg': 'Wrong Password'})
    else:
        return render(request, 'home.html', {'msg': 'Account does not Exist'})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def resetpswd_fun(request):
    if request.method == 'POST':
        Admin_Status = request.POST['admin?']
        User_Name = request.POST['name']
        Password = request.POST['pswd']
        if Admin_Status == 'Yes':
            if User.objects.filter(username=User_Name).exists():
                u1 = User.objects.get(username=User_Name)
                Email = u1.email
                u1.delete()
                u1 = User.objects.create_superuser(username=User_Name, email=Email, password=Password)
                u1.save()
                return render(request, 'home.html', {'msg': 'Password Reset Successful'})
            else:
                return render(request, 'resetpswd.html', {'msg': 'Please Enter Proper Details'})
        elif Admin_Status == 'No':
            if Student.objects.filter(Stud_Name=User_Name).exists():
                s1 = Student.objects.get(Stud_Name=User_Name)
                s1.Stud_Password = Password
                s1.save()
                return render(request, 'home.html', {'msg': 'Password Reset Successful'})
            else:
                return render(request, 'resetpswd.html', {'msg': 'Please Enter Proper Details'})
    return render(request, 'resetpswd.html', {'msg': ''})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def addbook_fun(request):
    course = Course.objects.all()
    return render(request, 'addbook.html', {'data': course, 'msg': ''})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def readbook_fun(request):
    Book_Name = request.POST['bookname']
    Author_Name = request.POST['authname']
    Course_id = Course.objects.get(Course_Name = request.POST['ddlcourse'])
    if Book.objects.filter(Q(Book_Name=Book_Name) & Q(Author_Name=Author_Name)).exists():
        return render(request, 'addbook.html', {'msg': 'Book by that Author Already Exists'})
    else:
        b1=Book()
        b1.Book_Name=Book_Name
        b1.Author_Name=Author_Name
        b1.Course_id=Course_id
        b1.save()
        course = Course.objects.all()
        return render(request, 'addbook.html', {'msg': 'Book Added Successfully', 'data': course})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def displaybook_fun(request):
    b1 = Book.objects.all()
    return render(request, 'displaybook.html', {'msg': '', 'data': b1})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def update_book(request, id):
    b1 = Book.objects.get(id=id)
    c = Course.objects.all()
    if request.method == 'POST':
        b1.Book_Name = request.POST['bookname']
        b1.Author_Name = request.POST['authname']
        b1.Course_id = Course.objects.get(Course_Name = request.POST['ddlcourse'])
        b1.save()
        b1 = Book.objects.all()
        return render(request, 'displaybook.html', {'msg': 'Book Updated Successfully', 'data': b1})
    return render(request, 'updatebook.html', {'data': b1, 'course': c})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def delete_book(request, id):
    b1= Book.objects.get(id=id)
    b1.delete()
    b1 = Book.objects.all()
    return render(request, 'displaybook.html', {'msg': 'Book Deleted Successfully', 'data': b1})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def issuebook_fun(request):
    c1 = Course.objects.all()
    sems = list(range(1,9))
    if request.method == 'POST':
        Student_Course = request.POST['ddlcourse']
        Student_Sem = request.POST['ddlsem']
        # sc = Course.objects.get(Course_Name = Student_Course)
        # ss = Student.objects.get(Stud_Sem = Student_Sem)
        books = Book.objects.filter(Course_id=Course.objects.get(Course_Name=Student_Course))
        students = Student.objects.filter(Q(Stud_Course=Course.objects.get(Course_Name=Student_Course)) & Q(Stud_Sem=Student_Sem))
        if students.exists() & books.exists():
            return render(request, 'issuebook.html', {'msg': '', 'students': students, 'books': books})
        elif students.exists():
            return render(request, 'issuebook.html', {'msg': 'No Books in that Course', 'courses': c1, 'sems': sems})
        elif books.exists():
            return render(request, 'issuebook.html', {'msg': 'No Students in that Course and Sem', 'courses': c1, 'sems': sems})
        else:
            return render(request, 'issuebook.html', {'msg': 'No Students and Books in that Sem and Course', 'courses': c1, 'sems': sems})
    return render(request, 'issuebook.html', {'msg': '', 'courses': c1, 'sems': sems})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def savebook_fun(request):
    ib1 = Issue_Book()
    ib1.Stud_Name = Student.objects.get(Stud_Name=request.POST['ddlsname'])
    ib1.Book_Name = Book.objects.get(Book_Name=request.POST['ddlbook'])
    ib1.Start_Date = request.POST['sdate']
    ib1.End_Date = request.POST['edate']
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("Start_Date")
        end_date = cleaned_data.get("End_Date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than Start date.")
        else:
            ib1.save()
    c1 = Course.objects.all()
    sems = list(range(1,9))
    return render(request, 'issuebook.html', {'msg': 'Book Issued Successfully'})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def booksissued_fun(request):
    ib1 = Issue_Book.objects.all()
    return render(request, 'booksissued.html', {'list': ib1, 'msg': ''})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def updatebookissue_fun(request, id):
    ib1 = Issue_Book.objects.get(id=id)
    if request.method == 'POST':
        ib1.Stud_Name = Student.objects.get(Stud_Name=request.POST['sname'])
        ib1.Book_Name = Book.objects.get(Book_Name=request.POST['bookname'])
        ib1.Start_Date = request.POST['sdate']
        ib1.End_Date = request.POST['edate']
        ib1.save()
        ib1 = Issue_Book.objects.all()
        return render(request, 'booksissued.html', {'msg': 'Updated Successfully', 'list': ib1})
    br = Book.objects.get(Book_Name=ib1.Book_Name)
    b1 = Book.objects.filter(Course_id=br.Course_id)
    sr = Student.objects.get(Stud_Name=ib1.Stud_Name)
    s1 = Student.objects.filter(Q(Stud_Sem=sr.Stud_Sem) & Q(Stud_Course=sr.Stud_Course))
    return render(request, 'updatebookissue.html', {'books': b1, 'students': s1, 'data': ib1})

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def deletebookissue_fun(request, id):
    ib1 = Issue_Book.objects.get(id=id)
    ib1.delete()
    ib1 = Issue_Book.objects.all()
    return render(request, 'booksissued.html', {'list': ib1, 'msg': 'Deleted Successfully'})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def admin_log_out_fun(request):
    return redirect('home')

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def shome_fun(request):
    return render(request, 'shome.html', {'sname': request.session['sname']})

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def s_log_out_fun(request):
    for i in Student.objects.all():
        if i.is_logged_in == 'Yes':
            i.is_logged_in = 'No'
            i.save()
    return redirect('home')

@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def sbooks_fun(request):
    Stud_Name = Student.objects.get(Stud_Name=request.session['sname'])
    print(Stud_Name)
    ib1 = Issue_Book.objects.filter(Stud_Name = Student.objects.get(Stud_Name=request.session['sname']))
    print(ib1)
    return render(request, 'sbooks.html', {'student': ib1})
