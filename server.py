"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = [
  'terrible', 'special','trash', 'not cool', 'creepy', 'awful', 'SHIT!!!']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    <a href="http://localhost:5000/hello">Hello page</a>
    </html>"""
    


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    diss_options = ""
    for diss in DISS:
      diss_options += f'<option value="{diss}">{diss.title()}</option>'

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <div>
          Chooose compliments: <select name="compliment">
            <option value="special">Special</option>
            <option value="beautiful">Beautiful</option>
            <option value="important">Important</option> 
          <br>
          <input type="submit" value="Submit"><br>
        </form>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <div>
          Chooose diss: <select name="diss">
            {}
          <br>
          <input type="submit" value="Submit"><br>
        </form>
      </body>
      
   
    
    </html>
    """.format(diss_options)


@app.route("/greet", methods=["GET"])
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! You think you're {}?
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss", methods =["GET"])
def diss_person():
    player = request.args.get("person")
    diss = request.args.get("diss")
    
    #diss = choice(DISS)

    return """
      <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! You're {}!!!
      </body>
    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
