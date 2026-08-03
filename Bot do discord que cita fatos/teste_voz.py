import pyttsx3

engine = pyttsx3.init()

voz_portugues = (
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens"
    r"\TTS_MS_PT-BR_MARIA_11.0"
)

engine.setProperty("voice", voz_portugues)
engine.say("Olá. Esta frase deve ser falada em português pela voz Maria.")
engine.runAndWait()

engine.stop()