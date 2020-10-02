from url_shortener.models import LinkUrl,db
from url_shortener import create_app
def test_sample_url():
    """This will create a dummy URL in the db and checks it"""
    flask_app=create_app(config_file='settings.py')
    context=flask_app.app_context()
    context.push()
    db.create_all()
    link=LinkUrl(original_url="https://google.com")
    db.session.add(link)
    db.session.commit()
    assert db
    db.drop_all()