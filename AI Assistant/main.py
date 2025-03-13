import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    print("Warning: Only one voice available.")

def talk(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user input and recognize speech."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for background noise
            voice = listener.listen(source, timeout=5)  # Timeout after 5 seconds
            command = listener.recognize_google(voice).lower()
            
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print("Command:", command)
            return command
    except sr.UnknownValueError:
        talk("I couldn't understand, please say that again.")
        return ""
    except sr.RequestError as e:
        talk("There was an issue with the recognition service.")
        print(f"Speech recognition error: {e}")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

# Define command functions
def play_song(command):
    """Play a song on YouTube."""
    song = command.replace('play', '').strip()
    talk(f'Playing {song}')
    try:
        pywhatkit.playonyt(song)
    except Exception:
        talk("I couldn't play the song. Check your internet connection.")

def tell_time(command):
    """Tell the current time."""
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f'Current time is {time}')

def search_wikipedia(command):
    """Fetch a summary from Wikipedia."""
    person = command.replace('who is', '').replace('tell me about', '').strip()
    try:
        info = wikipedia.summary(person, sentences=1)
        talk(info)
    except wikipedia.exceptions.PageError:
        talk("Sorry, I couldn't find any information on that.")
    except wikipedia.exceptions.DisambiguationError:
        talk("There are multiple results, please be more specific.")

def tell_joke(command):
    """Tell a joke."""
    talk(pyjokes.get_joke())

def tell_date(command):
    """Respond humorously when asked for a date."""
    talk("Sorry, I have a headache.")

def relationship_status(command):
    """Respond to a relationship query."""
    talk("I am in a relationship with WiFi.")

def exit_program(command):
    """Exit the program."""
    talk("Goodbye!")
    exit()

# Command dictionary (dispatch table)
commands = {
    'play': play_song,
    'time': tell_time,
    'who is': search_wikipedia,
    'tell me about': search_wikipedia,
    'joke': tell_joke,
    'date': tell_date,
    'are you single': relationship_status,
    'exit': exit_program,
    'stop': exit_program
}

def run_alexa():
    """Process user commands dynamically."""
    command = take_command()
    if not command:
        return
    
    print("Processing:", command)

    # Match the command with the available functions
    for key in commands:
        if key in command:
            commands[key](command)
            return

    # If no command is recognized
    talk("I didn’t get that. Try saying commands like play a song, tell me the time, or tell a joke.")

if __name__ == "__main__":
    print("Starting Alexa-like assistant... Say 'exit' to stop.")
    while True:
        try:
            run_alexa()
        except KeyboardInterrupt:
            talk("Goodbye!")
            break
        except sr.RequestError:
            talk("I am unable to access the speech recognition service.")
        except sr.UnknownValueError:
            talk("Sorry, I couldn't understand.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            talk("An error occurred. Please try again.")