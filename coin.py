from microdot import Microdot, Response
app= Microdot()
Response.default_content_type ='text/html'

def htmldoc():
    coin_text = "Heads" if coin_state==0 else "Tails"


    html=f'''
    <html>
       <head>
         <title> click to flip coin </title>
         </head>
         <body>
             <div>
                <h1> click to flip coin</title>
                <svg width="200" height= "200" viewbox= "0 0 200 200">
                  <a href="/toggle">
                   <circle fill="green" cx="100" cy="100" r="90"/>
                   <text x="50%" y= "50%" font-size="24" text-anchor="middle" dy=".3em">{coin_text}</text>
                    </a>
                </svg>
            </div>
        </body>
    </html>
    '''

    return html

coin_state=0
import numpy as np
coin_state= np.random.randint(2)

@app.route('/')
def home (request):
    return htmldoc()

@app.route('/toggle')
def toggle_coin(request):
    global coin_state
    coin_state =1 - coin_state
    return htmldoc()

    
app.run(debug=True, port=8008)