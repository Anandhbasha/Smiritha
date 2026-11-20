'''### **1. Singly Linked List – Hospital Patient Queue**

**Problem Statement:**

A hospital maintains a patient waiting list using a Singly Linked List. Each patient has a unique Patient ID and Name.

Implement a system that supports the following operations:

1. Add a new patient at the end of the waiting list.
2. Remove a patient using their Patient ID.
3. Display the patient waiting list.
4. Search for a patient using their Patient ID.
5. Display the total number of patients waiting.'''



class Patient:
    def __init__(self,patiendID,name):
        self.patiendID = patiendID
        self.name = name
        self.next = None
class Hospital:
    def __init__(self):
        self.head = None
    def addPatient(self,PID,Pname):
        newPatient =Patient(PID,Pname)
        if self.head is None:
            self.head= newPatient
            return
        temp = self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newPatient
    def removePatient(self,PID):
        temp = self.head
        prev =None
        if self.head is None:
            print("Waiting list is empty")
            return
        if self.head.patiendID==PID:
            self.head=self.head.next
            print("Patient removed sucessfully")
            return
        while temp is not None and temp.patiendID !=PID:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Patient id Not found")

        prev.next=temp.next
        print("Patiend Removed Sucessfully")
    def display(self):
        if self.head is None:
            print("waiting list is empty")
            return
        temp = self.head
        while temp is not None:
            print(f'ID:{temp.patiendID}|Name:{temp.name}')
            #  print("ID:",temp.patiendID, "|Name:"temp.name)
            temp = temp.next

H = Hospital()
H.addPatient(101,"Arun")
H.addPatient(102,"Balu")
H.addPatient(103,"Ravi")
H.addPatient(104,"Ragul")

print("Hospital Waiting List")
H.display()

pID = int(input("Enter a Patient ID to remove:"))
H.removePatient(pID)

print("Updated list")
H.display()

