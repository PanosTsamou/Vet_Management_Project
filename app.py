from flask import Flask, render_template

from controllers.pets_controller import pets_blueprint
from controllers.owners_controller import owners_blueprint

app = Flask(__name__)

app.register_blueprint(pets_blueprint)
app.register_blueprint(owners_blueprint)

@app.route('/')
@app.route('/home')
def home():
    return render_template('mvp/home.jinja')

if __name__ == '__main__':
    app.run(debug=True)