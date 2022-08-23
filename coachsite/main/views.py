from django.shortcuts import render, HttpResponse, redirect
from main import models
# Create your views here.


def main(request):
    cards = models.ForWhom.objects.filter(name_of_for_whom='No time')
    cards2 = models.ForWhom.objects.filter(name_of_for_whom='belly')
    cards3 = models.ForWhom.objects.filter(name_of_for_whom='food')
    cards4 = models.ForWhom.objects.filter(name_of_for_whom='muffin-top')
    cards5 = models.ForWhom.objects.filter(name_of_for_whom='waist')
    customer_results = models.CustomerResult.objects.all()
    tariffs = models.Tariffs.objects.all()
    about_me = models.AboutMe.objects.all()
    contacts = models.Contacts.objects.all()

    data = {
        'cards': cards,
        'cards2': cards2,
        'cards3': cards3,
        'cards4': cards4,
        'cards5': cards5,
        'customer_results': customer_results,
        'tariffs': tariffs,
        'about_me': about_me,
        'contacts': contacts,
    }
    # return HttpResponse('hello from main')
    return render(request, 'prime.html', context=data)   # , context=data
