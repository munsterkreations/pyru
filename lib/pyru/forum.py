# forum.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    # Code to handle the question and provide a response
    return 'Response to the question'

if __name__ == '__main__':
    app.run(debug=False)


