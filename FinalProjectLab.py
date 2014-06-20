__author__ = 'MR.WIAFE'
__author__ = 'riomensah'
__author__ = 'madibalive'

import time,sys,os
import pickle

class Patients():


    def __init__(self,id,name,age):
        self.id = id
        self.name = str(name)
        self.age = age
        self.teststatus = "incomplete"
        self.resultRetrivalDate = 'Not yet'
        self.patientArrival = time.strftime("%c")


    def payment(self,payments):
        self.payments = float(payments)

    def testRequest(self,testReq):
        self.testReq = testReq

    def testResultRetrival(self):
        self.resultRetrivalDate = time.strftime("%c")

    def patientdetails(self):
        print("\nPatient ID : \t\t\t%s"%self.id,
                "\nPatient Name :\t\t\t%s"%self.name,
                "\nAge :\t\t\t\t%s" %self.age,
                "\nDate of test Request :\t\t%s"%self.patientArrival,
                "\nTest Name : \t\t\t%s"%self.testReq,
                "\nTest Cost : \t\t\t%s"%self.payments,
                "\nTest Status: \t\t\t%s"%self.teststatus,
                "\nDate of Test Retrival:  \t%s\n"%self.resultRetrivalDate)


class LaboratoryClass:

    def login(self):

            trials = 0
            print ("""\n
        ########################################
              LAB MANAGEMENT SYSTEM V 2.O
        ########################################
                """
                )
            while 1:

                self.member={"richard":"1234",
                        "seth":"1234",
                        "razak":"1234",
                        "kofi":"1234",
                        "amoateng":"1234"}
                userInput = str(input("** USER LOGIN **\nPLEASE ENTER YOUR USERNAME >> "))
                id =userInput.lower()
                password = str(input("PLEASE ENTER YOUR PASSWORD >> "))

                if id in self.member and self.member[id] == password:
                    print("+---------------------------------------+")

                    print('         WELCOME  ' + " " + id.upper())
                    print("+---------------------------------------+")

                    break


                elif trials == 4:
                    clear()
                    print("\n\n*****************************\n      ERROR !!!!   \n*****************************\n\n **** TOO MANY FAILED LOGINS ****\n PLEASE WAIT FOR 1 MINUTES!!!")
                    currentTimeMinute= int(time.strftime("%M"))
                    waitingTime = int(currentTimeMinute + 1)
                    while currentTimeMinute <= waitingTime:
                        if currentTimeMinute == waitingTime:
                            clear()
                            print("WAITING OVER PLEASE \nLOG IN NOW !!")

                            break
                        else:

                            currentTimeMinute = int(time.strftime("%M"))
                    self.login()
                    break

                else:

                    print("""\n****Incorrect User Id or Password**** """)

                trials += 1





    def logOut(self):
        print("##############################\n       LOGOUT SECTION \n##############################")
        try:
            y = int(input("\nAre you sure you want to Log out?\nEnter 1 for Yes or 2 for No\n"))
        except:
            print("*** INVALID INPUT ****")
            home()

        if y in range(1,3):
            if y == 1:
                clear()
                sys.exit(print("You have successfully Logged Out!!"))

                input()
            elif y == 2:
                home()
        else:
            print("**** invalid input ****")
            home()

class LabTests():

    def __init__(self,name):
        self.name = name
        self.testId = 'null'
        self.teststatus = "incomplete"
        self.testDuration = int(1)
        self.resultRetrivalDate = 'Not yet'

    def testDate(self):
        self.date = time.strftime("%d/%m/%y")

    def sampleType(self,sample):
        self.sample = sample

    def testCost(self,cost):
        self.cost = cost

    def testResults(self,result):
        self.result = result

    def testResultRetrival(self):
        self.resultRetrivalDate = time.strftime("%c")

    def testdetails(self):
        print("\nTest ID : \t\t\t%s"%self.testId,
                "\nTest Name :\t\t\t%s"%self.name,
                "\nTest Duration :\t\t\t%s days" %self.testDuration,
                "\nSample Taken : \t\t\t%s" %self.sample,
                "\nDate of test Request :  \t%s"%self.date,
                "\nTest Cost : \t\t\t%s"%self.cost,
                "\nTest Status: \t\t\t%s"%self.teststatus,
                "\nDate of Test Delivery:  \t%s" %self.resultRetrivalDate,
                "\nTest Details : \n---------------\n%s"%self.result
                )





