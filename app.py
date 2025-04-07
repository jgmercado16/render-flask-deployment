from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    gender = request.form.get('gender')
    age = request.form.get('age')
    gmail = request.form.get('gmail')

    return render_template(
        'thanks.html',
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        age=age,
        gmail=gmail
    )

if __name__ == '__main__':
    app.run(debug=True)