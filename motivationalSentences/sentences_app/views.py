import json
from .models import Phrase
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class PhraseView(TemplateView):
    template_name = "_base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        for obj in Phrase.objects.filter(is_active=True):
            data.append([obj.id, obj.phrase, "" if obj.background == "" else obj.background.url])
        context['data'] = json.dumps(data)
        return context
