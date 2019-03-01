from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration, Client, Registrationform
from django.template import loader

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
           print("form is valid")

           user = Client.objects.create(
            first_name= form.cleaned_data['first_name'],
            last_name= form.cleaned_data['last_name'],
            contact_number= form.cleaned_data['contact_number'])
        data = {
        "users" : user
        }   
        form_page = loader.get_template('mainapp/form.html')
        return HttpResponse(form_page.render(data))
        # form = Registration({
        #   "first_name": user.first_name,
        #   "last_name": user.last_name,
        #   "contact_number": user.contact_number
        #   })
     
          
    else:
       	form = Registration()
			
 
    return render(request, 'mainapp/reg.html', {'form': form})


def list(request):
  print(request.user.is_authenticated)
  list_page = loader.get_template('mainapp/list.html')
  data = {
  "users": Client.objects.all()
  }
  return HttpResponse(list_page.render(data))

def client_details(request, client_id):
  client_page = loader.get_template('mainapp/client-details.html')
  client = Client.objects.get(id=client_id)
  data = {
  "client": client
  }
  return HttpResponse(client_page.render(data))


def update(request, client_id):
  client = Client.objects.get(id=client_id)
  if request.method == 'POST':
        form = Registrationform(request.POST, instance=client)
        if form.is_valid():
           print(client_id,"form is updated", form.changed_data)
           form.save()
           return redirect('/customer/list')

 
    

  else:
    
    form = Registrationform(instance=client)
  return render(request, 'mainapp/update.html', {'form': form})