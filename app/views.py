import json

from flask import redirect, Response, request

from app import app
from .models import Link
from .utils import generate_slug, validate_url


@app.route('/api/generate_short_url', methods=['POST'])
def get_short_url(url):
    """This view generate slug and returning short url"""
    exist_url = Link.get_or_none(Link.long_url == request.get_json().get('url'))
    if exist_url:
        return str(exist_url)
    if not validate_url(url):
        return Response(status=400)

    link = Link(long_url=url, short_url=generate_slug()).save()

    return app.response_class(response=json.dumps({'url': link.__str__()}),
                              mimetype='application/json',
                              status=201)


@app.route('/<url>')
def redirect_to_original(url):
    """This view redirrect currently to original website"""
    original_link = Link.get_or_none(Link.short_url == url)
    if original_link:
        return redirect(original_link.long_url)


@app.route('/')
def main_page():
    return app.response_class(response=json.dumps({'message': 'hello_word'}),
                              mimetype='application/json',
                              status=200)
