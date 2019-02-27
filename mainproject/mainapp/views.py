from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration, Client
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
