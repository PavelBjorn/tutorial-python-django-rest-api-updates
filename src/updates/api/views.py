from updates.api.mixins import CSRFExemptMixin
from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
import json
from cfeapi.mixins import HttpResponseMixin


# Creating, Updating, Deleting, Retrieving (1) - Update Model

class UpdateModelDetailAPI(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get_object(self, object_id=None):
        qs = UpdateModel.objects.filter(id=object_id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, update_id, *args, **kwargs):
        obj = self.get_object(update_id)

        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def put(self, request, update_id, *args, **kwargs):
        obj = self.get_object(update_id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        print(dir(request))
        print(request.POST)
        body = request.body
        print(body)
        return self.render_to_response({}, 403)

    def delete(self, request, update_id, *args, **kwargs):
        obj = self.get_object(update_id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        return self.render_to_response({}, 403)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Forbidden, please use the api/updates/ endpoint"})
        return self.render_to_response(json_data, 403)


class UpdateModelListAPI(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize
            return self.render_to_response(data=obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data=data, status=400)
        data = json.dumps("message: Not Allowed")
        return self.render_to_response(data=data, status=406)

    def delete(self, request, *args, **kwargs):
        data = json.dumps("message: You  can't delete whole list")
        return self.render_to_response(data=data, status=403)
