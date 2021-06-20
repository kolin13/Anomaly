class Room():

    def __init__(self, type, number, dostup):
        self.type = type
        self.number = number
        self.dostup = dostup

    def uroven(self):
        return self.dostup

    def info(self):
        print(self.type, ", номер -", self.number, "уровень доступа -", self.dostup)
        print("-----------------------------------------------------------------")



class chelovek():
    def __init__(self, typepol, ossoben, name, surname):
        self.typepol = typepol
        self.name = name
        self.surname = surname
        self.ossoben = ossoben
        if self.typepol == "родитель":
            self.urov = 0
        elif self.typepol == "ученик":
            self.urov = 1
        elif self.typepol == "учитель":
            self.urov = 2
        else:
            self.urov = 3

    def vxod(self, number):
        if self.urov >= spisokkomnat[number].uroven():
            print(f"{self.typepol} {self.name} {self.surname} пытается проникнуть в {spisokkomnat[number].type} {number}: успех")
            print("-----------------------------------------------------------------")
        else:
            print(f"{self.typepol} {self.name} {self.surname} пытается проникнуть в {spisokkomnat[number].type} {number}: неудача")
            print("-----------------------------------------------------------------")

    def info(self):
        print(self.name, self.surname, "-", self.typepol, ",", self.ossoben)
        print("-----------------------------------------------------------------")


room0 = Room("Учительская", 0, 2)
room1 = Room("Актовый зал", 1, 0)
room2 = Room("Кабинет для занятий", 2, 1)
room3 = Room("Кабинет директора", 3, 3)
room4 = Room("Кабинет для занятий", 4, 1)
room5 = Room("Кабинет для занятий", 5, 1)
spisokkomnat = [room0, room1, room2, room3, room4, room5]
chelovek1 = chelovek("родитель", "любит собак", "Павел", "Дроздяков")
chelovek2 = chelovek("директор", "10 наград", "Владимир", "Побединский")
chelovek3 = chelovek("учитель", "любимая шутка - заходит физик в бар...", "Бонредат", "Акисимович")
chelovek4 = chelovek("ученик", "пажилой геймер", "Виталий", "Эс")
chelovek5 = chelovek("учитель", "любимая шутка - Как доказать, что ученики ничего не делают", "Борис", "Трушин")
chelovek6 = chelovek("родитель", "Создатель легенд", "Gaben", "Freeman")
chelovek1.info()
chelovek2.info()
chelovek3.info()
chelovek4.info()
chelovek5.info()
chelovek6.info()
room0.info()
room1.info()
room2.info()
room3.info()
room4.info()
room5.info()
for i in range(6):
    chelovek6.vxod(i)
chelovek1.vxod(1)
chelovek2.vxod(1)
chelovek3.vxod(1)
chelovek4.vxod(1)
chelovek5.vxod(1)
chelovek6.vxod(1)
chelovek4.vxod(3)
chelovek5.vxod(3)

