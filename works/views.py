from django.shortcuts import render

# Create your views here.


def worklistview(request):
    return render(request, 'worklist.html', {'somedata': 100})
