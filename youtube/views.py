from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'personal/home.html')
def search(request):
    return render(request,'personal/search.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cc=form.cleaned_data
            field=cc['your_name']
            x=request.POST['love']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(x)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'personal/name.html', {'form': form})