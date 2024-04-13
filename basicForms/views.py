from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import RegisterForm

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
       
def register(request):
      form = RegisterForm()
      return render(
          request,
          "basicForms/register.html",
          {
              "form":form,
          }
      )

def form_submitted(request):
       return render(request,"basicForms/form_submitted.html")
   