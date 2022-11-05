from lib import auth
from lib import utils

from rich.console import Console

console = Console()
console.clear()


def main() -> None:
    # Initialize Authentication
    sp = auth.authenticate()

    # Get seed tracks and artists
    seed = utils.get_seed(sp)

    # Get recommendations
    recommendations = utils.get_recommendations(sp, seed)

    # Display recommendations
    # utils.display_recommendations(recommendations)

    # Generate playlist
    playlist_id = utils.generate_playlist(recommendations, sp)

    # Add tracks to playlist
    playlist_url = utils.add_to_playlist(playlist_id, recommendations, sp)

    console.print(f"Playlist generated at URL: [blue]{playlist_url}[/blue]")


if __name__ == "__main__":
    main()
