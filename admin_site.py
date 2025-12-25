from django.contrib.admin import AdminSite
from .models import Artist, Album, Song

class EchoVerseAdminSite(AdminSite):
    site_header = "EchoVerse Admin Panel"
    site_title = "EchoVerse Admin"
    index_title = "Dashboard"

    def each_context(self, request):
        context = super().each_context(request)

        context["total_artists"] = Artist.objects.count()
        context["total_albums"] = Album.objects.count()
        context["total_songs"] = Song.objects.count()

        return context
