import rest_framework.mixins as mixins
import rest_framework.generics as generics
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


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

    def get_queryset(self):
        qs = Status.objects.all()
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        id_param = request.GET.get('id', None)
        query_set = self.get_queryset()
        obj = None

        if id_param is not None:
            obj = get_object_or_404(query_set, id=id_param)
            self.check_object_permissions(request, object)

        return obj

    def get(self, request, *args, **kwargs):
        id_param = request.GET.get('id', None)
        if id_param is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
