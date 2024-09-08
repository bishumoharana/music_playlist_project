# Dynamic Music Playlist Project

This is a Python-based solution for creating dynamic music playlists based on vehicle telemetry data. The app integrates with Spotify and provides a simple web interface to control the music playback.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd music_playlist_project
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### 3. Install the Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
- Spotify: Get your client ID and secret from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
- OpenWeatherMap: Get your API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

### 5. Run the Application
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your web browser to see the app in action.

## Project Structure

```
music_playlist_project/
│
├── app.py                     # Main Flask app
├── music_controller.py        # Logic to control music playback
├── telemetry.py               # Module to fetch telemetry and weather data
├── playlist_logic.py          # Module to handle dynamic playlist logic
├── templates/
│   └── index.html             # HTML template for web interface
├── static/
│   └── style.css              # CSS for styling
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
```

## Next Steps

- Implement unit tests for each component.
- Add more complex playlist logic based on additional telemetry data.
- Deploy the application to a cloud platform.

## Contributing

Feel free to fork the repository and submit pull requests to contribute to the project.
