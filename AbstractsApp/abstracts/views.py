from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from abstracts.models import Abstract, Journal



# Create your views here.



def get_all_abstracts(request):

    serialized_data = serializers.serialize("json", Journal.objects.all())

    data = json.dumps(serialized_data, indent=4)
    return HttpResponse(data)




