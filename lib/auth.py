import spotipy
import time
import config
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

from rich.console import Console

console = Console()
console.clear()


def verify_auth(sp) -> None:
    try:
        sp.me()
        console.print("Authenticated successfully!", style="bold green")
        time.sleep(2)
        console.clear()
    except:
        console.print("\nAuthentication failed!", style="bold red")
        time.sleep(2)
        sys.exit(1)
        # console.clear()


def authenticate() -> spotipy.Spotify:
    scope = "playlist-modify-public"
    auth_manager = SpotifyOAuth(
        scope=scope,
        username=config.SPOTIFY_USER_ID,
        client_id=config.SPOTIFY_CLIENT_ID,
        client_secret=config.SPOTIFY_CLIENT_SECRET,
        redirect_uri=config.SPOTIFY_REDIRECT_URI,
        open_browser=False,
        cache_path="token.txt",
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)
    verify_auth(sp)

    return sp


def authenticate_browser() -> spotipy.Spotify:
    scope = "playlist-modify-public"
    token = util.prompt_for_user_token(
        scope=scope,
        username=config.SPOTIFY_USER_ID,
        client_id=config.SPOTIFY_CLIENT_ID,
        client_secret=config.SPOTIFY_CLIENT_SECRET,
        redirect_uri=config.SPOTIFY_REDIRECT_URI,
        cache_path="token.txt",
    )

    sp = spotipy.Spotify(auth=token)
    verify_auth(sp)

    return sp


def authenticate_auth_manager() -> spotipy.Spotify:
    auth_manager = SpotifyClientCredentials(
        client_id=config.SPOTIPY_CLIENT_ID, client_secret=config.SPOTIPY_CLIENT_SECRET
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)
    verify_auth(sp)

    return sp
