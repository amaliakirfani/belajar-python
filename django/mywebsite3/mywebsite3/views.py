from django.shortcuts import render

def index(request):
    context = {
        'judul':'kelas terbuka',
        'subjudul':'selamat datang',
    }
    return render(request,'index.html',context)