
#The first reverse engineering to run the code under O(n^2)
#The second code under the first is the optimized code to run O(n)

#Cafeteria Management Tool
#Mark meal cards.

class Student:
    def __init__(self,name,regno,AccessNumber,Course,HasEaten):
        self.name=name
        self.regno = regno
        self.AccessNumber=AccessNumber
        self.Course=Course
        self.HasEaten=HasEaten

class DailyAttendance:
    def __init__ (self,dayofTheWeek,studentMealList):
        self.dayofTheWeek=dayofTheWeek
        self.studentMealList=studentMealList

#The algorithm searches through a nested list
#When the student is found, the algorithm finds out if the student has not eaten
def searchToMarkMealCard(cafeteriaList, registrationNumber, dayOfTheWeek):

    for day in cafeteriaList:
        if(day.dayofTheWeek == dayOfTheWeek):
            for student in day.studentMealList:
                if(registrationNumber == student.regno):
                    if(not student.HasEaten):
                        return True
    return False

def main():
            
    serving=[]

    studentMealList=[]

    studentMealList.append(Student("Q","S21B23/019","A94172","B23",False));
    studentMealList.append(Student("A","S21B13/060","A94446","B13",True));
    studentMealList.append(Student("S","S21B13/023","A93581","B13",True));

    serving.append(DailyAttendance("Monday",studentMealList))


    print(searchToMarkMealCard(serving,"S21B23/019","Monday"))

    #Write a function that will update the Cafeteria's registry to "hasEaten" attribute to True, when
main()


########################## OPTIMIZED CODE   O(n) ###################################################


class Student:
    
    def __init__(self,name,regno,AccessNumber,Course,HasEaten):
        self.name=name
        self.regno = regno
        self.AccessNumber=AccessNumber
        self.Course=Course
        self.HasEaten=HasEaten
    
    def daysOfTheWeek(self,day):
        days = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
        if day in days:
            return day
            
def efficient(list,reg,day):
    if day == Student.daysOfTheWeek(Student,day):
        for student in list:
           if reg == student.regno:
                if(not student.HasEaten):
                    return True
        return False       
    else:
        print("Invalid day!!")
def main():
    
    studentMealList=[]
    studentMealList.append(Student("Q","S21B23/019","A94172","B23",False));
    studentMealList.append(Student("A","S21B13/060","A94446","B13",True));
    studentMealList.append(Student("S","S21B13/023","A93581","B13",True));
    print(efficient(studentMealList,"S21B13/060","Monday"))
    
main()


