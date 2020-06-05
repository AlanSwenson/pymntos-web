"""this starts our Flask app"""
from pymntos_web import create_app

app = create_app()

if __name__ == "__main__":
    # flask run
    app.run(debug=True)
