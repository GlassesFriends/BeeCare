# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS EXTRA     |=====|
# |=========================================|
from django.shortcuts import get_object_or_404, render, redirect
from apps.member.decorators import user_auth

# |=========================================|
# |=====|       BIBLIOTECAS EXTRA     |=====|
# |=========================================|
from .models import category, beePost, comment

# |=| Método para la página con la lista de artículos publicados |=|
def wikihome(request):
    posts = beePost.objects.all()

    return render(request, 'wiki/wikihome.html', {'posts': posts})

# |=| Método para la asignación de página para cada artículo |=|
def article_detail(request, bPostSlug):
    post = get_object_or_404(beePost, bPostSlug=bPostSlug)

    if request.method == 'POST':
        memberObj = request.user.member
        commentText = request.POST.get('membComment', '')

        if commentText:
            comment.objects.create(
                commentBeepost=post,
                commentMember=memberObj,
                commentText=commentText
            )

            return redirect('article_detail', bPostSlug=post.bPostSlug)

    return render(request, 'wiki/detail.html', {'post': post})