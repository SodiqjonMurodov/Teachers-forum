from django.shortcuts import render, redirect
from forum import forms
from forum.models import Forum


def main(request):
    user_cards = Forum.objects.all()
    return render(request, 'main.html', {'user_cards': user_cards})


def video(request, id):
    card = Forum.objects.get(id=id)
    return render(request, 'Card.html', {'card': card})


def post(request):
    form = forms.AddPost()
    if request.method == 'POST':
        form = forms.AddPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'post.html', {'form': form})
