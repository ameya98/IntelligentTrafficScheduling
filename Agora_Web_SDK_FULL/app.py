from flask import request, Flask, render_template, jsonify
from base64 import b64decode
import car_detection
import signalModel

app = Flask(__name__)


# main screen!
@app.route('/')
def main_screen():
    return render_template('index.html')


@app.route('/saveimage', methods=['POST'])
def save_image():
    data = request.form
    img_data = data['img64']
    index_data = data['index']

    # # write base64 string to file
    # with open("b64.txt", "w") as fh:
    #     fh.write(img_data)

    # strip POST headers
    img_data = img_data[img_data.find(",") + 1:]
    with open("savedimages/lane" + str(index_data) + ".png", "wb") as fh:
        fh.write(b64decode(img_data.encode('utf-8')))

    lanedetails = car_detection.carcount()

    # car_detection.carcount() should return a dict of the form
    # { "1": n1, "2": n2 }

    signals.updateSignals(lanedetails)
    signals.refreshSignals()
    return "saved file"


@app.route('/trafficsignals/<index>')
def traffic_logic_lane1(index):
    return render_template("traffic_signals" + index + ".html")


@app.route('/getsignaldata')
def get_signals():
    # routing logic in signalModel
    signal_states = {key: signals.getLightStatus(key) for key in signals.signal}
    return jsonify(signal_states)


if __name__ == '__main__':
    signals = signalModel.TrafficJunction()
    app.run(debug=True, host='192.168.15.158', ssl_context='adhoc')
