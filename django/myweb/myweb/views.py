from django.shortcuts import render

def index(request):
    context = {
        'judul':'Opened Class',
        'subjudul':'Welcome !!',
    }
    return render(request,'index.html', context)