technician = LaboratoryClass()


total_Patients_Dict=dict()
completed_Patients_Test = dict()
patients_List = list()
test_List = list()
completed_Tests = list()
incomplete_Test = dict()


def save_files():
    x = open("testObjects.pkl","wb")
    y = open("patientsObjects.pkl","wb")
    z = open("testObjCount.pkl","wb")
    a = open("testCompletedCount.pkl","wb")
    b = open("completedTest.pkl","wb")
    c = open("incompletedTest.pkl","wb")
    pickle.dump(test_List,x)
    pickle.dump(patients_List,y)
    pickle.dump(total_Patients_Dict,z)
    pickle.dump(completed_Patients_Test,a)
    pickle.dump(completed_Tests,b)
    pickle.dump(incomplete_Test,c)
    x.close()
    y.close()
    z.close()
    a.close()
    b.close()
    c.close()
try:
    open("testObjects.pkl","rb")
except:
    save_files()

x1 = open("testObjects.pkl","rb")
y1 = open("patientsObjects.pkl","rb")
z1 = open("testObjCount.pkl","rb")
a1 = open("testCompletedCount.pkl","rb")
b1 = open("completedTest.pkl","rb")
c1 = open("incompletedTest.pkl","rb")
test_List = pickle.load(x1)
patients_List = pickle.load(y1)
total_Patients_Dict = pickle.load(z1)
completed_Patients_Test = pickle.load(a1)
completed_Tests = pickle.load(b1)
incomplete_Test = pickle.load(c1)


def clear():
    clr = 'clear'
    os.system(clr)


def patientInfo():
    print ("""
    ####################################
              PATIENT PROFILE
    ####################################
    Note: Enter <-1> to stop operation)""")

    identity = input("ENTER PATIENT'S ID        >> ")
    if identity == '-1':
        print("\n***** OPERATION CANCELED!! *****")
        input("PRESS <ENTER> TO GO TO HOME")
        home()

    name = input("ENTER NEW PATIENT'S FULL NAME  >> ")
    if name == '-1':
        print("\n***** OPERATION CANCELED!! *****")
        input("PRESS <ENTER> TO GO TO HOME")
        home()
    while 1:
        try:
            age = int(input("ENTER NEW PATIENT'S AGE   >> "))

            if age in range(1,200):
                break
            else:
                print("AGE SHOULD BE IN RANGE 1 - 200")
                continue
        except:
            print("ENTER THE AGE IN FIGURES !!")
            continue
    patients_List.append(Patients(identity,name,age))



def generateId(y):
    count = str(y+1)
    uniqId = "LT"
    test_List[y].testId = uniqId+count



def newTest():
    # creates a new object for the Test call when ever this function is called
    # y hold the position of the object in the test list, which also the same position for the patient object in the patient list
    clear()
    y = int(len(test_List))
    print("""
       ###################################
                TEST DETAILS
       ###################################
       """)
    testname = input("\nENTER TEST NAME      >> ")
    test_List.append(LabTests(testname))

    #the stuff below intializes the various attributes of the patient object and test object created
    #Attributes like test requested by patient & date of test delivery and also generate an id for the particular test

    patients_List[y].testRequest(testname)
    test_List[y].testDate()
    generateId(y)
    total_Patients_Dict[patients_List[y].name] = int(y)


    sample = input("ENTER SAMPLE TAKEN   >> ")
    test_List[y].sampleType(sample)

    duration = input("ENTER TEST DURATION  >> ")
    test_List[y].testDuration = duration
    while 1:
        try:
            testcost = float(input("ENTER TEST COST      >> "))
            if testcost >= 0:
                break
            else:
                print("***** NEGATIVE FIGURES ARE NOT ALLOWED!! *****")
                continue
        except:
            print("***** ENTER THE COST IN FIGURES !! *****")
            continue

    patients_List[y].payment(testcost)
    test_List[y].testCost(testcost)

    #this stores the value of y, which is the position of the object created in a dictionary called incomplete_test with a key = the testId generated which will later aid in our search function below
    incomplete_Test["%s"%test_List[y].testId] = int(y)
    clear()
    print("PLEASE RECORD PATIENT'S TEST ID\n\n")
    print("TEST ID  =  %s"%test_List[y].testId)


