# Calculadora de IMC con PyQt5
# Esta aplicación permite calcular el Índice de Masa Corporal (IMC) y proporciona información sobre el estado de salud basado en el IMC.
#primero importamos las librerias
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox,QComboBox,QCheckBox)
import sys
#luego definimos la funcion para calcular el IMC
def calcular():
    #obtenemos los valores de los campos de entrada
    try:
        nombre = enombre.text().strip()
        peso = float(epeso.text())
        altura = float(ealtura.text())
        #validamos que los valores sean positivos
        if peso <= 0 or altura <= 0:
            QMessageBox.warning(ventana,"Error","Ingrese valores positivos")
            return
        #calculamos el IMC
        imc = peso / (altura**2)
        #determinamos el estado de salud basado en el IMC
          #estado = "Bajo peso"
        if imc < 18.5:
            estado = "Bajo peso"
            #estado = "peso normal"
        elif imc < 24.9:
            estado = "Normal"
            #estado = "sobrepeso"
        elif imc < 29.9:
            estado = "Sobrepeso"
            #estado = "obesidad"
        else:
            estado = "Obesidad"
    #determinamos el rango de IMC ideal basado en el sexo
        sexo = csexo.currentText()
    # definimos el rango de IMC ideal
        if sexo == "Hombre":
            rango = (20,25)
        else:
            rango = (19,24)
    #preparamos el mensaje de salida
        mensaje = f"Hola {nombre if nombre else 'Usuario'}, tu IMC es {imc:.2f}\nClasificación: {estado}\nIMC ideal para {sexo}: {rango[0]} - {rango[1]}"
    #si el checkbox está seleccionado, mostramos el rango de peso ideal
        if cpeso.isChecked():
            pi_min = rango[0]*(altura**2)
            pi_max = rango[1]*(altura**2)
            mensaje += f"\nPeso ideal: {pi_min:.1f} kg - {pi_max:.1f} kg"
    #mostramos el mensaje en una caja de diálogo
        QMessageBox.information(ventana,"Resultado",mensaje)
    except ValueError:
        QMessageBox.warning(ventana,"Error","Ingrese valores numéricos válidos")
#creamos la aplicación y la ventana principal
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Calculadora de IMC")
ventana.setGeometry(100,100,350,300)
layout = QVBoxLayout()
#creamos los widgets
linst = QLabel("Ingrese sus datos para calcular IMC")
lnombre = QLabel("Nombre:")
enombre = QLineEdit()
lpeso = QLabel("Peso (kg):")
epeso = QLineEdit()
laltura = QLabel("Altura (m):")
ealtura = QLineEdit()
lseco = QLabel("Sexo:")
csexo = QComboBox()
csexo.addItems(["Hombre","Mujer"])
cpeso = QCheckBox("Mostrar rango de peso ideal")
bcalcular = QPushButton("Calcular IMC")
bsalir = QPushButton("Salir")
#conectamos los botones a las funciones
bcalcular.clicked.connect(calcular)
bsalir.clicked.connect(ventana.close)
#añadimos los widgets al layout
widgets = [linst,lnombre,enombre,lpeso,epeso,laltura,ealtura,
           lseco,csexo,cpeso,bcalcular,bsalir]
for w in widgets:
    layout.addWidget(w)
#configuramos la ventana
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())
