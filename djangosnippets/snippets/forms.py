from django import forms

from snippets.models import Snippet


class SnippetFrom(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')
