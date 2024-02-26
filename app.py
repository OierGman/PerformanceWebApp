from flask import Flask, render_template, request, send_file
import os
import data

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Check if files were uploaded via the form
    if 'driver_file' in request.files and 'performance_file' in request.files:
        driver_file = request.files['driver_file']
        performance_file = request.files['performance_file']

        # Save the uploaded files to the app folder
        driver_file.save('driver_data.csv')
        performance_file.save('performance_data.csv')

        # Here you can perform further processing if needed
        # For example, you can read the CSV files and perform some analysis
        try:
            data.get_data()
            return render_template('complete.html')
        except:
            return render_template('oops.html')
    else:
        return render_template('oops.html')


@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(os.path.dirname(__file__), 'templates', filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404


if __name__ == '__main__':
    app.run(debug=True)
