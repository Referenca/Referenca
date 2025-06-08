import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Film_genre_choose_page import Ui_Film_page
from First_Window import Ui_My_cinema_ge

class basewindow(QMainWindow, Ui_My_cinema_ge, Ui_Film_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        class FirstApp(QMainWindow, Ui_My_cinema_ge, Ui_Film_page):
            def __init__(self):
                QMainWindow.__init__(self)
                Ui_My_cinema_ge.__init__(self)
                self.setupUi(self)
                self.film_btn.clicked.connect(self.Gadasvla)

            def Gadasvla(self):
                self.Film_page = SecondApp()
                self.Film_page.show()
                self.close()

        class SecondApp(QMainWindow, Ui_Film_page, Ui_My_cinema_ge):
            def __init__(self):
                QMainWindow.__init__(self)
                Ui_Film_page.__init__(self)
                self.setupUi(self)
                self.film_btn.clicked.connect(self.Gadmosvla)

            def Gadmosvla(self):
                self.My_cinema_ge = FirstApp()
                self.My_cinema_ge.show()
                self.close()



# class film_genre_choose(QMainWindow, Ui_Film_page):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#






app = QApplication(sys.argv)
window = basewindow()
window.show()
sys.exit(app.exec())


