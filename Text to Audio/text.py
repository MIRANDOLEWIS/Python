from gtts import gTTS
from playsound import playsound

language = "en"

sound = gTTS(lang=language,text="hello world",slow=False)

sound.save("welcome.mp3")

playsound("welcome.mp3")
