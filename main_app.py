from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run(debug=True)


