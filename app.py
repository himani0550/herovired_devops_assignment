from flask import Flask
app=Flask(__name__)
@app.route('/', methods=['GET'])
def helloWorld():
    return'helloworld'
@app.route('/aboutus', methods=['GET'])
def helloWorld():
    return'welcome back'
if __name__=="__main__":
    app.run(port=3000,debug='True')