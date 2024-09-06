from django.shortcuts import render

# Create your views here.
import random

moderatorList = [
    "Fr. Gilchrist",
    "Maman Mado",
    "Maman Caro",
    "Maman Sandrine",
    "Fr. Yves",
    "Fr. Jeremie",
    "Fr. Gentiny",
    "Fr. Onesime",
    "Maman Hadassa",
    "Maman Olga",
    "Maman Alphie",
    "Maman Gisèle",
    "Maman Mémé",
    "Maman Bijou",
]

def moderator(request):
    moderator = random.choice(moderatorList)
    context = {"moderator": moderator}
    return render(request, "ofele_app/ofele.html", context)
