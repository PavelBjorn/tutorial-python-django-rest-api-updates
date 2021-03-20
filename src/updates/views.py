from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# def detail_view(request):
#     return render() # return JSON data


def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)
