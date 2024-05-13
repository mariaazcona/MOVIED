"""
def cinema_list(request):
    all_cinemas = Cinema.objects.all()
    return render(request, "cinemas.html", {"cinemas": all_cinemas})


def cinema_detail(request, id):
    cinema = get_object_or_404(Cinema, id_cinema=id)
    movies = Movie.objects.filter(id_cinema=cinema)
    context = {
        'cinema': cinema,
        'movies': movies
    }
    return render(request, 'movie.html', context)
"""