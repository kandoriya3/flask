from flask import Flask, request, render_template, send_file
from rembg import remove

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the uploaded file
        file = request.files['file']
        # remove the background of the image
        input_data = file.read()
        output_data = remove(input_data)
        # display the output image
        return send_file(output_data, mimetype='image/png')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
