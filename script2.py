import datetime
from flask import Flask, render_template,request
app = Flask(__name__,template_folder='.')
@app.route("/date", methods=['GET','POST'])
def date_example():
    
    if request.method=="POST":
        
        # get date
        form_date = request.form.get('date') # in format 2012-10-25 or in Python String formatting %Y-%m-%d

        # get time
        # form_time = request.form.get('time') # in format 24 hour, eg 1:30PM = 13:30
        
        # create Python date from form_date and form_time. We use the python datetime string formmatting to describe how the date is built YYYY-MM-DD HH:MM

        date = datetime.datetime.strptime(form_date  ,"%Y,%m,%D" )
        
        # create your database document
        # this is an example model
        # mydoc = models.Mydata()
        # mydoc.date = date  # save date to the 'date' field
        # mydoc.save()
        
        return "The submitted date  is %s" % str(date)
        
    else:
        
        return render_template("index.html")