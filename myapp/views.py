from django.shortcuts import render
import random
from django.views.decorators.csrf import csrf_exempt
from .models import Singer, Concert, FavoriteConcert, Photo
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    # return HttpResponse('Hello from Python!')
    all_fav = FavoriteConcert.objects.all()
    all_photos = Photo.objects.all()
    all_concerts = Concert.objects.all()
    recent_concerts = []
    for c in all_concerts:
        if c.was_baught_recently():
            recent_concerts.append(c)
    r = random.randint(0, len(all_concerts) - 1)
    recommend = all_concerts[r]
    hot_concerts = all_concerts.order_by('-votes')[:3]
    return render(request, "index.html", locals())


def search(request):
    if request.method == 'POST':
        search = request.POST.get("search")
        if Concert.objects.filter(concert_name__icontains=search):
            d = Concert.objects.filter(concert_name__icontains=search)
            return render(request, 'spage.html', locals())
        else:
            return render(request, "index.html")


def spage(request):
    concert = Concert.objects.all()
    return render(request, "spage.html")


def info(request):
    p1 = request.GET.get('p1')
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    try:
        singer = Singer.objects.get(name__icontains=p1)
        concerts = singer.concert_set.all()
    except:
        pass
    return render(request, p1 + '.html', locals())


def addfavor(request):
    if request.method == 'POST':
        try:
            get_concert = Concert.objects.get(
                concert_name=request.POST['favorite'])
            FavoriteConcert.objects.create(concert_name=get_concert)
            get_concert.votes += 1
            get_concert.save()
            a = get_concert.concert_name
            return HttpResponse(a)
        except (KeyError, Concert.DoesNotExist):
            return HttpResponse('伺服器出錯, 請洽客服')


def deletefavor(request):
    if request.method == 'POST':
        try:
            get_concert = Concert.objects.get(
                concert_name=request.POST['favorite'])
            get_concert.favoriteconcert_set.all().delete()
            a = get_concert.concert_name
            return HttpResponse(a)
        except (KeyError, Concert.DoesNotExist):
            pass


def search(request):
    if request.method == 'POST':
        search = request.POST.get("search")
        all_photos = Photo.objects.all()
        if Concert.objects.filter(concert_name__icontains=search):
            d = Concert.objects.filter(concert_name__icontains=search)
            return render(request, 'spage.html', locals())
        else:
            return HttpResponseRedirect("/index/")


def spage(request):
    concert = Concert.objects.all()
    return render(request, "spage.html")


def Aimer(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    try:
        singer = Singer.objects.get(name__icontains=p1)
        concerts = singer.concert_set.all()
    except:
        pass
    return render(request, "Aimer.html", locals())


def Aska(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "Aska.html", locals())


def BaiAn(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "BaiAn.html", locals())


def BTS(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "BTS.html", locals())


def MAMAMOO(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "MAMAMOO.html", locals())


def MorningGirl(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "MorningGirl.html", locals())


def Shawn(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "Shawn Mendes.html", locals())


def WestLife(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "WestLife.html", locals())


def XiaoBinZhe(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "XiaoBinZhe.html", locals())


def eight(request):
    all_fav = FavoriteConcert.objects.all()
    all_concerts = Concert.objects.all()
    all_photos = Photo.objects.all()
    return render(request, "831.html", locals())
