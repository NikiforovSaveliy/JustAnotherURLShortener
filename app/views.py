import json

from flask import redirect, Response, request, render_template, send_from_directory

from app import app
from .models import Link
from .utils import generate_slug, validate_url


@app.route('/api/generate_short_url', methods=['POST'])
def get_short_url():
    """This view generate slug and returning short url"""
    url = request.get_json().get('url')
    exist_url = Link.get_or_none(Link.long_url == url)
    # FIXME: Check if colussion occured
    if exist_url:
        return str(exist_url)
    if not validate_url(url):
        return Response(status=400, response='no url in request')

    link = Link.create(long_url=url, short_url=generate_slug())
    return app.response_class(response=json.dumps({'url': str(link)}),
                              mimetype='application/json',
                              status=201)


@app.route('/<url>')
def redirect_to_original(url):
    """This view redirrect currently to original website"""
    original_link = Link.get_or_none(Link.short_url == url)
    if original_link:
        return redirect(original_link.long_url)
    return redirect('/not_found')


@app.route('/')
def main_page():
    """main page of web app"""
    return render_template('index.html')


@app.route('/not_found')
def not_found_page():
    """page which occured if url is not in database"""
    return render_template('not_found_page.html')


@app.route('/css/<file_name>')
def css_retrieve(file_name):
    """This view for retrieve files from static directory"""
    return send_from_directory('statics/css', file_name)
