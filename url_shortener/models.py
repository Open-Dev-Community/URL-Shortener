from .extensions import db
from datetime import datetime
import string
from random import choices


# Class for logic and linking.
class LinkUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    hits = db.Column(db.Integer, default=0)
    date_origin = db.Column(db.DateTime, default=datetime.now)

    # Initialize class instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_url()

    # Generate short url
    def generate_url(self):
        whole_set = (string.digits 
                     + string.ascii_letters)
        short_url = ''.join(
            choices(
                whole_set, 
                k=3
            )
        )    # Chooses 3 characters. That's how short our URL will be.
        # Make sure the generate url is unique. If not, recurse over this function.
        gen_link = self.query.filter_by(short_url=short_url).first()
        if gen_link:
            return self.generate_url()
        return short_url
