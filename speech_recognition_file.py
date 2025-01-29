#!/usr/bin/env python3
#Program for recognizing English speech and append the recognized text to the file named in the argument
#Output of speech recognizer with espeak text output
#and appending to a file named in the argument
#addition by Gerald Schuller, Sep. 2016
#To avoid alsa error message run with:
#python3  speech_recognition_file.py 2> /dev/null
#Gerald Schuller, February 2024

"""
python speech recognition:
https://pypi.python.org/pypi/SpeechRecognition/
sudo pip install SpeechRecognition
sudo apt install flac
sudo apt install python.pyaudio
sudo apt install espeak
#Eventuell update von pyaudio:
pip show pyaudio
sudo apt-get install portaudio19-dev
sudo apt-get install python-all-dev
sudo pip install --upgrade pyaudio
"""

import speech_recognition as sr
import os
import sys

#Opens file of 1st argument in append mode:
if (len(sys.argv)== 2):
   filename=sys.argv[1]
else:
   filename="recognizedtext.txt"
   
print("filename= ", filename)
textfile=open(filename, "a")

r = sr.Recognizer()
m = sr.Microphone()

try:
    announcement=" Speech-to Text program, recognizer set to German."
    print("\n"+announcement)
    os.system('espeak -ven -s 140 '+'"'+announcement+'"')
    print("End with Control-C after recognizing and while while it is listening again")
    os.system('espeak -ven -s 140 '+'"End with Control-C after recognizing and while it is listening again"')
    print("A moment of silence, please...")
    os.system('espeak -ven -s 140 '+'"A moment of silence, please..."')
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("Ready!")
    #os.system('espeak -ven -s 140 '+'"Ready!"')
    while True:
        print("Listening..")
        os.system('espeak -ven -s 140 '+'"Listening"')
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            #US English:
            #rectext = r.recognize_google(audio)
            #Different Languages:
            #https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
            #List of languages:
            #https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti
            #German:
            rectext = r.recognize_google(audio,language='de-DE')
            
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said: {}".format(rectext).encode("utf-8"))
                #os.system('espeak -ven -s 140 '+'"'+rectext +'"')
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said: {}".format(rectext))
            #First letter in capital letter and in the end add a '.'
            #textfile.write(rectext[0].upper()+rectext[1:]+'. ');
            #Drop the '.' in the end (it recognizes puctuation commands):
            textfile.write(rectext[0].upper()+rectext[1:]+' ');

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            os.system('espeak -ven -s 140 '+'"Please repeat"')
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            os.system('espeak -ven -s 140 '+'"Uh oh! Could not request results from Google Speech Recognition service"')
except KeyboardInterrupt:
    textfile.close()
    print("\nfilename= ", filename)
    print("\nYou said: {}".format(rectext))
    pass
