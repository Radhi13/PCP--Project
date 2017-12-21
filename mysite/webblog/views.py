from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm

def home_page(request):
    return render(request, 'webblog/home_page.html')

def contact(request):
    return render(request, 'webblog/contact_page.html',{'content':['If you would like to contact me, please email me.','radhika.hegde13@gmail.com']})

def feedback_form(request):
    
    form = FeedbackForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()
        print("yes it worked")
        return render(request, 'webblog/thanks.html')      
    else:
        form = FeedbackForm()
    
    context = {
        "form": form,
    }
    return render(request, 'webblog/feedback_form.html', context)