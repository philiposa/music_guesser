from django.http import HttpResponse
from django.shortcuts import render
from .spotify_utils import search_track
from django.template.loader import get_template
from django.conf import settings

def spotify_callback(request):
    return HttpResponse("Spotify Authentication Successful")

def home_view(request):
    # Render home.html from the central templates directory
    return render(request, 'home.html')

def search_view(request):
    # Simulating search functionality (just placeholder logic)
    query = request.GET.get('query', 'Bohe')  # Default query
    track_info = search_track(query)
    return render(request, 'search_result.html', {'track': track_info})