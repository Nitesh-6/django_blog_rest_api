from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class BlogListView(APIView):
    def get(self, req):
        all_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, req):
        serializer = BlogSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BlogDetailView(APIView):
    def get(self, req, pk):
        blog = Blog.objects.get(is_public=True, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, req, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# def blog_list(req):
#     if req.method == "GET":
#         all_blogs = Blog.objects.filter(is_public=True)
#         serializer = BlogSerializer(all_blogs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if req.method == "POST":
        # serializer = BlogSerializer(data=req.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def blog_detail(req, pk):
#     if req.method == "GET":
        # blog = Blog.objects.get(is_public=True, pk=pk)
        # serializer = BlogSerializer(blog)
        # return Response(serializer.data, status=status.HTTP_200_OK)
#     if  req.method == "PUT":
        # blog = Blog.objects.get(pk=pk)
        # serializer = BlogSerializer(blog, data=req.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if req.method == 'DELETE':        
        # blog = Blog.objects.get(pk=pk)
        # blog.delete()
        # return Response(status=status.HTTP_200_OK)