def lab_Result():
    print ("""
        ##############################################
                    TEST RESULT ENTRY
        #############################################
        NOTE: YOU CAN ENTER <-1> TO CANCEL OPERATION
        """)

    var = input("\nENTER <-2> TO DISPLAY LIST OF INCOMPLETED TEST AND CORRESPONDING PATIENTS \n\nENTER TEST ID   >> ")
    if var == '-1':
        print("\n***** OPERATION CANCELED!! *****")
        input("PRESS <ENTER> TO GO TO HOME")
        home()
    elif var == '-2':
            if len(incomplete_Test)==0:
                print("\nNO INCOMPLETE TEST AVAILABLE\n\n")
                input("PRESS <ENTER> TO GO TO HOME")
                home()
            else:
                clear()
                print("LIST OF INCOMPLETED TEST AND CORRESPONDING PATIENTS\n-----------------------------------------------")
                print("TEST ID             PATIENTS NAME\n")
                for x in incomplete_Test.keys():
                    print("* %s    - \t  %s" %(x,patients_List[incomplete_Test[x]].name))
                lab_Result()

    #obj will holds the object postiton of an object in the object list with a test id given by the user
    if var in incomplete_Test:
        obj = int(incomplete_Test[var])
        clear()
        print("NOTE!! ENTER <-1> ON A NEW LINE TO SAVE DATA\n")
        print("ENTER TEST RESULTS DETAILS  >>")
        detail = ''
        while 1:
            line = input()
            if line == '-1':
                break
            else:
                detail = "%s%s\n"%(detail,line)


        test_List[obj].testResults(detail)
        test_List[obj].teststatus = "COMPLETE"
        patients_List[obj].teststatus = "COMPLETE"
        completed_Tests.append(test_List[obj].testId)

        #this also saves the object position of a particular patient when test is completed to a dictionary with patient name as key
        completed_Patients_Test[patients_List[obj].name] = incomplete_Test[var]

        #removes item from incomplete list when test is complete
        incomplete_Test.pop(var)

        input("PRESS <ENTER> TO SAVE")
        clear()
        print("DATA SAVED !!!")
        input("PRESS <ENTER> TO GO TO HOME")
        home()
    else:
        #this lines of code caters for when there is no available test for the test Id provided

        clear()
        print("\n****** LAB TEST RESULT ENTRY ******\n\n\nNO TEST AVAILABLE FOR THE I.D ENTERED!!")
        response = input("\nNOTE! ENTER <-2> TO VIEW LIST OF INCOMPLETE TEST\n**** CHOOSE AN OPTION **** \n1.GO BACK TO HOMESCREEN \n2.TO TRY AGAIN\n >> ")
        if response == '-1':
            print("\n***** OPERATION CANCELED!! *****")
            input("PRESS <ENTER> TO GO TO HOME")
            home()
        elif response == '-2':

            if len(incomplete_Test)==0:
                print("\nNO INCOMPLETE TEST AVAILABLE")
                input("PRESS <ENTER> TO GO TO HOME")
                home()
            else:
                clear()
                print("LIST OF INCOMPLETED TEST AND CORRESPONDING PATIENTS\n-----------------------------------------------")
                print("TEST ID             PATIENTS NAME\n")
                for x in incomplete_Test.keys():
                    print("* %s    - \t  %s" %(x,patients_List[incomplete_Test[x]].name))
                lab_Result()

        if response == '2':
                clear()
                lab_Result()
        elif response == '1':
            home()
        else:
            clear()
            print("****  INVALID INPUT *****")
            lab_Result()
#This function opens the test result for printing
def opentext():
    command = 'gedit ./textfile.txt'
    command2 = 'gedit'
    os.system(command)
    os.system(command2)



