
# Emotify

*Creating an Emotional Backdrop to Meet Your Musical Needs*

This repository holds the code used for model building and development.

For details and code for the deployment of the actual Streamlit application, see [this repo](https://github.com/jecutter/Emotify_App).

To try out the app, visit the [application website](http://dataproject.xyz/).

<a href="url"><img src="img/emotify_app_example.png" width="80%"></a>

## Motivation

Music streaming services bring in an enormous amount of revenue. In 2019, subscriptions to such services *alone* brought in > $7 billion, excluding ad revenue.

Spotify, the Goliath of music streaming services, offers the ability for users to create custom playlists, and provides a wide variety of pre-categorized playlists as well. Mood playlists are quite popular, however they are manually curated by humans. Can we automate this process of filtering songs by their emotional content?

Emotify is a tool for listeners and content creators to filter any songs by emotion. This is a proof-of-concept for a feature that could be implemented on a larger scale as a premium subscription service, but this application is limited to any given public playlist (see the [application website](http://dataproject.xyz/)).

## Repo Contents

* Emotify_Project_Dev.ipynb - the main Jupyter notebook for this project containing data collection, EDA, model development, and model validation (with the sections ordered in time, showing project development)
* build_final_model.py - a separate Python script run specifically to build final models within specific environments (with parameters tuned in the development notebook)
* Data/ - folder containing combined musical data resulting from many hours of scraping and cleaning from various data sources (see below)
* img/ - folder containing project images

## Data Sources

* Last.fm (Million Songs Dataset, SQLite databases for [track info](http://millionsongdataset.com/pages/find-song-specific-name-or-feature/) ("track_metadata.db") and [user tags](http://millionsongdataset.com/lastfm/#getting) ("lastfm_tags.db"))
* Spotify API (via [Spotipy Python library](https://spotipy.readthedocs.io/en/2.12.0/))
* Genius API (via [LyricsGenius](https://github.com/johnwmillr/LyricsGenius))

## Building the Models

<p align="center">
  <a href="url"><img src="img/emotify_dataflow_diagram.png" width="80%"></a>
 </p>


