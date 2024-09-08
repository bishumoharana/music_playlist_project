def determine_next_song(telemetry_data):
    # Simplified logic to choose the next song
    if telemetry_data['road_type'] == 'highway':
        return "spotify:track:7GhIk7Il098yCjg4BQjzvb"  # Example Spotify URI
    elif telemetry_data['road_type'] == 'local road':
        return "spotify:track:0GjEhVFGZW8afUYGChu3Rr"
    else:
        return "spotify:track:1rfofaqEpACxVEHIZBJe6W"
