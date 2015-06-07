#! /usr/bin/python
# coding=utf-8

# -*- coding:utf-8 -*-

from flask import Flask, request, make_response
from PIL import Image
from StringIO import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return "Le chemin de 'racine' est : " + request.path

@app.route('/la')
def ici():
    return "Le chemin de 'ici' est : " + request.path

@app.route('/discussion')
@app.route('/discussion/page/<int:num_page>')
def mon_chat(num_page = 1):
    premier_msg = 1 + 50 * (num_page - 1)
    dernier_msg = premier_msg + 50
    return 'affichage des messages {} à {}'.format(premier_msg, dernier_msg)

@app.route('/image')
def genere_image():
    mon_image = StringIO()
    Image.new("RGB", (300,300), "#92C41D").save(mon_image, 'BMP')
    reponse = make_response(mon_image.getvalue())
    reponse.mimetype = "image/bmp"  # à la place de "text/html"
    return reponse

@app.route('/404')
def page_non_trouvee():
    reponse = make_response("Cette page devrait vous avoir renvoyé une erreur 404", 404)
    return reponse

@app.errorhandler(404)
def ma_page_404(error):
    return "Ma jolie page 404", 404

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
