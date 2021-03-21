import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from .models import Update


def json_example_view(request):
    # URI -- FOR REST API

    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):

    def get(self, request, *args, **kwargs):
        # URI -- FOR REST API
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)