def retrival_Of_Report():
    print ("""
            ######################################
                    TEST REPORT RETRIEVAL
            #######################################
            SEARCH FOR REPORT USING PATIENT NAME
            NOTE: ENTER <-1> TO CANCEL OPERATION

            """)
    check = input("\nENTER <-2> TO DISPLAY LIST OF PATIENTS\n\nENTER PATIENT'S NAME : ")
    if check == '-1':
        print("\n*****OPERATION CANCELED!!*****")
        input("PRESS <ENTER> TO GO TO HOME")
        home()
    elif check == '-2':

            if len(completed_Patients_Test)==0:
                print("\nTHERE IS NO COMPLETED TEST !!!")
                input("PRESS <ENTER> TO GO TO HOME!")
                home()
            else:
                clear()
                print("LIST OF PATIENTS WITH COMPLETED TEST\n----------------------------------------")
                for x in completed_Patients_Test.keys():
                    print("* %s" %x )
                retrival_Of_Report()

    if check in completed_Patients_Test:
        y = int(completed_Patients_Test[check])

        test_List[y].testResultRetrival()
        patients_List[y].testResultRetrival()
        text = open("textfile.txt","w")
        text.write("""
		#####################################################################################
                                                STDIO GHANA HOSPITAL
	      		        	      	     LAB REPORT

		*************************************************************************************


		PATIENT NAME : %s 			PATIENT ID   : %s

		COST OF TEST : %s

    		--------------------------------------------------------------------------------------

		TEST ID : %s				    TEST NAME : %s



		TEST STATUS :%s                       SAMPLE TAKEN : %s


----------------------------------------------------------------------------------------------------------------
					    TEST DETAILS /REPORT

---------------------------------------------------------------------------------------------------------------
%s






----------------------------------------------------------------------------------------------------------------
		DATE OF TEST RETRIEVAL:%s


		                                                      copyright (2014) GROUP5.INC

"""%(patients_List[y].name,patients_List[y].id,test_List[y].cost,test_List[y].testId,test_List[y].name,test_List[y].teststatus,test_List[y].sample,test_List[y].result,test_List[y].resultRetrivalDate))
        text.close()
        test_List[y].testdetails()

        option = input("\nCHOOSE AN OPTION \n1.GO BACK TO HOMESCREEN \n2.VIEW TEST REPORT FOR PRINTING\n >> ")
        if option == '-1':
            print("\n****OPERATION CANCELED!!****")
            input("PRESS <ENTER> TO GO TO HOME")
            home()
        elif option == '-2':
            if len(completed_Patients_Test)==0:
                print("\nTHERE IS NO COMPLETED TEST !!!")
                input("\n****** PRESS <ENTER> TO GO TO HOME! ******")
                home()
            else:
                clear()
                print("LIST OF PATIENTS WITH COMPLETED TEST\n----------------------------------------")
                for x in completed_Patients_Test.keys():
                    print("* %s" %x )
                retrival_Of_Report()

        if option == '1':
            home()
        elif option == '2':
            opentext()
            clear()
            input("PRESS <ENTER> TO GO HOME")
            home()
        else:
            print("\n*****INVALID INPUT*****")
            input("PRESS <ENTER> TO TRY AGAIN")
            retrival_Of_Report()


    else:
        #this lines of code caters for when there is no available test report for the patient of the name provided
        clear()
        print("\n**** LAB TEST RETRIEVAL *****\n\nLAB TEST NOT AVAILABLE FOR NAME ENTERED ")
        response = input("\nNOTE! ENTER <-2> TO VEW LIST OF PATIENTS\n****CHOOSE AN OPTION**** \n1.GO BACK TO HOMESCREEN \n2.TO TRY AGAIN \n >> ")
        if response == '-2':
            if len(completed_Patients_Test)==0:
                print("\nTHERE IS NO COMPLETED TEST !!!")
                input("PRESS <ENTER> TO GO TO HOME!")
                home()
            else:
                clear()
                print("LIST OF PATIENTS WITH COMPLETED TEST\n----------------------------------------")
                for x in completed_Patients_Test.keys():
                    print("* %s" %x )
                retrival_Of_Report()
        elif response == '-1':
            print("\n*****OPERATION CANCELED!!******")
            input("PRESS <ENTER> TO GO TO HOME")
            home()
        elif response == '2':
            clear()
            retrival_Of_Report()
        elif response == '1':
            home()
        else:
            clear()
            print("*****INVALID INPUT*****")
            retrival_Of_Report()

