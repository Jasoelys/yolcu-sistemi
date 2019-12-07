from PyQt5 import QtWidgets, uic
from mydesign import Ui_Form
import sys,sqlite3
from functools import partial

#===veritabanı hazırlıkları===
db = sqlite3.connect("vst.sqlite")
im = db.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS yolcular
(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,ad,soyad,cinsiyet,tarih,saat,binis,inis)""")
#=== === === === === === === ===

class mywindow(QtWidgets.QMainWindow):
    
    def __init__(self):

        super(mywindow,self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #signals
        self.ui.kaydet_btn.clicked.connect(self.nasi)
        
        #dinamik
        self.ui.koltuk_1_btn.clicked.connect(
            partial(self.selectSeat, self.ui.koltuk_1_btn.objectName().split("_")[1]))
            
        #statik
        self.ui.koltuk_2_btn.clicked.connect(partial(self.selectSeat, "2"))
        self.ui.koltuk_3_btn.clicked.connect(partial(self.selectSeat, "3"))
        self.ui.koltuk_4_btn.clicked.connect(partial(self.selectSeat, "4"))
        self.ui.koltuk_5_btn.clicked.connect(partial(self.selectSeat, "5"))
        self.ui.koltuk_6_btn.clicked.connect(partial(self.selectSeat, "6"))
        self.ui.koltuk_7_btn.clicked.connect(partial(self.selectSeat, "7"))
        self.ui.koltuk_8_btn.clicked.connect(partial(self.selectSeat, "8"))
        self.ui.koltuk_9_btn.clicked.connect(partial(self.selectSeat, "9"))
        self.ui.koltuk_10_btn.clicked.connect(partial(self.selectSeat, "10"))
        self.ui.koltuk_11_btn.clicked.connect(partial(self.selectSeat, "11"))
        self.ui.koltuk_12_btn.clicked.connect(partial(self.selectSeat, "12"))

    #slots
    def selectSeat(self, text):
        print("Tıklandı",text)

    def nasi(self):
                        
        ad = self.ui.ad_txt.text()
        soyad = self.ui.soyad_txt.text()
        cinsiyet = self.ui.cinsiyet_cbBox.currentText()
        tarih = self.ui.dateEdit.text()
        saat = self.ui.timeEdit.text()
        binis = self.ui.binis_TEdit.toPlainText()
        inis = self.ui.inis_TEdit.toPlainText()

        veri = (ad,soyad,cinsiyet,tarih,saat,binis,inis)

        im.execute(
            """INSERT INTO yolcular 
                (ad,soyad,cinsiyet,tarih,saat,binis,inis) 
                VALUES(?,?,?,?,?,?,?)""", veri)
       
        db.commit()
        
        print("ad > "+ad
            ,"soyad > "+soyad
            ,"cinsiyet >"+cinsiyet
            ,"tarih > "+tarih
            ,"saat > "+saat
            ,"binis > "+binis
            ,"inis > "+inis
            ,sep="\n")

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
