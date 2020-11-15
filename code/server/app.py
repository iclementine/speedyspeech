from flask import Flask, render_template, request, url_for
import numpy as np
from scipy.io.wavfile import write


sample_rate = 22050;

class SpeedySpeech:
    def __init__(self, sample_rate=sample_rate, bit_depth=16):
        self.sample_rate = 16000
        self.bit_depth = 16

    def synthesize(self, input_text):
        data = np.random.uniform(-1, 1, self.sample_rate * 5)  # 5 seconds of noise
        data = np.int16(data / np.max( np.abs(data) ) * (2 ** self.bit_depth - 1))
        return data

speedyObject = SpeedySpeech()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getData')
def getData():
    return 'Hello World';

@app.route('/user/<username>')
def profile(username):
    return username;



@app.route('/synthesize/<text>',methods=['POST'])
def synthesize(text):
    waveform_integers = speedyObject.synthesize(text)
    return np.array2string(waveform_integers, separator=',');
    # write('AudioFromNumpy.wav', sample_rate, waveform_integers)
    # return 'Finished with : ' + input_text
    # synthesize audio from text and return audio
    # this endpoint expects input text

if __name__ == '__main__':
    app.run(debug=True)
