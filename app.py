from flask import Flask, render_template, redirect, url_for
from livereload import Server
import markdown

md = markdown.Markdown(extensions=['mdx_wikilink_plus'])
wiki_path = "../tech-services-wiki.wiki"

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return redirect(url_for('load_page', path='home'))

@app.route("/<path:path>")
def load_page(path):
    with open(f"{wiki_path}/{path}.md") as f:
        return md.convert(f.read())

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    # Watch templates and static files for changes
    server.watch('templates/')
    server.watch('static/')
    server.watch('../tech-services-wiki.wiki/')
    server.watch('app.py')
    # Start the server
    server.serve(open_url_delay=True)
