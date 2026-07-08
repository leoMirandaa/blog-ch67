from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# Function Based View vs. Class Based Views

# Class Based View
class HomePageView(TemplateView): #OOP - Object Oriented Programming
    template_name = "pages/home.html"

    #Methods
    def get_context_data(self, **kwargs): # **kwargs -> keyword arguments / single variables
        context = super().get_context_data(**kwargs)
        context['name'] = "Luis"
        context['address'] = "Something 444, CA"
        context['email'] = "lrenteria@sdgku.edu"
        return context


# Function Based View
def contact_me(request):
    #return HttpResponse("Hello World from a Function Based View")
    contact_info = {
        "name":"Luis",
        "address":"Something 444, CA",
        "email":"lrenteria@sdgku.edu"
    }

    return render(request, "pages/contact.html", contact_info)
