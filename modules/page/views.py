from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.


class PageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Your custom logic here
        return Response({"message": "This is a custom page without a queryset."})
