import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# def detail_view(request):
#     return render() # return JSON data

def json_example_view(request):
    # URI -- FOR REST API

    data = {
        "count": 1000,
        "content": "Some new content"
    }
    # return JsonResponse(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
