from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/')
def home():
    return render_template(
        'index.html',
        appointments=appointment
    )

@app.route('/book', methods=['POST'])
def book():
    appointments.append({
        'name': request.form['name'],
        'doctor': request.form['doctor'],
        'date': request.form['date']
    })

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)