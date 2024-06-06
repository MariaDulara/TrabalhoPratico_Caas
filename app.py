from flask import Flask # type: ignore
from routes import init_routes

app = Flask(__name__)
init_routes(app)

if __name__ == "__main__":
 app.run(debug=True)
