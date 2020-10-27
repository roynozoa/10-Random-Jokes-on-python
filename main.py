# Python 10 random jokes
# thanks to random joke API (https://github.com/15Dkatz/official_joke_api)
# make API call and working with json object
# using python text to speech library (pyttsx3)

# implementing with python text to speech library (pyttsx3 v2.71)
# installing pyttsx3 : pip3 install pyttsx3==2.71

# import library
import json
import pyttsx3
from urllib import request
from jokes import Jokes  # import Jokes class from joke.py


url = "http://official-joke-api.appspot.com/jokes/ten"
req = request.urlopen(url)
# print(req.getcode())  # print the code
data = req.read()
json_data = json.loads(data)  # load a json file, json_data is dict data type
tts = pyttsx3.init()  # initialize pyttsx3
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)  # change voices to female


# ================ MAIN PROGRAM ====================
# ==================================================
print("======= Python 10 Random Jokes =======")

jokes_list = []  # create an empty jokes list


# for loop put jokes from json intu Jokes class and append to jokes list
for j in json_data:
    joke_type = j['type']
    setup = j['setup']
    punchline = j["punchline"]
    new_joke = Jokes(joke_type, setup, punchline)
    jokes_list.append(new_joke)


# for loop printing joke from jokes list
num_joke = 0
for joke in jokes_list:
    num_joke += 1
    print(f'[{num_joke}]')
    print(joke)
    tts.say("Setup")
    tts.say(joke.setup)
    tts.say("Punchline")
    tts.say(joke.punchline)
    tts.runAndWait()


tts.say("That is the end of the code")
tts.runAndWait()
