from django.shortcuts import render
from django.http import HttpResponse
#from django.core import serializers
from rest_framework import serializers
import json
from abstracts.models import Abstract, Journal



# Create your views here.

class JournalSerializer(serializers.Serializer):
    journal_title = serializers.CharField(max_length=200)


def get_all_abstracts(request):

    serialized_data = serializers.serialize("json", Journal.objects.filter(journal_title="PLOS Computational Biology"))
    serializer = JournalSerializer(serialized_data)

    #data = json.dumps(serialized_data)
    # return HttpResponse(data, mimetype='application/json')
    return HttpResponse(serializer.data)




