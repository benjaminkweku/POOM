from flask import Flask, render_template, redirect, url_for
#from flask import Flask, render_template
from flask import request
import requests
# from gpiozero import LED

app=Flask(__name__)

@app.route('/on',methods=["GET","POST"])
def light_on():
    requests.get('http://169.254.203.24:5000/on')
    return redirect(url_for('index'))


        #if request.method=='POST':
            #search_on=request.form.get['box1']
            #elif search_on=="on" or "light off" or "off light":
                    #requests.get('http://169.254.203.24:5000/on/off')

            #else:
                    #print('hello')
              
                       
@app.route('/on/off',methods=["GET","POST"])
def light_off():
  
    requests.get('http://169.254.203.24:5000/on/off')
    return redirect(url_for('index'))


@app.route('/motor',methods=["GET","POST"])
def motor():
    requests.get('http://169.254.203.24:5000/motor')
    return redirect(url_for('index'))

@app.route('/',methods=["GET","POST"])
def index():

    #if request.method=="POST":
           # search_on=request.form['box1']
            #if search_on=="light on" or "on" or "on light":
               # text="The light is on"
               # return redirect(url_for("https://169.254.203.24:5000/on"))
            #elif search_on=="light off" or "off light" or "off":
                #return redirect(url_for("https://192.168.43.224:5000/off"))
            #else:
                #results="invalid syntax.please try again"
                #return results
  
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')