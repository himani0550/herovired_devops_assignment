from flask import Flask
app=Flask(__name__)
@app.route('/', methods=['GET'])
def helloWorld():
    print("hi u there")
@app.route('/aboutus', methods=['GET'])
def hello():
    print ("welcome back")
if __name__=="__main__":
    app.run(port=3000,debug='True')