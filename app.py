from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import emoji
import joblib  
app = Flask(__name__)

model1=pickle.load(open('croprecomd.pkl','rb'))
#model1=joblib.load("croprecomd.pkl")

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(float(x)) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model1.predict(final)
    output='{}'.format(prediction[0])
    if (output == str(1)):
        return render_template('index.html',pred='Recommended crop is PADDY ')
    elif (output == str(2)):
        return render_template('index.html',pred='Recommended crop is COTTON')  
    elif (output == str(3)):
        return render_template('index.html',pred='Recommended crop is MAIZE') 
    elif (output == str(4)):
        return render_template('index.html',pred='Recommended crop is MANGO') 
    elif (output == str(5)):
        return render_template('index.html',pred='Recommended crop is APPLE') 
    elif (output == str(6)):
        return render_template('index.html',pred='Recommended crop is WATERMELON ') 
    elif (output == str(7)):
        return render_template('index.html',pred='Recommended crop is BLACKGRAM') 
    elif (output == str(8)):
        return render_template('index.html',pred='Recommended crop is BANANA') 
    elif (output ==str(9)):
        return render_template('index.html',pred='Recommended crop is GRAPES') 
    elif (output == str(10)):
        return render_template('index.html',pred='Recommended crop is COCONUT') 
    else:
        return render_template('index.html',pred='Check Your Parameters'); 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=144)