def patient_Details():
    print ("""
        ###########################################
                   PATIENTS DETAILS
        ###########################################
        NOTE: ENTER <-1> TO CANCEL OPERATION
        """
    )
    check = input("\nENTER <-2> TO DISPLAY LIST OF PATIENTS \n\nENTER PATIENTS NAME >>")

    if check == '-1':
        print("\n*****OPERATION CANCELED!!*****")
        input("PRESS <ENTER> TO GO TO HOME")
        home()
    elif check == '-2':
                if len(total_Patients_Dict)==0:
                    print("NO PATIENT RECORD AVAILABLE")
                    home()
                else:
                    clear()
                    print("LIST OF PATIENTS\n---------------")
                    for x in total_Patients_Dict.keys():
                        print("* %s" %x )

                    patient_Details()

    elif check in total_Patients_Dict:
        y = int(total_Patients_Dict[check])
        patients_List[y].patientdetails()
    else:
        clear()
        #this lines of code caters for when there is no available test report for the patient of the name provided
        print("\n****** PATIENT INFO ******\n\n\nNO RECORD FOUND THIS NAME !!!")
        response = input("\nNOTE! ENTER <-2> TO VIEW LIST OF PATIENTS \n****CHOOSE AN OPTION**** \n1.GO BACK TO HOMESCREEN \n2.TO TRY AGAIN \n >> ")
        if response == '-1':
            print("\n*****OPERATION CANCELED!!*****")
            input("PRESS <ENTER> TO GO TO HOME")
            home()
        elif response == '-2':
            if len(total_Patients_Dict)==0:
                print("NO PATIENT RECORD AVAILABLE")
                home()
            else:
                clear()
                print("LIST OF PATIENTS\n---------------")
                for v in total_Patients_Dict.keys():
                    print(v)


                patient_Details()

        elif response == '2':
            clear()
            patient_Details()

        elif response == '1':
            home()
        else:
            clear()
            print("****INVALID INPUT**** ")
            patient_Details()

#this function serves as the home page of software
def home():
    clear()
    save_files()

    print("""
    #########################################################
                 LAB MANAGEMENT SYSTEM  >> MENU
    #########################################################

            CHOOSE AN OPTION
            1.NEW TEST REQUEST
            2.ENTER TEST RESULTS DETAILS
            3.RESULTS RETRIEVAL
            4.PATIENTS  DETAILS

            5.logout \n



                                           copyrights(2014 ) group5.inc
         """)

    while 1:
            try:
                task = int(input("ENTER CHOICE >>"))
                if task in range(1,6):
                    break
                else:
                    print ("********  ERROR ************")
                    print("***** INVALID OPTION *******\n\nPLEASE CHOOSE BETWEEN OPTION 1 - 5!!!")
                    input("PRESS <ENTER> TO TRY AGAIN")
                    home()
            except:
                print ("*********  ERROR ************")
                print("***** INVALID OPTION *******\n\nPLEASE CHOOSE BETWEEN OPTION 1 - 5!!!")
                input("PRESS <ENTER> TO TRY AGAIN!!")
                home()
    if task == 1:
        clear()
        patientInfo()
        newTest()
        input("PRESS <ENTER> TO SAVE")
        clear()
        print("DATA SAVED !!!")
        home()

    elif task == 2:
        clear()
        lab_Result()

    elif task == 3:
        clear()
        retrival_Of_Report()
        input("PRESS <ENTER> TO SAVE")
        print("DATA SAVED")
        home()

    elif task == 4:
        clear()
        patient_Details()
        input("PRESS <ENTER> TO GO TO HOME")
        home()

    elif task == 5:

        clear()
        save_files()
        technician.logOut()

    else:
        print ("*********  ERROR ************")
        print("\n******INVALID INPUT********\nPLEASE CHOOSE BETWEEN OPTION 1 - 5!!")
        home()
clear()
technician.login()
home()
save_files()
