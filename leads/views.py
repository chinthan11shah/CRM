from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context=context)


def lead_details(request, pk):
    # context = {}
    # return render(request, lead_detail.html, context=context)
    print(pk)
    return HttpResponse("Here is the detail view")