from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Menu
from .serializers import MenuSerializer

class MenuAPIView(APIView):
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = MenuSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, *args, **kwargs):
    #     menu = Menu.objects.get(pk=pk)
    #     serializer = MenuSerializer(menu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, *args, **kwargs):
    #     menu = Menu.objects.get(pk=pk)
    #     menu.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)