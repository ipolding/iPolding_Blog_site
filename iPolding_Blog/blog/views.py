from django import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext, loader
from blog.models import Entry


def index(request):
    latest_blog_entries = Entry.objects.order_by('-pub_date')[:5]
    output = ', '.join([entry.title for entry in latest_blog_entries])
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'latest_blog_entries': latest_blog_entries,
    })
    return HttpResponse(template.render(context))

def entry(request, entry_id):
    # return HttpResponse("You are looking at blog %s." % entry_id)
    return HttpResponse("You are looking at blog %s." % entry_id)