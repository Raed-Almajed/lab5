from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

people = []

class account:
    def __init__(self, name, password):
        self.username = name
        self.password = password

    def __str__(self):
        return self.username

class NewAccountForm(forms.Form):
    name = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)    

# Create your views here.
def index(request):      
    return render(request, "accounts/index.html", {
        "people": people
    })

def add(request):
    if request.method == "POST":
        form = NewAccountForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            person = account(name,password)
            people.append(person)
            return HttpResponseRedirect(reverse("accounts:index"))
        else:
            return render(request, "accounts/add.html",{
                "form": form
            })
    else:
        return render(request, "accounts/add.html",{
            "form": NewAccountForm()
        })
