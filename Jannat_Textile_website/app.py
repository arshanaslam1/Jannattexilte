from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/contactus')
def contactus():
    return render_template("/contactus.html")

@app.route('/manufacturing')
def manufacturing():
    return render_template("/manufacturing.html")

@app.route('/products')
def products():
    return render_template("/products.html")

@app.route('/profile')
def profile():
    return render_template("/profile.html")

@app.route('/quality-assurance')
def quality():
    return render_template("/quality-assurance.html")
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])




if __name__ == '__main__':
    app.run()
