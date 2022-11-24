# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS EXTRA     |=====|
# |=========================================|
from django.shortcuts import get_object_or_404, render, redirect

# |=========================================|
# |=====|       BIBLIOTECAS EXTRA     |=====|
# |=========================================|
from .models import Category, BeePost, Comment

# |=| Método para la página con la lista de artículos publicados |=|
def articleList(request):
    posts = BeePost.objects.all()

    return render(request, 'BeePost/frontpage.html', {'posts': posts})

# |=| Método para la asignación de página para cada artículo |=|
def article_detail(request, slug):
    post = get_object_or_404(BeePost, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')

        if name and comment:
            Comment.objects.create(
                post=post,
                name=name,
                comment=comment
            )

            return redirect('post_detail', slug=post.slug)

    return render(request, 'BeePost/detail.html', {'post': post})