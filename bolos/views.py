from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from bolos.models import Bolo




def post_list(request):
    posts=Bolo.objects.all()
    return render(request, 'bolos/post_list.html',  {'posts': posts})

def post_detail(request, aniversario):
    post = get_object_or_404(Bolo, aniversario=aniversario)
    return render(request, 'bolos/post_detail.html', {'post': post})

