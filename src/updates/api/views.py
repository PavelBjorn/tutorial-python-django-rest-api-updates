from updates.api.mixins import CSRFExemptMixin
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
import json
from cfeapi.mixins import HttpResponseMixin


# Creating, Updating, Deleting, Retrieving (1) - Update Model

class UpdateModelDetailAPI(HttpResponseMixin, View):
    is_json = True

    def get(self, request, update_id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=update_id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def put(self, *args, **kwargs):
        return self.render_to_response({}, 403)

    def delete(self, *args, **kwargs):
        return self.render_to_response({}, 403)


class UpdateModelListAPI(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, *args, **kwargs):
        data = json.dumps("message: Unknown Data")
        return self.render_to_response(data=data, status=400)

    def delete(self, *args, **kwargs):
        data = json.dumps("message: You  can't delete whole list")
        return self.render_to_response(data=data, status=403)
