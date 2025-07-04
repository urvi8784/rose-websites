from flask import Flask
from roses.routes import roses

app = Flask(__name__)
app.register_blueprint(roses)

if __name__ == "__main__":
    app.run(debug=True)
