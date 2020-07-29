from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Movie
from .forms import *
from django.db.models import Avg
# Create your views here.

def home(request):
    query=request.GET.get("title")
    allMovies=None
    if query:
        allMovies = Movie.objects.filter(name__icontains=query)
    else:
        allMovies=Movie.objects.all()



    context={
    "movies":allMovies,
    }
    return render(request,'geekapp/index.html',context)

def detail(request, id):

    movie=Movie.objects.get(id=id)
    reviews=Review.objects.filter(movie=id).order_by("-comment")
    average=reviews.aggregate(Avg("rating"))["rating__avg"]
    if average==None:
        average=0
    average=round(average,2)
    context={
    "movie":movie,
    "reviews":reviews,
    "average":average
    }

    return render(request,'geekapp/details.html',context)


def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=="POST":
                form=MovieForm(request.POST or None)

                if form.is_valid():
                    data=form.save(commit=False)
                    data.save()
                    return redirect("geekapp:home")
            else:
                form=MovieForm()
            return render(request,'geekapp/addmovies.html',{'form':form, "controller":"Add Movies"})
        else:
            return redirect("geekapp:home")
    return redirect("accounts:login")
def edit_movies(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie=Movie.objects.get(id=id)

            if request.method=="POST":
                form=MovieForm(request.POST or None,instance=movie)

                if form.is_valid():
                    data=form.save(commit=False)
                    data.save()
                    return redirect("geekapp:detail",id)
            else:
                form=MovieForm(instance=movie)
            return render(request,'geekapp/addmovies.html',{"form":form, "controller":"Edit Movies"})
        else:
            return redirect("geekapp:home")
    return redirect("geekapp:home")

def delete_movies(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie=Movie.objects.get(id=id)
            movie.delete()
            return redirect("geekapp:home")
        else:
            return redirect("geekapp:home")
    return redirect("accounts:login")

def add_review(request,id):
    if request.user.is_authenticated:
        movie=Movie.objects.get(id=id)
        if request.method == 'POST':
            form=ReviewForm(request.POST or None)
            if form.is_valid():
                data=form.save(commit=False)
                data.comment=request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user=request.user
                data.movie=movie
                data.save()
                return redirect("geekapp:detail",id)
        else:
            form=ReviewForm()
        return render(request,"geekapp/details.html",{"form":form})
    else:
        return redirect("accounts:login")
def edit_review(request,movie_id,review_id):
    if request.user.is_authenticated:
        movie=Movie.objects.get(id=movie_id)
        review=Review.objects.get(movie=movie,id=review_id)

        if request.user == review.user:
            if request.method=="POST":
                form =ReviewForm(request.POST,instance=review)
                if form.is_valid():
                    data=form.save(commit=False)
                    if( data.rating > 10) or (data.rating < 0):
                        error= "Please select between 0 to 10 !"
                        return render(request,'geekapp/editreview.html',{"error":error,"form":form})
                    else:
                        data.save()
                        return redirect("geekapp:detail",movie_id)


            else:
                form =ReviewForm(instance=review)
                return render(request,"geekapp/editreview.html",{"form":form})
        else:
            return redirect("geekapp:detail",movie_id)
    else:
        return redirect("accounts:login")
def delete_review(request,movie_id,review_id):
    if request.user.is_authenticated:
        movie=Movie.objects.get(id=movie_id)
        review=Review.objects.get(movie=movie,id=review_id)

        if request.user == review.user:
            review.delete()
        return redirect("geekapp:detail",movie_id)
    else:
        return redirect("accounts:login")
