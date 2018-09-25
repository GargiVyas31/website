from django.contrib.auth import authenticate
from .models import
'''from django.shortcuts import render,get_object_or_404
from .models import Albums,Song

def index(request):
    all_albums= Albums.objects.all()
    context={'all_albums': all_albums}
    return render(request,'photos/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Albums,pk=album_id)
    return render(request,'photos/detail.html',{'album': album})

def favorite(request,album_id):
    album= get_object_or_404(Albums,pk=album_id)
    try:
        selected_song= album.song_set.get(pk= request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request, 'photos/detail.html',{
            'album': album,
            'error_message': "You did not choose a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'photos/detail.html',{'album':album})'''

def login_page(request):
    from =LoginForm(request.POST or None)
    context={
        'form ':form
    }
    next_=request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path= next_ or next_post or None
    if form.is_valid():
        mob_no= form.cleaned_data.get("mob_no")
        password= form.cleaned_data.get("password")
        user= authenticate(request,mob_no=mob_no,password=password)
        if user is not None:
            login(request,user)
            try:
                del request.session[]

    return render(request,'',context)
User = get_user_model()
def register_page(request):
    form= Registration(request.POST or None)
