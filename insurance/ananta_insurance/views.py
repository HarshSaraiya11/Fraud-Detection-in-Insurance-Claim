from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from  home.models import Profile

@login_required(login_url='/login')
def claim_form(request):
    current_user = request.user
    userid = current_user.id
    fname= current_user.first_name
    lname= current_user.last_name
    details = Profile.objects.filter(user_id=userid).values()
    details_dict = details[0]
    details_dict.update({'fname': fname, 'lname': lname})
    # print(details_dict)

    if request.method == "POST":
        # Details about the driver
        fullname = request.POST['fullname']
        driver_is = request.POST['driver_is']
        phone = request.POST['phone']
        dlnumber = request.POST['dlnumber']

        # details of accident
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        stt = request.POST['stt']
        city = request.POST['city']
        accident_type = request.POST['accident_type']
        collision_type = request.POST['collision_type']
        severity = request.POST['severity']
        damage_material = request.POST['damage_material']
        auth_contacted = request.POST['auth_contacted']
        police_report = request.POST['police_report']
        fir = request.POST['fir']
        third_party_resp = request.POST['third_party_resp']
        noofvehicle = request.POST['noofvehicle']
        noofpeople = request.POST['noofpeople']
        description = request.POST['description']

        # print(driver_is)
        # print(date)
        claim = [fullname, driver_is, phone, dlnumber, date, time, location, stt, city, accident_type, collision_type, severity, damage_material, auth_contacted, police_report, fir, third_party_resp, noofvehicle, noofpeople, description]
        print(claim)
        

        # saving the above details in database (pending)
        
        return render(request, 'ananta_insurance/success.html', context= claim)
    return render(request, 'ananta_insurance/claimform.html', context= details_dict)
    # return HttpResponse("this is ananta insurance claimform")

def success(request):
    
    return render(request, 'ananta_insurance/success.html')