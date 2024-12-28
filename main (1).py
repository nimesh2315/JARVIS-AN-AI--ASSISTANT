import time
from http import client

import speech_recognition as sr
import os
import datetime
import webbrowser
import random
import openai
from config import api_data


def ai(prompt):
    openai.api_key = api_data
    text = f"Openai response for prompt: {prompt}\n ************\n\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response["choices"][0]["message"]["content"]
        print(response_text)
        text += response_text
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    file_path = f"Openai/prompt-{random.randint(1, 68719231)}.txt"
    try:
        with open(file_path, "w") as f:
            f.write(text)
        print(f"Response saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "Sorry, my speech service is down."
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return "Listening timed out"
        except Exception as e:
            print(f"Error: {e}")
            return "Some error occurred from JARVIS"

if __name__ == '__main__':
    print('Hello Good Morning everyone ,  I am JARVIS, An A. I. Assistant')
    say(" Hello Good Morning everyone, I am JARVIS, an A. I. Assistant")
    while True:
        query = takeCommand()
        say(query)
        if query.lower() in ["exit", "quit", "stop"]:
            say("Goodbye , see you soon!")
            break
        sites = ["YouTube", "Google", "Facebook","Instagram","Wikipedia" ]
        for site in sites:
            if f"Open {site}".lower() in query.lower():
                say(f"Opening {site}")
                webbrowser.open(f"https://{site.lower()}.com")

        if "play music" in query:
            musicPath = "/Users/mrityunjaykumar/Downloads/india.mp3"
            os.system(f"open {musicPath}")

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        if "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        time.sleep(0.6)  # Add a short delay to avoid tight loops
