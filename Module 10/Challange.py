class DigitalSchool:
    def __init__(self,name,city,state,courses):
        self.__name=name
        self.__city=city
        self.__state=state
        self.__courses=courses

    @property
    def name(self):
        return self.__name

    @name.settter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.settter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.settter
    def state(self, state):
        self.__state = state

    @property
    def courses(self):
        return self.__courses

    @courses.settter
    def courses(self, courses):
        self.__courses = courses

    def show_school_info(self):pass #return a dictionary with school info
    def organize_hackathon(self):pass #define a placeholder method to be overriden by a subclasses


class DS_Prishtina(DigitalSchool):
    def __init__(self,name,city,state,courses,student_number):
        @property
        def name(self):
            return self.__name

        @name.settter
        def name(self, name):
            self.__name = name

        @property
        def city(self):
            return self.__city

        @city.settter
        def city(self, city):
            self.__city = city

        @property
        def state(self):
            return self.__state

        @state.settter
        def state(self, state):
            self.__state = state

        @property
        def courses(self):
            return self.__courses

        @courses.settter
        def courses(self, courses):
            self.__courses = courses

        @property
        def student_number(self):
            return self.__student_number

        @student_number.settter
        def student_number(self, student_number):
            self.__student_number = student_number

        def SCF(self):
            print("Spring Code")

        def organize_hackathon(self): pass #overrride the method

        #REDO