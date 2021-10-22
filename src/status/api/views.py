import rest_framework.mixins as mixins
import rest_framework.generics as generics
import json
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False

    return is_valid


class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView
):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    object_id = None

    def get_queryset(self):
        qs = Status.objects.all()
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        query_set = self.get_queryset()
        obj = None

        print(self.object_id)
        if self.object_id is not None:
            obj = get_object_or_404(query_set, id=self.object_id)
            self.check_object_permissions(self.request, object)

        return obj

    def get(self, request, *args, **kwargs):
        self._retrieve_id(request)

        if self.object_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        self._retrieve_id(request)
        return self.update(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        self._retrieve_id(request)
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        self._retrieve_id(request)
        return self.destroy(request, args, kwargs)

    def perform_destroy(self, instance):
        if instance is not None:
           return instance.delete()
        return None

    def _retrieve_id(self, request):
        self.object_id = None
        id_param = request.GET.get('id', None)
        if id_param is None:
            body = request.body
            if is_json(body):
                self.object_id = json.loads(body).get('id', None)
        else:
            self.object_id = id_param

        print(request.body)
