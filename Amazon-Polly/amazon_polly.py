import boto3

polly = boto3.client('polly')

# Use Amazon Polly to convert text to speech
res = polly.synthesize_speech(
    Text = "Hello, how are you?",
    OutputFormat = 'mp3',
    VoiceId = 'Joanna')

# Save the response from Amazon Polly into the mp3 file
audiofile = 'myaudio.mp3'
file = open(audiofile, 'wb')
file.write(res['AudioStream'].read())
file.close()

# Play the mp3 file
import IPython
IPython.display.Audio(audiofile)