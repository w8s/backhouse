from backhouse.models import db
import datetime
from dateutil.relativedelta import relativedelta


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship(
        "Category", backref=db.backref("activities", lazy="select"), lazy="joined"
    )

    def __init__(self, cat):
        self.start = datetime.datetime.now()
        self.category = cat

    def duration(self):
        try:
            return relativedelta(self.end, self.start)
        except:
            return -1
