from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import RegisterForm
from .models import Register

# Create your views here.
# def register(request):
#     if request.method == "POST":
#         entered_firstname = request.POST['firstname']
#         entered_lastname = request.POST['lastname']
#         # print(entered_firstname,entered_lastname )
#     return render(request,"basicForms/register.html")


# def register(request):
#     # Handling form errors manually
#     if request.method == "POST":
#         entered_firstname = request.POST['firstname']
#         entered_lastname = request.POST['lastname']
#         if entered_firstname == "":
#          return render(
#             request,
#             "basicForms/register.html",
#             {
#                 "has_error":True
#             }
#          )
        #  return HttpResponseRedirect("/form-submitted")
        
    # return HttpResponse("form submitted")
       
# def register(request):
#       # Handling forms with form class
#       form = RegisterForm()
#       return render(
#           request,
#           "basicForms/register.html",
#           {
#               "form":form,
#           }
#       )

#   view with form class       
# def register(request):
#        if request.method == "POST":
#               form = RegisterForm(request.POST)
#               if form.is_valid():
#                      return HttpResponseRedirect("/form-submitted")
#               else:
#                 #if form is not valid render this
#                 return render(
#           request,
#            "basicForms/register.html",
#            {
#                "form":form,
#            }
#      )
#        else:
#              #if method is not post render this
#              form=RegisterForm()
#              return render(
#                    request,
#                    "basicForms/register.html",
#            {
#                "form":form,
#            }

#              )
              
#   view with models  

def register(request):
       if request.method == "POST":
              form = RegisterForm(request.post)   
              if form.is_valid():
                     register=Register(
                            firstname = form.cleaned_data("firstname"),
                            lastname = form.cleaned_data("lastname"),
                     )  
                     register.save()
                     return HttpResponseRedirect("/form-submitted")   
              else:
                     return render(
                            request,
                            "basicForms/register.html",
                            {
                                   "form":form
                            }
                     ) 
       else:
              form = RegisterForm()
              return render(
                            request,
                            "basicForms/register.html",
                            {
                                   "form":form
                            }
                     ) 
              

def form_submitted(request):
       return render(request,"basicForms/form_submitted.html")
   