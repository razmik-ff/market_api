from rest_framework import views, status
from rest_framework.response import Response

from .models import Company
from .serializers import CompanyGetSerializer


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


class CompanyDetailAPIView(views.APIView):

    serializer_class = CompanyGetSerializer

    def get(self, request, c_pk):
        queryset = Company.objects.get(pk=c_pk)
        companies = CompanyGetSerializer(queryset)
        return Response(companies.data)

    def patch(self, request, c_pk):
        company = Company.objects.filter(pk=c_pk).first()
        serializer = CompanyGetSerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, request, c_pk):
        company = Company.objects.filter(pk=c_pk)
        company.delete()
        return Response({"msg": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
