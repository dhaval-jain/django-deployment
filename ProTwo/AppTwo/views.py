from django.shortcuts import render

from django.http import HttpResponse
from AppTwo.models import Users
from AppTwo.forms import NewuserForm
# Create your views here.

def index(request):
    return HttpResponse("Go to users to sign up")

def help(requst):
    insert_dict = {"insert": "Insert string"}
    return render(requst,'AppTwo/help.html', context=insert_dict)

def user(request):
        form = NewuserForm()

        if request.method=="POST":
             form = NewuserForm(request.POST)
             
             if form.is_valid():
                  form.save(commit=True)
                  return index(request)
             else:
                  print("ERROR invalid form")

        return render(request, 'AppTwo/users.html', {'form': form})