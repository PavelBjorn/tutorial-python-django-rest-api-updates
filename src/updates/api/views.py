from updates.api.mixins import CSRFExemptMixin
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
import json


# Creating, Updating, Deleting, Retrieving (1) - Update Model

class UpdateModelDetailAPI(View):
    def get(self, request, update_id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=update_id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def put(self, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def delete(self, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")


class UpdateModelListAPI(CSRFExemptMixin, View):

    def get(self, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, *args, **kwargs):
        data = json.dumps("message: Unknown Data")
        return HttpResponse(data, content_type="application/json")

    def delete(self, *args, **kwargs):
        data = json.dumps("message: You  can't delete whole list")
        return HttpResponse(data, content_type="application/json")