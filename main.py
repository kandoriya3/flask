from flask import Flask, request, render_template, send_file
import rembg

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the uploaded file
        file = request.files['file']
        # remove the background of the image
        output_file = rembg.remove_background(file)
        # create a response object with the output image as the attachment
        response = make_response(send_file(output_file, as_attachment=True, attachment_filename='output.jpg'))
        return response
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
