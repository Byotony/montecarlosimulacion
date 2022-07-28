from flask import Flask, render_template, request
    
import numpy as np
import pandas as pd

from pandas import ExcelWriter
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import io
from io import BytesIO
import base64    

arranque = Flask(__name__)


@arranque.route("/")
def inicio():
    return render_template("montecarlo.html")


@arranque.route("/montecarloejemplo")
def montecarloejemplo():
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import io
    import base64
    datos = pd.DataFrame()
    demanda = [100, 200, 300, 400, 500, 600]
    probabilidad = [0.15, 0.25, 0.18, 0.22, 0.13, 0.07]
    datos["DEMANDA"] = demanda
    datos["PROBABILIDAD"] = probabilidad
    data = datos.to_html(classes="table table-hover table-striped",
                   justify="justify-all", border=0)
    buf = io.BytesIO() ##
    plt.plot(datos)
    fig = plt.gcf()
    canvas = FigureCanvasAgg(fig)##
    canvas.print_png(buf)##
    fig.clear()##
    plot_url = base64.b64encode(buf.getvalue()).decode('UTF-8')##


    a1= np.cumsum(datos["PROBABILIDAD"]) #Cálculo la suma acumulativa de las probabilidades
    x2=datos
    x2['FPA'] =a1
    data2 = x2.to_html(classes="table table-hover table-striped",
                   justify="justify-all", border=0)

   
    x2['Min'] = x2['FPA']
    x2['Max'] = x2['FPA']
    x2
    data3 = x2.to_html(classes="table table-hover table-striped",
                   justify="justify-all", border=0)


    
    lis = x2["Min"].values
    lis2 = x2['Max'].values
    lis[0]= 0
    for i in range(1,6):
        lis[i] = lis2[i-1]
        print(i,i-1)
    x2['Min'] = lis
    data4 = x2.to_html(classes="table table-hover table-striped",
                   justify="justify-all", border=0)


    datos2 = pd.DataFrame()
    ri = [0.11, 0.44, 0.90, 0.52, 0.00, 0.54, 0.56, 0.66, 0.52, 0.46, 0.24, 0.31, 0.48, 0.03, 0.50, 0.65, 0.80, 0.74, 0.32, 0.66]
    datos2 ["ri"] = ri
    data5 = datos2.transpose().to_html(classes="table table-hover table-striped",
                   justify="justify-all", border=0)



    max = x2 ['Max'].values
    min = x2 ['Min'].values
    datosv1= []
    simu=pd.DataFrame()
    for a in range(len(datos2)):
        for b in range(len(x2)):
            if(datos2["ri"][a]>=x2["Min"][b] and datos2["ri"][a]<x2["Max"][b]):
                datosv1.append(x2["DEMANDA"][b])
    simu["ri"]=datos2["ri"]
    simu["DEMANDA"]=datosv1
    data6 = simu.transpose().to_html(classes="table table-hover table-striped",
                   justify="justify-all", border=0)


    x=simu["DEMANDA"].sum()
    promedio=x/28
    
    data7 = promedio


    return render_template('montecarloejemplo.html',data=data,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,image=plot_url)


if __name__ == '__main__':
    arranque.run(port=5000,debug=True)