import csv
import pandas as pd


class Hospital_Management:

    Doctors=[]
    Patients=[]
    Appointments=[]
    hAccounts=[]

    def AddDoctor(self):
        d_id=len(self.Doctors)+1
        d_name=input("Enter name of doctor: ")
        d_specialist=input("Enter speciality: ")
        d_contactNo=input("Enter contact no.: ")
        d_roomNo=input("Enter doctor room no.: ")

        Doctor={
            "ID":d_id,
            "Name":d_name,
            "Specialist":d_specialist,
            "Contact No.":d_contactNo,
            "Room No.":d_roomNo

        }
        self.Doctors.append(Doctor)

        fieldnames = ["ID", "Name", "Specialist", "Contact No.", "Room No."]
        with open("doctor.csv", mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.Doctors)
        print(f"Doctors saved to successfully!")

    def AddPatient(self):
        p_id=len(self.Patients)+1
        p_name=input("Enter Patient Name: ")
        p_age=input("Enter age: ")
        p_problem=input("Enter problem: ")
        p_contactNo=input("Enter contact No.: ")

        Patient={
            "ID":p_id,
            "Name":p_name,
            "Age":p_age,
            "Problem":p_problem,
            "Contact No.":p_contactNo
        }
        self.Patients.append(Patient)

        fieldnames=["ID","Name","Age","Problem","Contact No."]

        with open("patient.csv",mode="w",newline='') as file:
            writer=csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.Patients)

            print("Patient saved successfully.")

    def Appointment(self):
        A_serial=len(self.Appointments)+1
        A_name=input("Enter your name: ")
        A_age=input("Enter age: ")
        A_doctor_name=input("Eneter Doctor nanme: ")
        A_date=input("Enter Appointment date: ")
        A_phone=input("Enter your phone number: ")

        Appointment={
            "Serial No.":A_serial,
            "Patient Name":A_name,
            "Patient Age":A_age,
            "Doctor Name":A_doctor_name,
            "Date":A_date,
            "Phone":A_phone
        }

        self.Appointments.append(Appointment)

        fieldnames=["Serial No.","Patient Name","Patient Age","Doctor Name","Date","Phone"]

        with open("appopintment.csv",mode="w",newline='') as file:
            writer=csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.Appointments)
            print("Appointment saved successfully.")
###############################################################################################
    def ViewDoctorList(self):
        df=pd.read_csv("doctor.csv")
        print(df.to_string(index=False))
    def ViewPatientList(self):
        df=pd.read_csv("patient.csv")
        print(df.to_string(index=False))
    def ViewAppointmentList(self):
        df=pd.read_csv("appopintment.csv")
        print(df.to_string(index=False))
    def deleteDoctor(self):
        de=int(input("Enter Doctor ID: "))
        self.Doctors=[d for d in self.Doctors if d["ID"]!=de]
        df=pd.read_csv("doctor.csv")
        df=df[df["ID"]!=de]p
        df.to_csv("doctor.csv",index=False)
        print("Removed successfully.")
    def deletePatient(self):
        de=int(input("Enter Patient ID: "))
        self.Patients=[p for p in self.Patients if p["ID"]!=de]
        df=pd.read_csv("patient.csv")
        df=df[df["ID"]!=de]
        df.to_csv("patient.csv", index="False")
        print("Removed successfully")
    def cancelAppointment(self):
        de=int(input("Enter appointment serial no.: "))
        self.Appointments=[a for a in self.Appointments if a["Serial No."]!=de]
        df=pd.read_csv("appopintment.csv")
        df=df[df["Serial No."]!=de]
        df.to_csv("appopintment.csv")
        print("Removed successfully.")

#########################################################################################################
    def Hospital(self):
        print("1. Login")
        print("2. Register")

        op=input("Choose option: ")

        if op=="1":
            email=input("Enter email: ")
            password=input("Enter password: ")

            for i in range(len(self.hAccounts)):
                if self.hAccounts[i]["Email"]==email:
                    if self.hAccounts[i]["Password"]==password:
                        print("Login successful.")

                    else:
                        print('Password is incorrect')
                        self.Hospital()
                else:
                    print("Account didn't found.")
                    self.Hospital()

        elif op=="2":
            name=input("Enter name: ")
            email=input("Enter email: ")
            password=input("Enter password: ")


            for i in range(len(self.hAccounts)):
                if email in self.hAccounts[i].values():
                    print("This email already exists.")
                    self.Hospital()

            hAccount={
                "name":name,
                "Email":email,
                "Password":password
            }

            self.hAccounts.append(hAccount)
            print("Successfully registered.")
            self.Hospital()
        else:
            print("Invalid option.")
            self.Hospital()



        while True:
            print("0. Exit")
            print("1. Add Doctor ")
            print("2. Add Patient ")
            print("3. Delete Doctor ")
            print("4. Delete Patient")
            print("5. Cancel appointment")
            print("6. View Doctor ")
            print("7. View Patient ")
            print("8. View Appointment ")

            option = input("Enter option: ")

            if option == "0":
                break
            elif option == "1":
                p.AddDoctor()
            elif option == "2":
                p.AddPatient()
            elif option == "3":
                p.deleteDoctor()
            elif option=="4":
                p.deletePatient()
            elif option=="5":
                p.cancelAppointment()
            elif option == "6":
                p.ViewDoctorList()
            elif option == "7":
                p.ViewPatientList()
            elif option == "8":
                p.ViewAppointmentList()
            else:
                print("Invalid option.")
    def Patient(self):
        while True:
            print("0. Exit")
            print("1. View Doctor Lists ")
            print("2. Make Appointment ")

            option = input("Enter option: ")
            if option == "0":
                break
            elif option == "1":
                p.ViewDoctorList()
            elif option == "2":
                p.Appointment()
            else:
                print("Invalid option.")
p=Hospital_Management()

while True:
    print("-------------------Welcome To Our Hospital-------------------------------\n")
    print("0. exit")
    print("1. Hospital")
    print("2. Patient")

    menu=input("Choose option: ")

    if menu=="0":
        break
    elif menu=="1":
        p.Hospital()
    elif menu=="2":
        p.Patient()
    else:
        print("Invalid option.")