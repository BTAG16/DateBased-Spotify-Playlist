# DateBased-Spotify-Playlist

## Overview

**DateBased-Spotify-Playlist** is a Python application that allows users to create a Spotify playlist consisting of the top 100 songs from a specific date based on the Billboard Hot 100 chart. By simply providing a date in the format YYYY-MM-DD, users can generate a personalized playlist of popular songs from that time period.


## Features
```markdown
- Fetches the Billboard Hot 100 songs for a specified date.
- Uses the Spotify API to create a private playlist.
- Automatically adds the top 100 songs to the created playlist.
- Easy-to-use command-line interface.
```
## Requirements
```markdown
- Python 3.6 or higher
- `spotipy` library for Spotify API integration
- `requests` library for making HTTP requests
- `beautifulsoup4` library for parsing HTML
- `python-dotenv` library for managing environment variables
```
## Installation
```markdown
1. **Clone the repository:**

   ```bash
   git clone https://github.com/BTAG16/DateBased-Spotify-Playlist.git
   cd DateBased-Spotify-Playlist
   ```

2. **Install the required libraries:**

   You can use pip to install the necessary packages:

   ```bash
   pip install spotipy requests beautifulsoup4 python-dotenv
   ```

3. **Set up your Spotify Developer account:**

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
   - Get your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and set the `SPOTIPY_REDIRECT_URI` (you can use `http://localhost:8888/callback` for local development).

4. **Create a `.env` file:**

   In the root of your project directory, create a file named `.env` and add the following lines, replacing the placeholders with your actual credentials:

   ```env
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. When prompted, enter the date in the format YYYY-MM-DD. For example:

   ```
   Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2024-10-06
   ```

3. The application will create a private Spotify playlist named "Hot 100 Songs from [Date]" and add the top 100 songs from that date.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. Any contributions are welcome!

## Acknowledgments

- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [Billboard](https://www.billboard.com/charts/hot-100/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## Contact

For any questions or feedback, feel free to open an issue on the repository or contact me at [rumeighoraye@gmail.com].
