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
        # create a response object with the output image as the attachment
        response = make_response(send_file(output_data, as_attachment=True, attachment_filename='output.png'))
        return response
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
