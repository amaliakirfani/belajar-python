from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'About',
        'subjudul':'everything about you',
    }
    return render(request,'about/index.html', context)