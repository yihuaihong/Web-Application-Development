import flask
from flask import request,redirect
app = flask.Flask(__name__, template_folder='templates')
from model.pycorrector import en_spell
from model.poetry_generator.dataset import tokenizer
from model.poetry_generator.model import model
from model.poetry_generator import settings
from model.poetry_generator import utils
from pycorrector.seq2seq.seq2seq_corrector import Seq2SeqCorrector

# 加载训练好的模型
model.load_weights(settings.BEST_MODEL_PATH)

@app.route('/predict', methods=['POST'])
def predict():

    text = request.form.get('message')

    # 随机生成一首诗
    prediction= utils.generate_random_poetry(tokenizer, model)

    return flask.render_template('html/result.html', prediction=prediction)

@app.route('/predict1', methods=['POST'])
def predict1():

    text = request.form.get('message')

    # 给出部分信息的情况下，随机生成剩余部分
    prediction=utils.generate_random_poetry(tokenizer, model, s=text+'，')


    return flask.render_template('html/result.html', prediction=prediction)

@app.route('/predict2', methods=['POST'])
def predict2():

    text = request.form.get('message')

    # 生成藏头诗
    prediction=utils.generate_acrostic(tokenizer, model, head=text)


    return flask.render_template('html/result.html', prediction=prediction)

@app.route('/correct2', methods=['POST'])
def correct2():

    text = request.form.get('message')
    m = Seq2SeqCorrector()
    error_sentences=[text]
    res = m.seq2seq_correct(error_sentences)


    return flask.render_template('html/correct2.html', correct_words= res[0][0] ,original_words=text,details=res[0][1])

@app.route('/correct')
def correct():

    return flask.render_template('html/correct.html')

@app.route('/about')
def about():
    return flask.render_template('html/about.html')



@app.route('/en_correct')
def en_correct():

    return flask.render_template('html/en_correct.html')


@app.route('/en_correct2', methods=['POST'])
def en_correct2():
    text = request.form.get('message')
    enspell = en_spell.EnSpell()
    corrected_text, details = enspell.correct(text)
    print(text, '=>', corrected_text)

    return flask.render_template('html/en_correct2.html', correct_words= corrected_text ,original_words=text,details=details)


@app.route('/')
def main():
    return(flask.render_template('html/about.html'))
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1600,threaded=False)


