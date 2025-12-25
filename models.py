from django.db import models

class Labels(models.Model):
    label_id = models.IntegerField(primary_key=True)
    label_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'labels'
        verbose_name = "Label"
        verbose_name_plural = "Labels"
        ordering = ['label_name']

    def __str__(self):
        return self.label_name if self.label_name else f"Label {self.label_id}"

class Artists(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'artists'
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ['artist_name']

    def __str__(self):
        return self.artist_name


class Genres(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'genres'
        verbose_name = "Genre"
        verbose_name_plural = "Genres" # Çift 's' hatasını önler

    def __str__(self):
        return self.genre_name

class Albums(models.Model):
    album_id = models.IntegerField(primary_key=True)
    album_name = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    label = models.ForeignKey('Labels', models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums'
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        unique_together = (('album_name', 'label', 'release_date'),) #burası eklendi

    def __str__(self):
        return self.album_name if self.album_name else f"Album {self.album_id}"

class Songs(models.Model):
    track_id = models.IntegerField(primary_key=True)
    track_name = models.CharField(max_length=255)
    duration_min = models.FloatField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    instrumentalness = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)
    tempo = models.FloatField(blank=True, null=True)
    album = models.ForeignKey(Albums, models.CASCADE) # SQL: ON DELETE CASCADE

    class Meta:
        managed = False
        db_table = 'songs'
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ['track_name']
        
    def __str__(self):
        return self.track_name

# Ara Tablolar (ManyToMany İlişkileri için)
class SongArtists(models.Model):
    track = models.OneToOneField(Songs, models.CASCADE, primary_key=True)
    artist = models.ForeignKey(Artists, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'song_artists'
        unique_together = (('track', 'artist'),)
        verbose_name = "Song Artist"
        verbose_name_plural = "Song Artists"

class SongGenres(models.Model):
    track = models.OneToOneField(Songs, models.CASCADE, primary_key=True)
    genre = models.ForeignKey(Genres, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'song_genres'
        unique_together = (('track', 'genre'),)
        verbose_name = "Song Genre"
        verbose_name_plural = "Song Genres"