# views blog
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul':'Blog',
        'subjudul' : 'blog untuk kelas terbuka',
    }
    return render(request,'blog/index.html', context)
