from flask import Flask, render_template, request, make_response
import numpy as np
from scipy.io.wavfile import write
from io import BytesIO

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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/synt/<text>',methods=['GET'])
def synt(text):
    buf = BytesIO()
    waveform_integers = speedyObject.synthesize(text)
    write(buf, sample_rate, waveform_integers)
    response = make_response(buf.getvalue())
    buf.close()
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'
    return response;




if __name__ == '__main__':
    app.run(debug=True)
