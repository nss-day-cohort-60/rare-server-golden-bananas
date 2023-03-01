"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category


class CategoryView(ViewSet):
    """rare category view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category
        Returns:
            Response -- JSON serialized category
        """
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all categories
        Returns:
            Response -- JSON serialized list of categories
        """
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle Post operations
            returns
                Response -- JSON serialized category instance with 
                status code 201"""

        category = Category.objects.create(
            label=request.data["label"],
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a category
        Returns:
            Response -- Empty body with 204 status code
        """

        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        
        category.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categorys
    """
    class Meta:
        model = Category
        fields = ('id', 'label')

