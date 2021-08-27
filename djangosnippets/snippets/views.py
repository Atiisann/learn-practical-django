from django.http import HttpResponse
from django.shortcuts import render

from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/top.html', context)


def snippet_new(request):
    return HttpResponse('register snippets')


def snippet_edit(request):
    return HttpResponse('edit snippets')


def snippet_detail(request):
    return HttpResponse('detail snippet')
