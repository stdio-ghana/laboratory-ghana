__author__ = 'MR.WIAFE'

import time

class Patients():


    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def arrival(self):
        self.patientArrival = time.strftime("%c")

    def payment(self,payments):
        self.payments = float(payments)

    def testRequest(self,testReq):
        self.testReq = testReq

    def testResulRetrival(self):
        self.resultRetivalDate = time.strftime("%c")


me = Patients(39232,"kofi",23)
me.testRequest("Gono")
me.payment(23.70)
me.testResulRetrival()
me.arrival()
print("patient Name : \t%s" %me.name,"\nAge : \t\t\t%a" %me.age , "\nTest type :\t\t%s" %me.testReq,"\nDate of arrival:%s" %me.patientArrival,"\nAmount Paid : \t%f"%me.payments,"\nDate of retrival of Results : %s"%me.resultRetivalDate)

