"""Posts View Module."""
from django.views import generic
from blog.models import Post, Category
from django.db.models import Q


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = super(PostList, self).get_queryset()
        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if query is not None and query != '':
                queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

        if 'c' in self.request.GET:
            c = self.request.GET['c']
            if c is not None and c != '':
                queryset = queryset.filter(category__id=c)

        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        return data


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
