from django.shortcuts import render,redirect, reverse
from .models import Photo, Contact, comment
from django.contrib import messages
from .forms import post_comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    return render(request, "gallery/home.html")


def exhibitions(request):
    return render(request, 'gallery/exhibitions.html',)


def about(request):
    return render(request, 'gallery/about.html',)


def contact(request):
    if request.method == 'POST':
        forename = request.POST['forename']
        print(forename)
        surname = request.POST['surname']
        email = request.POST['email']
        message = request.POST['message']
        form = Contact(forename=forename, surname=surname, email=email,
                       message=message)
        form.save()
        messages.info(request, 'Your form has been submitted!')
        return redirect(reverse('contact'))
    return render(request, 'gallery/contact.html',)


def photos(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {"photos": photos})


# Gives the information page of image.
def photo(request, id):
    photo = Photo.objects.get(id=id)
    length = len(comment.objects.filter(
        photo=photo)) # To pass across how many comments have been made
    comments = comment.objects.filter(
        photo=photo)  # So that we only show the comments that have been made on that particular photo.
    page = request.GET.get('page')
    paginator = Paginator(comments, 4)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    form = post_comment()
    return render(request, 'gallery/photo.html',
                  {"photo": photo, "comments": comments, "length": length, "form": form, })


@login_required
def post_comments(request, id, user,):
    photo = Photo.objects.get(id=id)
    username = User.objects.get(id=user)
    if request.method == 'POST':
        content = request.POST['content']
        form = comment(user=username, content=content, photo=photo)
        form.save()
        return redirect(reverse('photo', kwargs={'id': id}))
    else:
        return redirect('/')


def delete_comment(request, id, photo_id, ):
    post = comment.objects.get(id=id)
    post.delete()
    return redirect(reverse('photo', kwargs={'id': photo_id}))


# Search bar functionality
def search(request):
    photos = Photo.objects.filter(title__icontains=request.GET['q'])
    return render(request, "gallery/gallery.html", {"photos": photos})
