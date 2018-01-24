from django.contrib.auth.decorators import login_required
from django.conf import settings
from cw.models import Votes
from django.shortcuts import render, HttpResponse
import json

def votes(request):
    context = {}
    return render(request, 'index.html', context)

def index(request):
    context = {}
    return render(request, 'vote.html', context)

def cast_vote(request):
    args = {}
    answer = request.GET.get('answer', None)
    args["answer"] = answer
    possible_options = ["nairobi", "athens", "bangkok", "reykjavik"]
    if answer:
        answer = answer.lower().strip()
        if answer in possible_options:
            record, created = Votes.objects.get_or_create(id = 1)
            if answer == "nairobi":
                record.nairobi += 1
            if answer == "athens":
                record.athens += 1
            if answer == "bangkok":
                record.bangkok += 1
            if answer == "reykjavik":
                record.reykjavik += 1
            record.total += 1
            record.save()
            args["created"] = created
            args["response"] = "saved"
    return HttpResponse(json.dumps(args), content_type="application/json")

def get_votes(request):
    record = Votes.objects.get(id=1)
    args = {
        "nairobi": record.nairobi,
        "athens": record.athens,
        "bangkok": record.bangkok,
        "reykjavik": record.reykjavik,
    }
    return HttpResponse(json.dumps(args), content_type="application/json")