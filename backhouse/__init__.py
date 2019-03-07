from flask import Flask
from backhouse.models import db, Activity, Category
import datetime

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object("config.default")

# Load the configuration from the instance folder
app.config.from_pyfile("config.py")

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar("APP_CONFIG_FILE")


db.init_app(app)


@app.route("/")
def test():
    activities = Activity.query.all()
    for a in activities:
        print(a.duration())
    return activities[0].start.strftime("%m/%d/%Y, %H:%M:%S")


@app.route("/new")
def test_new():
    c = Category.query.filter_by(name='Training').first()
    a = Activity(c)
    return a.category.name


@app.cli.command("initdb")
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    print("Initialized the database.")


@app.cli.command("bootstrap")
def bootstrap_command():
    """Creates initial data."""
    c = Category("Cat0")
    db.session.add(Category("Cat1"))
    db.session.add(c)
    db.session.add(Category("Cat2"))
    db.session.add(Category("Cat3"))
    db.session.add(Category("Cat4"))
    db.session.add(Category("Cat5"))
    db.session.add(Category("Cat6"))
    db.session.add(Category("Cat7"))

    db.session.add(Activity(c))

    db.session.commit()
