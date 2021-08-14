from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import *
from app.bbdata import *


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        cRanks = get_vCrankDay()
        pRanks = get_vPrankDay()
        cHits = get_vStats()


        ctxt = super().get_context_data()
        ctxt["cranks"] = cRanks
        ctxt["pranks"] = pRanks
        ctxt["cHits"] = cHits
        return ctxt


class TeamsView(TemplateView):
    template_name = "teams.html"


class PlayerView(TemplateView):
    template_name = "player.html"


class LibraryView(TemplateView):
    template_name = "library.html"


class NewsView(TemplateView):
    template_name = "news.html"

