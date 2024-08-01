import speech_recognition as sr
import pyttsx3
import tkinter as tk
import time
# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()  # Experiment with different recognizers
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Adjust speaking rate

# Function to store text in a file
def store_output(text, filename="output.txt"):
    with open(filename, "a") as file:
        file.write(text + "\n")

# Function to speak and store text
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()
    store_output(command + " (spoken)")

# Create the UI window
root = tk.Tk()
root.title("Speech Recognition")

# Label to display recognized text
label = tk.Label(root, text="Listening...")
label.pack()

# Main loop for continuous listening
while True:
    try:
        # Listen for audio input
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)  # Increased duration
            audio = r.listen(source, timeout=5)  # Set timeout

        # Recognize and format text
        MyText = r.recognize_google(audio)  # Experiment with recognizers
        MyText = MyText.lower()

        # Print and speak recognized text
        print("Input Voice:",MyText)
        robot_voice="Did you say "+ MyText
        print(robot_voice)
        SpeakText(robot_voice)

        # Store recognized and spoken text
        store_output(MyText + " (recognized)")

        # Update UI label only when necessary
        label.config(text= MyText)

        time.sleep(1)
        

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        label.config(text="Error: Could not request results")
    except sr.UnknownValueError:
        print("Unknown error occurred")
        label.config(text="Error: Unknown error occurred")

    # Update the UI window
    root.update()

    # Run the UI mainloop
    root.mainloop()


