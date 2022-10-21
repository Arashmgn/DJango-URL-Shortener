from random import choices
from string import ascii_letters
from django.shortcuts import render
from .models import url
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
import validators


def url_shortner(request):
    if request.method=='POST':
        expired_ulrs=url.objects.filter(expiration__lte=timezone.now())
        expired_ulrs.delete()
        long_url = request.POST.get('long_url')

        if long_url[-1]!='/' :
            long_url = long_url + '/'

        if long_url[0:8] != "https://":
            long_url = "https://"+long_url


        if long_url and validators.url(long_url):
            long_exists = url.objects.filter(long_url=long_url).first()
            if long_exists == None:
                short_url=make_short_url(long_url)
                new_url = url.objects.create(short_url=short_url,long_url=long_url)
                new_url.save()
                context={'short_url':new_url}
                return render(request,"short_url.html",context=context)
            else:  
                context={'short_url':long_exists}
                return render(request,"short_url.html",context=context)
        else:
            messages.warning(request, 'Please enter a valid URL.')
            return redirect("home")
        
    else:
        return render(request,"home.html")


def make_short_url(long_url):
    letters = ascii_letters
    short_url = choices(letters,k=4)
    short_url = "".join(short_url)
    short_exits = url.objects.filter(short_url=short_url).first()
    if short_exits is None:
        return short_url
    else:
        return make_short_url(long_url)

def url_redirect(request,slug):
    long_url = get_object_or_404(url,short_url=slug)
    return redirect(long_url.long_url)