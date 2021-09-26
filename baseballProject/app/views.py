from django.views.generic import TemplateView
from app.bbdata import *
from django.http.response import JsonResponse
import json
from django.shortcuts import render, redirect, get_object_or_404

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        cRanks = get_vCrankDay()
        pRanks = get_vPrankDay()
        cHits = get_vcStats()
        pHits = get_vpStats()
        cPicthes = get_vcPicthes()
        pPicthes = get_vpPicthes()


        ctxt = super().get_context_data()
        ctxt["cranks"] = cRanks
        ctxt["pranks"] = pRanks
        ctxt["cHits"] = cHits
        ctxt["pHits"] = pHits
        ctxt["cPicthes"] = cPicthes
        ctxt["pPicthes"] = pPicthes
        ctxt["active_path"] = "top"
        return ctxt


class TeamsView(TemplateView):
    template_name = "teams.html"

    def get_context_data(self):

        team = self.request.GET.get("teams")
        if not team:
            team = "giants"
        bstats = get_team_bstats(team)
        pstats = get_team_pstats(team)

        ctxt = super().get_context_data()

        ctxt["bstats"] = bstats
        # ctxt["pstats"] = pstats
        ctxt["active_path"] = "teams"
        # json.dumps(ctxt, default=str)

        print(type(ctxt))
        return ctxt


class PlayerView(TemplateView):
    template_name = "player.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["active_path"] = "player"
        return ctxt


class LibraryView(TemplateView):
    template_name = "library.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["active_path"] = "library"
        return ctxt


class NewsView(TemplateView):
    template_name = "news.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["active_path"] = "news"
        return ctxt

