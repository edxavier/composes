#/usr/bin/python
from PyQt5.QtWidgets import QPushButton, QApplication, QFormLayout, QWidget, QSpinBox, QRadioButton, QLabel, QFileDialog, QDateEdit, QMessageBox, QLineEdit, QCheckBox, QGroupBox, QVBoxLayout
from meteo_helpers import Generator, Generator2
from PyQt5.QtCore import QDate, Qt,  QThreadPool
import webbrowser
import os 


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.selected_cab = 28
        self.selected_dev = 'RVR'
        self.selected_file = None
        self.threadpool = QThreadPool()
        self.windowTitle = "Generador de formatos meteo"

        self.name = QLineEdit()
        self.group_box = QGroupBox()
        self.cab_box = QGroupBox()
        self.box = QVBoxLayout()
        self.box2 = QVBoxLayout()
        
        self.preview_template = QCheckBox()
        self.preview_template.setChecked(True)
        self.label = QLabel('Cabecera:')
        self.label2 = QLabel('Equipo:')
        self.date = QDateEdit(self)
        self.date.setCalendarPopup(True)
        d = QDate.currentDate()
        self.date.setDate(d) 

        self.rbtn1 = QRadioButton('10')
        self.rbtn1.toggled.connect(self.radio_checked)
        self.rbtn2 = QRadioButton('28')
        self.rbtn2.toggled.connect(self.radio_checked)
        self.rbtn2.setChecked(True)

        self.rvr = QRadioButton('RVR', self.group_box)
        self.rvr.setChecked(True)
        self.rvr.toggled.connect(self.equipo_checked)
        self.ceilo = QRadioButton('Ceilo', self.group_box)
        self.ceilo.toggled.connect(self.equipo_checked)

        self.box.addWidget(self.rvr)
        self.box.addWidget(self.ceilo)
        self.box.addStretch(1)
        self.group_box.setLayout(self.box)

        self.box2.addWidget(self.rbtn1)
        self.box2.addWidget(self.rbtn2)
        self.box2.addStretch(1)
        self.cab_box.setLayout(self.box2)


        self.week = QSpinBox()
        self.week.setRange(1, 3)

        self.select_btn = QPushButton("Seleccionar archivo")
        self.select_btn.pressed.connect(self.select_file_dalog)

        self.generate_btn = QPushButton("Generar archivo")
        self.generate_btn.setEnabled(False)
        self.generate_btn.pressed.connect(self.generate_report)
        self.setGeometry(500, 100, 300, 200)
  

        layout = QFormLayout()
        layout.addRow("Nombres o inicales", self.name)
        layout.addRow("Fecha de captura:",self.date)    
        layout.addRow(self.label2)    
        layout.addRow(self.group_box)

        layout.addRow("Semana:", self.week)
        layout.addRow(self.label)    
        layout.addRow(self.cab_box)
    
        layout.addRow("Mostrar sobre plantilla:",self.preview_template)    

        layout.addRow(self.select_btn)
        layout.addRow(self.generate_btn)

        self.setLayout(layout)

    def radio_checked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            print('radio_checked')
            self.selected_cab = int(radioBtn.text())

    def equipo_checked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.selected_dev = radioBtn.text()
            
    def select_file_dalog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Seleccionar captura de datos", "","All Files (*);;Txt Files (*.txt)", options=options)
        if fileName:
            self.selected_file = fileName
            self.generate_btn.setEnabled(True)
            #self.select_btn.setEnabled(False)

    def generate_report(self):
        if self.selected_file:
            folder = str(QFileDialog.getExistingDirectory(self, "Guardar resultado en:"))
            if folder:
                data = {
                    'selected_file': self.selected_file,
                    'selected_folder': folder,
                    'week': int(self.week.value()),
                    'preview': self.preview_template.isChecked(),
                    'cab': int(self.selected_cab),
                    'name': self.name.text(),
                    'date': (self.date.date().toString(Qt.DefaultLocaleShortDate)),
                }
                if self.selected_dev == 'RVR':
                    gen2 = Generator2(data)
                    gen2.signals.file_saved_as.connect(self.generated)
                    gen2.signals.error.connect(self.error)  # Print errors to console.
                    self.threadpool.start(gen2)
                else:
                    gen = Generator(data)
                    gen.signals.file_saved_as.connect(self.generated)
                    gen.signals.error.connect(self.error)  # Print errors to console.
                    self.threadpool.start(gen)

    def generated(self, outfile, path):
        self.generate_btn.setDisabled(False)
        try:
            os.startfile(outfile)
        except Exception:
            # If startfile not available, show dialog.
            #webbrowser.open_new(path)
            mess = "El reporte fue generado correctamente en la ruta seleccionada " + outfile
            QMessageBox.information(self, "Finalizado",  mess)

    def error(self, error):
        QMessageBox.warning(self, "Finalizado", "Error generando reporte: " + error)

app = QApplication([])
w = Window()
w.show()
app.exec()