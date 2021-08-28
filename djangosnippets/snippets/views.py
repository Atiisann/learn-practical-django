from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from snippets.forms import SnippetFrom
from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/top.html', context)

@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetFrom(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetFrom()
    return render(request, 'snippets/snippet_new.html', {'form': form})


def snippet_edit(request):
    return HttpResponse('edit snippets')


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})
