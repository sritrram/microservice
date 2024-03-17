from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class BaseView(APIView):
    def get(self, request):
        return Response("Welcome to the Order Service!")

class OrderHistoryView(APIView):

    def get(self, request):
        return Response("Order History")


