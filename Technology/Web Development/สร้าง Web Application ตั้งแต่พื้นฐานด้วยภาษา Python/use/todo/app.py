from glob import glob
from os.path import dirname, join
from uuid import uuid4

from flask import Flask, render_template, request, redirect

from model import db, Card, Items

template_folder = join(dirname(__file__), "templates/")
app = Flask(__name__, template_folder=template_folder)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template("index.html", cards=Card.get_all())


@app.route('/item/check', methods=['POST'])
def check_complete_item():
    body = request.form
    item_id = body.get('item_id')
    print(item_id)
    status = bool(body.get(f'status', type=int))
    print(status, type(status))
    Items.update({Items.completed: status}).where(Items.id == item_id).execute()
    return redirect('/')


@app.route('/card/new', methods=['POST'])
def add_card():
    body = request.form
    cid = str(uuid4())
    Card.create(id=cid, name=body.get('cardName')).save()
    return redirect('/')


@app.route('/item/new', methods=['POST'])
def add_item():
    body = request.form
    cid = body.get('card_id')
    item_name = body.get('name')
    Items.create(name=item_name, card=cid).save()
    return redirect('/')


if __name__ == "__main__":
    db.connect()
    db.drop_tables([Items, Card])
    db.create_tables([Card, Items])
    cid = str(uuid4())
    Card.create(id=cid, name='Test Card').save()
    Items.bulk_create([Items(card_id=cid, name=f"Step-{i}") for i in range(10)])

    extra_files = glob('templates/*')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run("0.0.0.0", 5000, extra_files=extra_files)
