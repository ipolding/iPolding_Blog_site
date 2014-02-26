from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from abstracts.models import Abstract, Journal



# Create your views here.



def get_all_abstracts(request):

    serialized_data = serializers.serialize("python", Journal.objects.filter(journal_title="PLOS Computational Biology"))

    data = json.dumps(serialized_data)
    # return HttpResponse(data, mimetype='application/json')
    return HttpResponse(data)




