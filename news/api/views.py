from rest_framework import generics, permissions
from ..models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class PostDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    queryset = Post.objects.all()


class CommentListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            post = self.kwargs['post']
            if post:
                return Comment.objects.filter(post__id=post)
        except:
            post = None
            return Comment.objects.all()


class CommentCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()