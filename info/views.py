from django.shortcuts import render

# Create your views here.


def aboutview(request):
    context = {
    }
    return render(request, 'info/about.html', context)


def contactview(request):
    context = {
    }
    return render(request, 'info/contact.html', context)
