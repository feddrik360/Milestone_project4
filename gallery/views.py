from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Photo
from blog.models import comment
from django.contrib import messages
from .forms import post_comment
from django.contrib.auth.models import User


def home(request):
    return render(request, "gallery/home.html")


def exhibitions(request):
    return render(request, 'gallery/exhibitions.html', )


def about(request):
    return render(request, 'gallery/about.html.', )


def contact(request):
    return render(request, 'gallery/contact.html.', )


def photos(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {"photos": photos})


# Gives the information page of image.
def photo(request, id):
    photo = Photo.objects.get(id=id)
    comments = comment.objects.filter(
        photo=photo)  # So that we only show the comments that have been made on that particular photo.
    length = len(comments)  # so that the user can knows how many comments have been made.
    form = post_comment()
    return render(request, 'gallery/photo.html',
                  {"photo": photo, "comments": comments, "length": length, "form": form, })


def post_comments(request, id, user, ):
    photo = Photo.objects.get(id=id)
    username = User.objects.get(id=user)
    if request.method == 'POST':
        content = request.POST['content']
        form = comment(user=username, content=content, photo=photo)
        form.save()
        comments = comment.objects.filter(photo=photo)
        length = len(comments)
        return render(request, "gallery/photo.html", {"photo": photo, "comments": comments, "length": length})
    else:
        return redirect('/')


def delete_comment(request, id, photo_id,):
    post = comment.objects.get(id=id)
    post.delete()
    photo = Photo.objects.get(id=photo_id)
    comments = comment.objects.filter(photo=photo)
    lengths = len(comments)
    print(lengths)
    return render(request, "gallery/photo.html", {"photo": photo, "comments": comments, "length": lengths})


# Search bar functionality
def search(request):
    photos = Photo.objects.filter(title__icontains=request.GET['q'])
    return render(request, "gallery/gallery.html", {"photos": photos})