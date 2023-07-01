from rest_framework import views, status
from rest_framework.response import Response
from .models import Company
from .serializers import CompanyGetSerializer

# Create your views here.
class CompanyAPIView(views.APIView):

    serializer_class = CompanyGetSerializer

    def get(self, request):
        queryset = Company.objects.all()
        companies = CompanyGetSerializer(queryset, many=True)
        return Response(companies.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        resp = self.serializer_class(company)
        return Response(resp.data, status=status.HTTP_201_CREATED)
