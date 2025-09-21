from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox,QComboBox,QCheckBox)
import sys

def calcular():
    try:
        nombre = enombre.text().strip()
        peso = float(epeso.text())
        altura = float(ealtura.text())
        if peso <= 0 or altura <= 0:
            QMessageBox.warning(ventana,"Error","Ingrese valores positivos")
            return
        imc = peso / (altura**2)
        if imc < 18.5:
            estado = "Bajo peso"
        elif imc < 24.9:
            estado = "Normal"
        elif imc < 29.9:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        sexo = csexo.currentText()
        if sexo == "Hombre":
            rango = (20,25)
        else:
            rango = (19,24)

        mensaje = f"Hola {nombre if nombre else 'Usuario'}, tu IMC es {imc:.2f}\nClasificación: {estado}\nIMC ideal para {sexo}: {rango[0]} - {rango[1]}"

        if cpeso.isChecked():
            pi_min = rango[0]*(altura**2)
            pi_max = rango[1]*(altura**2)
            mensaje += f"\nPeso ideal: {pi_min:.1f} kg - {pi_max:.1f} kg"

        QMessageBox.information(ventana,"Resultado",mensaje)
    except ValueError:
        QMessageBox.warning(ventana,"Error","Ingrese valores numéricos válidos")

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Calculadora de IMC")
ventana.setGeometry(100,100,350,300)
layout = QVBoxLayout()

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

bcalcular.clicked.connect(calcular)
bsalir.clicked.connect(ventana.close)

widgets = [linst,lnombre,enombre,lpeso,epeso,laltura,ealtura,
           lseco,csexo,cpeso,bcalcular,bsalir]
for w in widgets:
    layout.addWidget(w)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())
#borras esto que solo quiero ingresarlo y me da error