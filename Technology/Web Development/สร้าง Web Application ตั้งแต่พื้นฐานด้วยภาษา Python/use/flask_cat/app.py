from flask import Flask, request, render_template
import os

app = Flask(__name__)
template_folder = os.path.join(os.path.dirname(__file__), "templates/")
app.static_folder = 'static'
app.static_url_path = '/static'
# localhost:5000/static/cat.jpg

names = ["Sarina Mills",
         "Verity Ryder",
         "Minnie Hahn",
         "Tadhg Parks",
         "Tommie Harding",
         "Keanan Wynn",
         "Elaina Dalton",
         "Zi Wormald",
         "Hallam Regan",
         "Stephen Metcalfe"]

@app.route("/names", methods=['GET'])
def get_all_names():
    return render_template('names.html', names=names)

@app.route('/cat_image', methods=["GET"])
def shot_cat_image():
    return render_template('album.html')

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/post', methods=["POST"])
def post():
    return "post method"

@app.route('/query', methods=["POST"])
def query():
    name = request.args.get("name")
    return "name is " + name

@app.route('/form', methods=["POST"])    
def form_data():
    name=  request.form.get("name")
    age=  request.form.get("age")

    return name + "is " + str(age) + 'year old'

@app.route('/user/<user_id>', methods=['POST'])
def get_user(user_id):
    return user_id



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)