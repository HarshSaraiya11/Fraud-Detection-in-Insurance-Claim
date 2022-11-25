from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from  home.models import Profile
# from insurance.ananta_insurance.harsh import getpredictions
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


standard_to = StandardScaler()
model = pickle.load(open('./savedmodels/modelfinal.pkl', 'rb'))
def getpredictions(month_as_customer, age, policy_csl, policy_deductable, policy_annual_premium, umbrella_limit, insured_sex, incident_type, collision_type, incident_severity, authorities_contacted,incident_hour_of_the_day, number_of_vehicles_involved, property_damage, bodily_injuries,witnesses, police_report_available, total_claim_amount, injury_claim, property_claim, vehicle_claim, auto_make):
    features = np.array([[month_as_customer, age, policy_csl, policy_deductable, policy_annual_premium, umbrella_limit, insured_sex, incident_type, collision_type, incident_severity, authorities_contacted, incident_hour_of_the_day, number_of_vehicles_involved, property_damage, bodily_injuries, witnesses, police_report_available, total_claim_amount,injury_claim, property_claim, vehicle_claim, auto_make]])
    prediction = model.predict(features)
    if prediction == 0:
        return "Not a fraudulent claim."
    elif prediction == 1:
        return "Fraudulent claim analyzed."
    else:
        return "error"
# --------------------------------------------------------

@login_required(login_url='/login')
def claim_form(request):
    current_user = request.user
    userid = current_user.id
    fname= current_user.first_name
    lname= current_user.last_name
    details = Profile.objects.filter(user_id=userid).values()
    details_dict = details[0]
    gender = details_dict.get('insured_sex')

    # changing value of sex from 0,1 to male female to print on claimform
    if (gender==1):
        details_dict.update({'insured_sex': "Male"})
    elif(gender==0):
        details_dict.update({'insured_sex': "Female"})

    # changing brand value from 0,1,2... to brand names, to print on claimform
    car_brand = details_dict.get('brand')
    if(car_brand == '0'):
        details_dict.update({'brand': "Audi"})
    elif(car_brand == '1'):
        details_dict.update({'brand': "BMW"})
    elif(car_brand == '2'):
        details_dict.update({'brand': "Chevrolet"})
    elif(car_brand == '3'):
        details_dict.update({'brand': "Ford"})
    elif(car_brand == '4'):
        details_dict.update({'brand': "Honda"})
    elif(car_brand == '5'):
        details_dict.update({'brand': "Hyundai"})
    elif(car_brand == '6'):
        details_dict.update({'brand': "Jeep"})
    elif(car_brand == '7'):
        details_dict.update({'brand': "Mahindra"})
    elif(car_brand == '8'):
        details_dict.update({'brand': "Mercedes"})
    elif(car_brand == '9'):
        details_dict.update({'brand': "Nissan"})
    elif(car_brand == '10'):
        details_dict.update({'brand': "Skoda"})
    elif(car_brand == '11'):
        details_dict.update({'brand': "Tata"})
    elif(car_brand == '12'):
        details_dict.update({'brand': "Toyoto"})
    elif(car_brand == '13'):
        details_dict.update({'brand': "Volkswag"})
    
    auto_make = int(car_brand)
    details_dict.update({'fname': fname, 'lname': lname})
    age = int(details_dict.get('age'))
    annual_premium = float(details_dict.get('premium'))
    
    if request.method == "POST":
        # policy information
        policy_period = int(request.POST['policy_period'])
        policy_csl = int(request.POST['policy_csl'])
        policy_deductible = int(request.POST['policy_deductible'])
        umbrella_limit = int(request.POST['umbrella_limit'])

        # Details about the driver
        fullname = request.POST['fullname']
        driver_is = request.POST['driver_is']
        phone = request.POST['phone']
        dlnumber = request.POST['dlnumber']

        # details of accident
        date = request.POST['date']
        time = int(request.POST['time'])
        location = request.POST['location']
        stt = request.POST['stt']
        city = request.POST['city']
        accident_type = int(request.POST['accident_type'])
        collision_type = int(request.POST['collision_type'])
        severity = int(request.POST['severity'])
        damage_material = request.POST['damage_material']
        auth_contacted = int(request.POST['auth_contacted'])
        police_report = int(request.POST['police_report'])
        fir = request.POST['fir']
        third_party_resp = request.POST['third_party_resp']
        noofvehicle = int(request.POST['noofvehicle'])
        noofpeople = int(request.POST['noofpeople'])
        property_damage = int(request.POST['property_damage'])
        people_injured = int(request.POST['people_injured'])
        no_of_witnesses = int(request.POST['no_of_witnesses'])
        injury_claim = int(request.POST['injury_claim'])
        property_claim = int(request.POST['property_claim'])
        vehicle_claim = int(request.POST['vehicle_claim'])
        total_claim = int(request.POST['total_claim'])
        description = request.POST['description']

    
        claim = [ policy_period, policy_csl, policy_deductible, umbrella_limit, fullname, driver_is, phone, dlnumber, date, time, location, stt, city, accident_type, collision_type, severity, damage_material, auth_contacted, police_report, fir, third_party_resp, noofvehicle, noofpeople, property_damage, people_injured, no_of_witnesses, injury_claim, property_claim, vehicle_claim, total_claim, description]
        print(claim)

        result = getpredictions(policy_period, age, policy_csl, policy_deductible, annual_premium, umbrella_limit, gender, accident_type, collision_type, severity, auth_contacted, time, noofvehicle, property_damage, people_injured, no_of_witnesses, police_report, total_claim, injury_claim, property_claim, vehicle_claim, auto_make)

        context = {
            'result': result
        }
        # saving the above details in database (pending)

        return render(request, 'ananta_insurance/success.html', context= context)
    return render(request, 'ananta_insurance/claimform.html', context= details_dict)
    # return HttpResponse("this is ananta insurance claimform")

def success(request):
    
    return render(request, 'ananta_insurance/success.html')