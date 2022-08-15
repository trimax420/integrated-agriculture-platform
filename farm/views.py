from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login
from .forms import loginForm,registrationForm,farmerForm,research_agroForm,drone_operatorForm,kvkForm,warehouseForm,registrationForm
from .models import login
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if login.objects.filter(userid=username).exists() and login.objects.filter(password).exists():
                return HttpResponse('sucessful')
            else:
                return HttpResponse('error')

            
    else:
        return render(request,'login.html')
    

def register(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            adhaar_number = form.cleaned_data['adhaar_number']
            request.session['adhaar_number'] = adhaar_number
            request.session['role'] = role

            form.save()
            return redirect(role_registrations)
           
    else:
        form = registrationForm()
    return render(request,'register.html',{'form':form})

def role_registrations(request):
    role = request.session['role']
    adhaar_number = request.session['adhaar_number']
    if role == 'Farmer':
               if request.method == 'POST':
                   form_role = farmerForm(request.POST)
                   form_role.save()
                   return HttpResponse('sucessful')
               else:
                   form_role = farmerForm()
               return render(request,'register.html',{'form':form_role})
           
    elif role == 'Researcher' or role == 'Agro-scientist':
        if request.method == 'POST':
            form_role = research_agroForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = research_agroForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'Drone Operator' :
        if request.method == 'POST':
            form_role = drone_operatorForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = drone_operatorForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'KVK':
        if request.method == 'POST':
            form_role = kvkForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = kvkForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'Warehouse' or role == 'Food Processor' or role == 'Distributer' or role == 'Retailer':
        if request.method == 'POST':
            form_role = warehouseForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = warehouseForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'Others':
        if request.method == 'POST':
            form_role = farmerForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = farmerForm()
        return render(request,'register.html',{'form':form_role})