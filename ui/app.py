from flask import Flask, render_template, request
from flask import jsonify
import os

# set root path for the project
# os.chdir(os.path.dirname(os.path.abspath( __file__)) + '/../')

app = Flask(__name__, static_url_path="/static")


#############
# Routing
#
@app.route('/message', methods=['POST'])
def reply():
    # return print(request.form['msg'])
    return jsonify({'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'])})


@app.route("/")
def index():
    return render_template("index.html")


#############

'''
Init seq2seq model

    1. Call main from execute.py
    2. Create decode_line function that takes message as input
'''
# _________________________________________________________________
import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')
# _________________________________________________________________

# start app
if (__name__ == "__main__"):
    app.run(debug=True, port=5000)
