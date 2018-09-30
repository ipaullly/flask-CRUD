from flask import Flask, request, redirect, url_for, render_template
from student import Student

app = Flask(__name__)

students = []

if __name__ == '__main__':
    app.run(debug=True)