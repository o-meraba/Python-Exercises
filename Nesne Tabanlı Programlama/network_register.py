

class Person():

    def __init__(self, name="name", surname="surname", country="country", city_of_living="city_of_living", hometown="hometown", contact_type="contact_type"):
        self.name = name
        self.surname = surname
        self.country = country
        self.city_of_living = city_of_living
        self.hometown = hometown
        self.contact_type = contact_type
        self.social_medias = social_medias

    def add_user(self,name,surname,country,city_of_living,hometown,contact_type,social_medias):
        self.name = name
        self.surname = surname
        self.country = country
        self.city_of_living = city_of_living
        self.hometown = hometown
        self.contact_type = contact_type
        self.social_medias = social_medias
        #add to db
    def __str__(self):
       return "Name".format(self.name,self.surname,self.country,self.city_of_living,self.hometown,self.contact_type)

#"ömer","aba","Turkey", "Istanbul", "Diyarbakir", "telephone",["facebook","instagram"])
omer = Person()

#person.add_user("ömer", "aba", "Turkey", "Istanbul", "Diyarbakir", "telephone", "facebook,instagram")
print(omer)

