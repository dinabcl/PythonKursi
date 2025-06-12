#create a class called DigitalSchool with 4 atributes a constructor, getters and setters with decorator and two methosed
class DigitalSchool:
    def __init__(self,name,city,state,courses):
        self.__name=name
        self.__city=city
        self.__state=state
        self.__courses=courses

    #def get and set for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    #def get and set for city
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city
    #def get and set for state
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
    #def get and set for courses
    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    #def methods
    def show_school_info(self):
        return {
            "name":self.__name,
            "city":self.__city,
            "state":self.__state,
            "courses":self.__courses
        }   #return a dictionary with school info

    def organize_hackathon(self): #define a placeholder method to be overriden by a subclasses
        print("Organizing a generic hackathon.")

#define a subclass called DS_Prishtina where it has a private atribute called stydent number and two methods organize_hacakathon and SCF
class DS_Prishtina(DigitalSchool):
    def __init__(self,name,city,state,courses,student_number):
        super().__init__(name, city, state, courses)
        self.__student_number=student_number

    def SCF(self):
        print("First edition")

    def organize_hackathon(self):
        print("We are doing a data analysis hackathon")

prishtina_obj=DS_Prishtina("DS_Prishtina","prishtina","Kosove",["PHP","Python","Java"], 3000)
prishtina_obj.SCF()
prishtina_obj.organize_hackathon()
print(prishtina_obj.show_school_info())

class DS_Ferizaj(DigitalSchool):
    def __init__(self,name,city,state,courses,student_number):
        super().__init__(name, city, state, courses)
        self.__student_number=student_number

    def organize_hackathon(self):
        print("We are doing a 48 hour hackathon. If you win you get an internship")

    def internship(self):
        print("You got an internship!")

ferizaj_obj = DS_Ferizaj("DS_Ferizaj","ferizaj","Kosove",["PHP","React","Java"],4444)
ferizaj_obj.organize_hackathon()
ferizaj_obj.internship()
print(ferizaj_obj.show_school_info())