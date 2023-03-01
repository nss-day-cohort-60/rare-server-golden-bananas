"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser, Category


class PostView(ViewSet):
    """Level up post view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single post 
        Returns:
            Response -- JSON serialized post
        """
        
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all posts
        Returns:
            Response -- JSON serialized list of posts
        """
        user_id = request.query_params.get('user_id')

        if user_id:
            posts = Post.objects.filter(user=user_id)

        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle POST operations
            Returns
                Response -- JSON serialized post instance
        """
        rare_user = RareUser.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category"])

        post = Post.objects.create(
            title=request.data["title"],
            publication_date=request.data["publication_date"],
            content=request.data["content"],
            image_url=request.data["image_url"],
            approved = request.data["approved"],
            user= rare_user,
            category=category
        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a post
        Returns:
            Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.content = request.data["content"]
        post.image_url = request.data["image_url"]
        post.approved = request.data["approved"]

        category = Category.objects.get(pk=request.data["category"])
        post.category = category
        rare_user = RareUser.objects.get(user=request.auth.user)
        post.user = rare_user
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class RareUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = RareUser
        fields = ( 'id', 'full_name', )

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categorys
    """
    class Meta:
        model = Category
        fields = ( 'id', 'label')


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    category = CategorySerializer()
    user = RareUserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'category', 'user',)