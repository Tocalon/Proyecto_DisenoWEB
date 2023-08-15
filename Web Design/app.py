from flask import Flask, render_ template
app=Flask(__name__)


Properties=[
    {
        "ID": 1, 
        "Name" : "Mojo Dojo Casa House",
        "Location": "Santa Ana", 
        "Price" : "$500,000", 
    },
    
    {
        "ID": 2, 
        "Name" : "Dream House",
        "Location": "Escazu ", 
        "Price" : "$450,000",      
    },
    
    {
        "ID": 3, 
        "Name" : "Real House",
        "Location": "Heredia ", 
        "Price" : "$350,000",      
    }
]

@app.route("/")
def aceboProperties(): 
    return render_template("webdesign.html", 
                           propertie=Properties)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)