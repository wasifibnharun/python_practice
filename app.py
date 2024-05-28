from flask import Flask

app=Flask(__name__)

#creating a route
@app.route('/')
def index():
    return "<h4>This is made using Flask</h4>"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h3>Welcome to NVIT,{name}</h3>"

if __name__=='__main__':
    app.run(debug=True)