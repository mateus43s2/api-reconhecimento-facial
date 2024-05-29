import unittest
class TestGeral(unittest.TestCase):
    from flask import Flask, render_template, redirect, url_for
    import subprocess
 
    app = Flask(__name__)

    @app.route('/')
    def index():
     return render_template('index.html')
    @app.route('/run-scan', methods=['POST'])
    def run_scan():
       subprocess.run(['python', 'facial2.py'])
       return redirect(url_for('index'))
    if __name__ == '__main__':
       app.run(debug=True)
