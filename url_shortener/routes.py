from flask import Blueprint, render_template, request, redirect
from .models import LinkUrl
from .extensions import db

short_blp = Blueprint('short_blp', __name__)


@short_blp.route('/<short_url>')
def redirect_to(short_url):
    link_w = LinkUrl.query.filter_by(short_url=short_url).first_or_404()
    return redirect(link_w.original_url)


@short_blp.route('/')
def index():
    return render_template('index.html')


@short_blp.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    link = LinkUrl(original_url=original_url)
    db.session.add(link)
    db.session.commit()
    return render_template('link_added.html', 
                           new_url=link.short_url, 
                           original_url=link.original_url)


@short_blp.errorhandler(404)
def page_not_found(e):
    return '', 404
