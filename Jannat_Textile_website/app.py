from flask import Flask
from flask import render_template
from datetime import date, datetime, timedelta
from flask import make_response, request
from urllib.parse import urlparse

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


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc
    lastmod = date.today() - timedelta(5)
    lastmod = lastmod.strftime('%Y-%m-%d')

    # Static routes with static content
    static_urls = list()
    
    for rule in app.url_map.iter_rules():
        if not str(rule).startswith("/admin") and not str(rule).startswith("/user"):
            if "GET" in rule.methods and len(rule.arguments) == 0:
                url = {
                    "loc": f"{host_base}{str(rule)}"
                }
               
                static_urls.append(url)
                
                

    
    print (static_urls)
    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, host_base=host_base, lastmod = lastmod)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response




if __name__ == '__main__':
    app.run()
