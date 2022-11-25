from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home/Homepage_ananta.html')

def contact(request):
    # return HttpResponse("This is home contact")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')



def signup(request):
    if request.method=="POST":
        # get post parameters
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname =request.POST['lastname']
        email =request.POST['email']
        phone = request.POST['phone']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']
        age =request.POST['age']
        insured_sex = request.POST['insured_sex']
        address1 =request.POST['address1']
        address2 =request.POST['address2']
        city =request.POST['city']
        state =request.POST['state']
        pincode =request.POST['pincode']
        pan =request.POST['pan']
        aadhar =request.POST['aadhar']
        policyno =request.POST['policyno']
        premium =request.POST['premium']
        brand =request.POST['brand']
        caryear =request.POST['caryear']
        registrationno =request.POST['registrationno']
        chassisno =request.POST['chassisno']


        # create user 
        Myuser = User.objects.create_user(username, email, pass1)
        Myuser.first_name = firstname
        Myuser.last_name = lastname
        Myuser.save()
        # print(Myuser)
        print(insured_sex)
        u = User.objects.get(username=username)
        uid = u.pk
        UserProfile = Profile(uid, phone, age, insured_sex, address1, address2, city, state, pincode, pan, aadhar, policyno, premium, brand, caryear, registrationno, chassisno)
        UserProfile.save()

    return render(request, "home/signup.html")



# def createProfile(request, username):
#     myuser = User.objects.get(pk=username)

def handleLogin(request):
    if request.method=="POST":
        loginemail=request.POST['loginemail']
        loginpass=request.POST['loginpass']
        user = authenticate(username=loginemail, password=loginpass)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "home/login.html")
    return render(request, "home/login.html")

def handlelogout(request):
    logout(request)
    print("LOGGED OUT SUCCESSFULLY")
    return redirect("home")
