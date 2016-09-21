from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = 'ShhhSneaky'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['fullName']) < 1:
        flash("Name cannot be empty")
        return redirect('/')
    elif len(request.form['comments']) < 1 or len(request.form['comments']) > 120:
        flash("Comments aren't actually optional but keep it under 120 characters!")
        return redirect('/')
    else:
        name = request.form['fullName']
        location = request.form['location']
        language = request.form['language']
        comments = request.form['comments']
        return render_template("result.html", name=name, location=location, language=language, comments=comments)


app.run(debug=True)
