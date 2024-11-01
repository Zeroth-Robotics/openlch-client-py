import time
from openlch.hal import HAL
import sounddevice as sd
from scipy.io import wavfile
import io

def test_audio_recording():
    hal = HAL()
    
    try:
        print("Starting 5 second recording...")
        hal.audio.start_recording(sample_rate=44100, format="wav", channels=1)
        time.sleep(5)
        
        print("Stopping recording...")
        hal.audio.stop_recording()
        
        # Get the recording
        print("Getting recorded audio...")
        audio_data, format_type, timestamp = hal.audio.get_recording()
        
        # Play locally
        print("Playing recording locally...")
        audio_buffer = io.BytesIO(audio_data)
        sample_rate, audio_array = wavfile.read(audio_buffer)
        sd.play(audio_array, sample_rate)
        sd.wait()
        
        # Upload and play on device
        print("Uploading audio for device playback...")
        response = hal.audio.upload_file(audio_data, format_type)
        
        if response['success']:
            print("Playing back on device...")
            hal.audio.play(response['audio_id'], volume=0.8)
            time.sleep(1)
        else:
            print("Failed to upload audio")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        hal.close()

if __name__ == "__main__":
    test_audio_recording()
