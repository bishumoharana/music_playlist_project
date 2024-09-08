from flask import Flask, render_template, request
from music_controller import MusicController
from telemetry import Telemetry

app = Flask(__name__)

# Initialize music controller and telemetry modules
music_controller = MusicController()
telemetry = Telemetry()

@app.route('/')
def home():
    # Fetch telemetry data
    data = telemetry.get_data()
    # Get the next song based on the telemetry data
    next_song = music_controller.get_next_song(data)
    return render_template('index.html', song=next_song, telemetry=data)

if __name__ == '__main__':
    app.run(debug=True)
