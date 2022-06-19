from cmath import sqrt
import scipy.stats as st
import time
from sklearn.preprocessing import scale

question_0 = input("Que desea calcular: media poblacional con varianza conocida, media poblacional con varianza desconocida, varianza poblacional ó contraste parametrico: ")

def media_poblacional_dt_poblacional():
    question_2 = int(input("Indique el tamaño de la muetra: "))
    question_5 = float(input("Media de la muestra: "))
    question_6 = float(input("Desviación típica de la población: "))
    brazo_izquierdo = (question_5 - 1.96*(question_6/sqrt(question_2)))
    brazo_derecho = (question_5 + 1.96*(question_6/sqrt(question_2)))
    solution_1 = [brazo_izquierdo.real, brazo_derecho.real] #REDONDEARLO
    return print(solution_1)

def media_poblacional_dt_muestra():
    question_2 = int(input("Indique el tamaño de la muetra: "))
    question_5 = float(input("Media de la muestra: "))
    question_7 = float(input("Desviación típica de la muestra: "))
    varianza_muestral = question_7*question_7
    cuasivarianza = (varianza_muestral*question_2)/(question_2 - 1)
    cuasidesviacion_tipica = ((sqrt(cuasivarianza))).real
    standard_error = (cuasidesviacion_tipica/sqrt(question_2)).real
    solution_2 = st.t.interval(alpha=0.95, df= question_2 - 1, loc = question_5,scale = standard_error ) 
    return print(solution_2)

def varianza_poblacional():
    question_2 = int(input("Indique el tamaño de la muetra: "))
    question_7 = float(input("Desviación típica de la muestra: "))
    varianza_muestral = question_7*question_7
    cuasivarianza = (varianza_muestral*question_2)/(question_2 - 1)
    cuasidesviacion_tipica = ((sqrt(cuasivarianza))).real
    standard_error = (cuasidesviacion_tipica/sqrt(question_2)).real
    brazo_izquierdo = (((question_2 - 1)*cuasivarianza)/st.chi2.ppf(q=0.95, df = (question_2 - 1)))
    brazo_derecho = (((question_2 - 1)*cuasivarianza)/st.chi2.ppf(q=0.05, df = (question_2 - 1)))
    return print(brazo_izquierdo, brazo_derecho)
    
def contraste_paramétrico_dt_poblacional():
    question_8 = float(input("¿Que media poblacional quiere contrastar? "))
    question_5 = float(input("Media de la muestra: "))
    question_6 = float(input("Desviación típica de la población: "))
    question_2 = int(input("Indique el tamaño de la muetra: "))
    estadistico = (question_5 - question_8)/(question_6/sqrt(question_2))
    #region_critica = 1.96 # Nivel de confianza del 95%
    region_critica_cola = ["izquierda, derecha, ambas"]
    question_9 = input("Indique la región crítica: izquierda, derecha u ambos: ")
    if question_9 == "izquierda":
        if estadistico <= -1.96 :
            print("Con un 95 por ciento de confianza que NO es la media poblacional")
        else :
            print("Con un 95 por ciento de confianza que es la media poblacional")
    elif question_9 == "ambos" or "derecha" :
        if abs(estadistico ) >= 1.96:
            print("Con un 95 por ciento de confianza que NO es la media poblacional")
        else:
            print("Con un 95 por ciento de confianza que es la media poblacional")
            
    else:
        print("Please an error has ocurred; Check the python file")
    
if question_0 == "media poblacional con varianza conocida":
    media_poblacional_dt_poblacional()
elif question_0 == "media poblacional con varianza desconocida":
    media_poblacional_dt_muestra()
elif question_0 == "varianza poblacional":
    varianza_poblacional()
elif question_0 == "contraste parametrico":
    contraste_paramétrico_dt_poblacional()
else :
    time.sleep(2)
    print("ERROR: NO SE HA INDICADO BIEN QUE SE DESEA CALCULAR")
