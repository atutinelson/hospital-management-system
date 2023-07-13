import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from datetime import datetime
from sidebar_ui import Ui_MainWindow
from database import session, Patient


# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
# python -m PyQt5.uic.pyuic -x sidebar.ui -o sidebar_ui.py
def show_popup(message, icon_type):
    msg = QMessageBox()
    msg.setWindowTitle("Hospital management system")
    msg.setText(message)
    if icon_type == "error":
        msg.setIcon(QMessageBox.Warning)
    elif icon_type == "infor":
        msg.setIcon(QMessageBox.Information)
    else:
        msg.setIcon(QMessageBox.Critical)
    x = msg.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    ## functions for changing menu page

    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        date = datetime.now()
        self.ui.date_of_admission.setDate(date)
        self.ui.register_btn.clicked.connect(self.registration)

    def registration(self):
        date_of_admission = self.ui.date_of_admission.date().toPyDate()
        admission_number = self.ui.admission_number.text()
        full_names = self.ui.fullname.text()
        date_of_birth = self.ui.date_of_birth.date().toPyDate()
        age = self.ui.age.text()
        county = self.ui.county.currentText()
        sub_county = self.ui.sub_county.text()
        village = self.ui.village.text()
        marital_status = self.ui.marital_status.currentText()
        phone_number = self.ui.phone_number.text()
        parity = self.ui.parity.text()
        ovaration = self.ui.ovaration.text()
        number_of_ANC_visits = self.ui.no_of_anc_visits.text()
        last_date_of_menstrual_period = self.ui.lmp.date().toPyDate()
        estimated_date_of_birth = self.ui.estimated_date_of_birth.date().toPyDate()
        diagnosis = self.ui.diagosis.text()
        result = len(admission_number) == 0 or len(full_names) == 0
        result2 = len(age) == 0 or len(county) == 0 or len(sub_county) == 0 or len(village) == 0 or len(
            marital_status) == 0
        result3 = len(phone_number) == 0 or len(parity) == 0 or len(ovaration) == 0 or len(number_of_ANC_visits) == 0
        result4 = len(diagnosis) == 0

        final_result = result and result2 and result3 and result4
        print(type(date_of_admission))
        if final_result == False:
            try:
                patient = Patient(date_of_admission=date_of_admission, admission_number=admission_number,
                                  fullname=full_names,
                                  date_of_birth=date_of_birth, age=int(age), county=county,
                                  sub_county=sub_county,
                                  village=village,
                                  marital_status=marital_status, phone_number=phone_number, parity=parity,
                                  oviration=ovaration,
                                  no_of_anc_visits=int(number_of_ANC_visits),
                                  date_of_last_menstrual_period=last_date_of_menstrual_period,
                                  estimated_date_of_birth=estimated_date_of_birth,
                                  diagnosis=diagnosis)
                session.add(patient)
                session.commit()
                show_popup("you have successfully inserted new patient", icon_type="infor")
            except Exception as e:
                print(e.)
                show_popup(message="error", icon_type="error")

        else:
            show_popup("all fields are required", icon_type="error")

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.delivery_btn.clicked.connect(self.delivery)

    def delivery(self):
        duration_of_labour = self.ui.duration_of_labor.text()
        date_of_delivery = self.ui.date_of_delivery.text()
        time_of_delivery = self.ui.time_of_delivery.text()
        gestation = self.ui.gestation.text()
        mode_of_delivery = self.ui.mode_of_delivery.currentText()
        no_of_baby = self.ui.no_of_baby.text()
        placenta_complete = self.ui.placenta_complete.currentText()
        uterus_givern = self.ui.uterus_givern.currentText()
        vigina_examination = self.ui.vigina_examination.currentText()
        blood_loss = self.ui.blood_loss.text()
        admission_no = self.ui.admission_no.text()
        fields = [duration_of_labour, date_of_delivery, time_of_delivery, gestation, mode_of_delivery, no_of_baby,
                  placenta_complete, uterus_givern, vigina_examination, blood_loss, admission_no]
        counter = 0

        print("clicked delivery button")

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.baby_submit.clicked.connect(self.baby)
        
    def baby(self):
        birth_weight = self.ui.birth_weight.text()
        sex = self.ui.sex.currentText()
        initited_on_BF = self.ui.initiated_bf.currentText()
        kangaroo_mother_care = self.ui.kangaroo_mother.currentText()
        teo_givern_birth = self.ui.teo_givern_at_birth.currentText()
        chlorhexidine = self.ui.chlorhexidine.currentText()
        birth_with_deformity = self.ui.birth_with_deformity.currentText()
        givern_vitamin_k = self.ui.givern_vitamin_k.currentText()
        vdrl_result = self.ui.vdrl_result.currentText()
        print(f"{birth_weight},{sex}, {initited_on_BF}, {kangaroo_mother_care},{teo_givern_birth}")
        print(f"{chlorhexidine},{birth_with_deformity}, {givern_vitamin_k}, {vdrl_result}")

    def on_orders_btn_2_toggled(self):
        print("health status 1")
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.health_information_btn.clicked.connect(self.health_information)

    def health_information(self):
        kit_name1 = self.ui.kit_name1.text()
        lot_no1 = self.ui.lot_no1.text()
        expiry1 = self.ui.exipiry1.text()
        result1 = self.ui.result1.currentText()
        kit_name2 = self.ui.kit_name2.text()
        lot_no2 = self.ui.lot_no2.text()
        expiry2 = self.ui.expiry2.text()
        result2 = self.ui.result2.currentText()
        hiv_result_maternity = self.ui.hiv_result_maternity.currentText()
        mother_issued_from_anc = self.ui.issued_from_anc.currentText()
        mother_issued_from_maternity = self.ui.issued_from_maternity.currentText()
        ctx_to_mother = self.ui.ctx_to_mother.currentText()
        partner_test_for_hiv = self.ui.partner_test_for_hiv.currentText()
        partner_hiv_status = self.ui.partner_hiv_status.currentText()
        to_baby_maternity = self.ui.to_baby_in_mat.currentText()
        counseling_on_infant_feeding = self.ui.counselled_on_infant_feeding.currentText()
        delivery_conducted_by = self.ui.delivery_conducted_by.text()
        print(f"{kit_name2}, {delivery_conducted_by},{counseling_on_infant_feeding}")
        


    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
