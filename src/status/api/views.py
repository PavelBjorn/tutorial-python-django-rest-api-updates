import rest_framework.mixins as mixins
import rest_framework.generics as generics

from status.models import Status
from .serializers import StatusSerializer


class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    lookup_field = 'id'  # "pk" - is default param. Changes "pk" to "id" for automatically object retrieving
    queryset = Status.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
