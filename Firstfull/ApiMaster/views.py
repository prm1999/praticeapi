from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import *


class CropView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = CropSerializer
    queryset = Crop.objects.all()

    def get(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CropUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = CropSerializer
    queryset = Crop.objects.all()


    def get(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Crop, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Crop, pk=kwargs['id'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = generics.get_object_or_404(Crop, pk=kwargs['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

