
@app.route("/sitemap.xml")
def sitemap():
    """
        Route to dynamically generate a sitemap of your website/application.
        lastmod and priority tags omitted on static pages.
        lastmod included on dynamic content such as blog posts.
    """
    from flask import make_response, request, render_template
    import datetime
    from urllib.parse import urlparse

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc
    lastmod = datetime.now()
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

    # Dynamic routes with dynamic content
    
    dynamic_urls = list []
    blog_posts = Post.objects(published=True)
    for post in blog_posts:
        url = {
            "loc": f"{host_base}/blog/{post.category.name}/{post.url}",
            "lastmod": post.date_published.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        dynamic_urls.append([url,lastmod])

    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls, host_base=host_base)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response

















    from flask import Flask
from flask import render_template
from datetime import datetime
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




:
    
    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc
    pages = []

    # get static routes
    # use arbitary 10 days ago as last modified date
    lastmod = datetime.now()
    lastmod = lastmod.strftime('%Y-%m-%d')
    for rule in app.url_map.iter_rules():
        # omit auth and admin routes and if route has parameters. Only include if route has GET method
        if 'GET' in rule.methods and len(rule.arguments) == 0 \
                and not rule.rule.startswith('/admin') \
                and not rule.rule.startswith('/auth') \
                and not rule.rule.startswith('/test'):
            url = {
                    "loc": f"{host_base}"
                }
            pages.append(["url" + rule.rule, lastmod])

    


    sitemap_template = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_template)
    response.headers['Content-Type'] = 'application/xml'
    return response



if __name__ == '__main__':
    app.run()

