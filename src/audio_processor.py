import tempfile
import os
from typing import Tuple

try:
    from pydub import AudioSegment
    import speech_recognition as sr
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False

class AudioProcessor:
    def __init__(self):
        self.available = AUDIO_AVAILABLE
        if self.available:
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 300
    
    def transcribe_audio(self, audio_path: str) -> Tuple[str, str]:
        """Transcribe audio to text using Google Speech Recognition"""
        if not self.available:
            return "Audio processing not available", ""
        
        temp_path = None
        try:
            # Convert to WAV format
            sound = AudioSegment.from_file(audio_path)
            temp_path = tempfile.mktemp(suffix=".wav")
            sound.export(temp_path, format="wav")
            
            # Speech recognition
            with sr.AudioFile(temp_path) as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.record(source)
            
            text = self.recognizer.recognize_google(audio, language='en-US')
            return text, "Success"
            
        except sr.UnknownValueError:
            return "", "Could not understand audio"
        except sr.RequestError as e:
            return "", f"Speech service error: {str(e)}"
        except Exception as e:
            return "", f"Audio processing error: {str(e)}"
        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
                except:
                    pass
