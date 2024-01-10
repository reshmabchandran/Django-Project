from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from . import models
from .models import TenantDetails, PropertyDetails,UnitDetails,RentDetails


# Create your views here.


def index(request):
    return render(request,'index.html')


def login_page(request):
    return render(request,'login.html')


def register_page(request):
    return render(request,'register.html')


def admin_home(request):
    data=RentDetails.objects.all()
    return render(request,'admin_home.html',{'data':data})


def tenant_home(request):
    data=PropertyDetails.objects.all()
    return render(request,'tenant_home.html',{'data':data})






def tenantregister(request):
    if request.method == 'POST' and request.FILES:

        fname = request.POST.get('fname')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        proof = request.FILES['proof']
        cpassword = password
        role='tenant'
        status="0"
        


        if password==cpassword:
            if User.objects.filter(username=email).exists():
                messages.info(request,"Username Taken")
                return redirect('register_page')

            
            else:
                user=User.objects.create_user(username=email,password=password)
                user.save()
                print(user)
                
                tenantDetail = models.TenantDetails(user=user, fname=fname, address=address, mobile=mobile, email=email, password=password, proof=proof, role=role,status=status)
                tenantDetail.save()
                print(tenantDetail)


                print('user created')
        else:
            messages.info(request,"Password is not matching")
            return redirect('register_page')
        
        return redirect('login_page')
    else:
        return render(request, 'register.html')




def userlogin(request):
    role=''
    stat=''
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')



        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            u_name = i['username']
            id=i['id']

            d=TenantDetails.objects.filter(user_id=id).values()
            print("userdata==>",d)
            for i in d:
                stat=i['status']
                role=i['role']

            
            user = authenticate(username=username,password=password)

            if user is not None and role=="tenant" and username==u_name and stat=="0":
                auth_login(request,user)
                return redirect('tenant_home')
            
            elif  username=="admin@gmail.com" and password=="admin":
                return redirect('admin_home')
            else:pass

    
    
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login_page')

    else:
        return render(request, 'login.html')



def add_property_page(request):
    return render(request,'add_property.html')



def admin_add_property(request):
    if request.method == 'POST' and request.FILES:

        pname = request.POST.get('pname')
        address = request.POST.get('address')
        locaton = request.POST.get('locaton')
        features = request.POST.get('features')
        image = request.FILES['image']
        status = '0'

        
        propertyDetails = models.PropertyDetails(pname=pname, address=address,locaton=locaton, features=features,image = image , status=status)
        propertyDetails.save()


        print('Property Added')
        return redirect('admin_view_property')

    else:
        return render(request,'add_property.html')   



def admin_view_property(request):
    data=PropertyDetails.objects.all()
    return render(request,'admin_view_property.html',{'data':data})


def admin_add_unit_page(request,id):
    data=PropertyDetails.objects.get(id=id)
    return render(request,'admin_add_unit.html',{'data':data})


def admin_add_unit(request,pid):
    if request.method == 'POST':

        pname = request.POST.get('pname')
        uname = request.POST.get('uname')
        rent_cost = request.POST.get('rent_cost')
        types = request.POST.get('type')
        status = '0'

        property_instance = PropertyDetails.objects.get(id=pid)


        unitDetails = models.UnitDetails(properti=property_instance,pname=pname, uname=uname,rent_cost=rent_cost, types=types, status=status)
        unitDetails.save()


        print('Unit Added')
        return redirect('admin_view_property')

    else:
        return render(request,'add_property.html') 


def admin_view_unit(request,id):
    data=UnitDetails.objects.filter(properti=id).values()
    return render(request,'admin_view_unit.html',{'data':data})


def tenant_view_more(request,id):
    data=UnitDetails.objects.filter(properti=id).values()
    prop_data=PropertyDetails.objects.filter(id=id).values()
    return render(request,'tenant_view_more.html',{'data':data,'prop_data':prop_data})


def tenant_getnow_page(request,id):
    prop_data=UnitDetails.objects.get(id=id)
    return render(request,'tenant_getnow_page.html',{'data':prop_data})



def tenant_add_rentdetails(request,uid):
    if request.user:
        user=request.user
        da=TenantDetails.objects.filter(user=user).values()
        for i in da:
            fname=i['fname']
            address=i['address']
            mobile=i['mobile']

        if request.method == 'POST':

            # pid = request.POST.get('pid')
            pname = request.POST.get('pname')
            uname = request.POST.get('uname')
            rent_cost = request.POST.get('rent_cost')
            types = request.POST.get('types')
            enddate = request.POST.get('enddate')
            rentdate = request.POST.get('rentdate')
            status = '0'

            unit_instance = UnitDetails.objects.get(id=uid)
            pid=unit_instance.properti


            prop_instance = PropertyDetails.objects.get(pname=pid)



            dta=PropertyDetails.objects.filter(pname=prop_instance).values()
            for i in dta:
                paddress=i['address']
                locaton=i['locaton']
                features=i['features']


            rentDetails = models.RentDetails(user=user,fname=fname,address=address,mobile=mobile,properti=prop_instance,pname=pname,paddress=paddress,locaton=locaton,features=features,unit=unit_instance, uname=uname,rent_cost=rent_cost, types=types,enddate=enddate,rentdate=rentdate, status=status)
            rentDetails.save()


            print('Rent Details Added')
            return redirect('tenant_home')

        else:
            return render(request,'tenant_getnow_page.html') 
    
    else:
            return render(request,'tenant_getnow_page.html') 


def tenant_profile(request):
    if request.user:
        user=request.user
        prop_data=RentDetails.objects.get(user=user)
        return render(request,'tenant_profile.html',{'data':prop_data})
