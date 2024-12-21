from flask import Flask, render_template, request

app = Flask(__name__)

web_title = "Halaman Utama"

@app.route("/")
def utama():
    return render_template('home.html', data="Hello Wut Wut")


@app.route("/usia", methods=['GET', 'POST'])
def usia():
    if request.method == 'POST':
        tahun_lahir = int (request.form['tahun_lahir'])
        tahun_sekarang = 2024
        usia = tahun_sekarang - tahun_lahir
        return render_template('about.html', usia = usia)

    return render_template('about.html', usia=None)
