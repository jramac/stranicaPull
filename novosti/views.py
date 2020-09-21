from django.shortcuts import render, get_object_or_404

from .models import Post, PostImage





def blog(request):

    context = {

        'posts' : Post.objects.all()

    }

    return render(request, 'novosti/novosti.html', context)



def detail(request, id):

    post = get_object_or_404(Post, id=id)

    photos = PostImage.objects.filter(post=post)

    return render(request, 'novosti/detail.html', {

        'post':post,

        'photos':photos

    })



def home(request):

    post = Post.objects.filter().order_by('-id')[:4]

    images = PostImage.objects.filter().order_by('id')

    postid = Post.objects.filter().order_by('-id').values_list('id',flat=True)[:4]

    imageid = PostImage.objects.filter().order_by('id').values_list('post_id',flat=True)

    count = imageid.count()

    postcount = postid.count()

    br=0

    for i in range (postcount):

        br=0

        for j in range (count):

            if postid[i]==imageid[j]:

                br=br+1

        broj = int(postid[i])

        postedit = Post.objects.get(id=broj)

        postedit.thumbBroj = br

        postedit.save()
    
    imageidlist = list(imageid)
    for k in range(count):
        if k>0:
            if imageid[k]==imageid[k-1]:
                imageidlist.remove(imageid[k])

    imageidlistcount = len(imageidlist)

    for m in range (imageidlistcount):
        a = PostImage.objects.filter(post_id = imageidlist[m]).values_list('id',flat=True)
        b = list(a)
        bcount = len(b)
        for n in range(bcount):
            edit = PostImage.objects.get(id = b[n])
            edit.redni = n
            edit.save()

    return render(request, 'novosti/home.html',{

        'posts':post,

        'images':images,

        'postid':postid,

        'imageid':imageid

    })



def oprojektu(request):

    return render(request, 'novosti/oprojektu.html')



def partneri(request):

    return render(request, 'novosti/partneri.html')



def kontakt(request):

    return render(request, 'novosti/kontakt.html')