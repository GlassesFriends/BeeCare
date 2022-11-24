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
def wikihome(request):
    posts = BeePost.objects.all()

    return render(request, 'wiki/wikihome.html', {'posts': posts})

# |=| Método para la asignación de página para cada artículo |=|
def article_detail(request, bPostSlug):
    post = get_object_or_404(BeePost, bPostSlug=bPostSlug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')

        if name and comment:
            Comment.objects.create(
                post=post,
                name=name,
                comment=comment
            )

            return redirect('post_detail', bPostSlug=post.bPostSlug)

    return render(request, 'wiki/detail.html', {'post': post})