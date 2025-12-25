from django.contrib import admin
from .models import Songs, Albums, Artists, Labels, Genres

# 1. Artists Ayarları
@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = ('artist_id', 'artist_name')
    search_fields = ('artist_name',)

# 2. Labels Ayarları
@admin.register(Labels)
class LabelsAdmin(admin.ModelAdmin):
    list_display = ('label_id', 'label_name')
    search_fields = ('label_name',)

# 3. Genres Ayarları
@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('genre_id', 'genre_name')
    search_fields = ('genre_name',)

# 4. Albums Ayarları
@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'release_date', 'label')
    list_filter = ('release_date', 'label')
    search_fields = ('album_name',)
    def display_label(self, obj):
        return obj.label.label_name if obj.label else "-"
    display_label.short_description = 'Label'

# 5. Songs Ayarları
@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    # list_display içine 'display_artists' ekledik
    list_display = ('track_name', 'album', 'display_artists', 'popularity', 'duration_min')
    list_filter = ('popularity', 'album')
    search_fields = ('track_name',)
    ordering = ('track_name',)

    # Şarkıya ait sanatçıları SongArtists ara tablosundan çeken fonksiyon
    def display_artists(self, obj):
        from .models import SongArtists
        # Bu şarkıya (obj) bağlı tüm sanatçı kayıtlarını getiriyoruz
        song_artists_records = SongArtists.objects.filter(track=obj)
        # Sanatçı isimlerini virgülle ayırarak birleştiriyoruz
        return ", ".join([sa.artist.artist_name for sa in song_artists_records])
    
    # Tablodaki sütun başlığı
    display_artists.short_description = 'Artists'