from django.shortcuts import render, redirect
from . models import Video, Movie, Profile
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import ProfileForm


class Home(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("netflixapp:profile-lists")
        return render(request, 'index.html')

method_decorator(login_required, name="dispatch")
class ProfileList(View):

    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context = {
            'profiles': profiles
        }
        return render(request, 'profilelist.html', context)

@method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request,*args, **kwargs):
        form=ProfileForm()

        return render(request,'profileCreate.html',{
            'form':form
        })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)

       
        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                # return redirect(f'/watch/{profile.uuid}')
                return redirect('netflixapp:profile-lists')

        return render(request,'profileCreate.html',{
            'form':form
        })


@method_decorator(login_required,name='dispatch')
class Watch(View):
    def get(self,request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            if profile not in request.user.profiles.all():
                return redirect(to="netflixapp:profile-lists")
            return render(request,'movieList.html', {'movies': movies})
        except Profile.DoesNotExist:
            return redirect(to="netflixapp:profile-lists")

            
        
@method_decorator(login_required,name='dispatch')
class ShowMovieDetail(View):
    def get(self,request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            return render(request,'movieDetail.html', {'movie': movie})
        except Movie.DoesNotExist:
            return redirect(to="netflixapp:profile-lists")

@method_decorator(login_required,name='dispatch')
class ShowMovie(View):
    def get(self,request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.video.values()
            return render(request,'showMovie.html', {'movie': list(movie)})
        except Movie.DoesNotExist:
            return redirect(to="netflixapp:profile-lists")