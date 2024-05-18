from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hey i am django functions")

# def success_page(request):
#     return HttpResponse("Hey this is and sucess page django functions")


def home(request):
    people = [
        {
            'name':"chiran thapa ",
            'age':12,
            "test":23
        },
           {
            'name':"Alex parsard",
            'age':23,
            "test":15
        },
           {
            'name':"parsard resta",
            'age':34,
            "test":33
        }
    ]
    return render(request ,"index.html",context={"page":'home',"peoples":people})




def contact(request):
    context = {'page':'contact'}
    print("this")
    return render(request,"contact.html",context)

def about(request):
    context = {'page':'about'}
    return render(request,"about.html",context)


def success_page(request):
    return HttpResponse("Hey this is and sucess page django functions")
