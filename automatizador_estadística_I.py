from cmath import sqrt
import scipy.stats as st
import time
from sklearn.preprocessing import scale

question_1 = input("Indique la distribución: normal, binomial o poisson: ")
time.sleep(1)
question_2 = int(input("Indique el tamaño de la muetra: "))
time.sleep(1)
question_3 = input("Indique que desea estimar: probabilidad, media poblacional, varianza poblacional, contraste paramétrico ó contraste no paramétrico: " )
time.sleep(1)
#question_4 = float(input("Nivel de confianza: "))
question_5 = float(input("Media de la muestra: "))
question_6 = float(input("Desviación típica de la población: "))
question_7 = float(input("Desviación típica de la muestra: "))
distributions = ["normal", "binomial", "poisson"]
varianza_muestral = question_7*question_7
cuasivarianza = (varianza_muestral*question_2)/(question_2 - 1)
cuasidesviacion_tipica = ((sqrt(cuasivarianza))/10).real
print(cuasivarianza)
def media_poblacional_dt_poblacional():
    brazo_izquierdo = (question_5 - 1.96*(question_7/sqrt(question_2)))
    brazo_derecho = (question_5 + 1.96*(question_7/sqrt(question_2)))
    solution_1 = [brazo_izquierdo.real, brazo_derecho.real] #REDONDEARLO
    return print(solution_1)

def media_poblacional_dt_muestra():
    solution_2 = st.t.interval(alpha=0.95, df= question_2 - 1, loc = question_5,scale =  cuasidesviacion_tipica ) #Está mal; hacerlo tú
    return print(solution_2)

media_poblacional_dt_poblacional()

media_poblacional_dt_muestra()
