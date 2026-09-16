#here this not full code it's just how to connect flask and backend code 

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
