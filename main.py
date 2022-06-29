import gattu


from google.cloud import speech

#client key for access to google text to speech
client = speech.SpeechClient.from_service_account_file('Hand.json')

#name of first audio file
file_name = r"C:\Users\rzark\PycharmProjects\pythonProject\recording1.wav"



#opens audio file already (file_name) in "rb" mode
#"rb" mode = reading binary
with open(file_name, 'rb') as f:
     byte_data_wav = f.read()

#mp3_data = binary reading of audio file
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

#configs API speech recognision hz, punctuation, and language
config = speech.RecognitionConfig(
     sample_rate_hertz=44100,
     enable_automatic_punctuation=False,
     language_code="en-US"
 )
config = speech.RecognitionConfig(
     sample_rate_hertz=44100,
     enable_automatic_punctuation=False,
     language_code="en-US",
     audio_channel_count=2
 )

#sets var response = google API transcript
#using settings from config and audio from audio_file
response = client.recognize(
     config=config,
     audio=audio_wav
 )

#writing the result to result.txt
file = open("result.txt", "w")
file.write(str(response))
file = open("result.txt", "r")
#extracting transcript from result.txt
content = file.readlines()
fileOne = content[2]
fileOne = fileOne[17:len(fileOne)-2]
#clearing text file
# file = open("result.txt", "w+")
# file.truncate()
file.close()

