
import random
from datetime import date


#Klasa bazowa
class Base:
    def __init__(self, type_card, title, year):
        self.type_card = type_card
        self.title = title
        self.year = year
        
        


#Klasa movies
class Movieinformation(Base):
    def __init__(self, title, year, type, numplays):
        super().__init__("Movie",title, year)
        
        self.type = type
        self.numplays = numplays
        
          
    def play(self):
        self.numplays += 1
        return self.numplays
    
    
    def __repr__(self): 
        return f'{self.title} ({self.year})'
    
   



#Klasa series
class Seriesinformation(Base):
    def __init__(self, title, year, type, episodenum, seasonnum, numplays):
        super().__init__("Series",title, year)
        self.typ = type
        self.episodenum = episodenum
        self.seasonnum = seasonnum
        self.numplays = numplays
    
    #Wyświetlenia
    def play(self):
        self.numplays += 1
        return self.numplays
     
    
    
    #Informacje
    def __repr__(self): 
        return f'{self.title} S{self.seasonnum} E{self.episodenum}'


movieserialsbase = [] 
library = []  

#Dodawanie filmu
def add_movies():
        m = Movieinformation(title=input("Title of movie: "), year=int(input("Movie year: ")), type=input("Movie type: "), numplays=random.randint(1,100))
        movieserialsbase.append(m)
        library.append(m)
        print("Successfully added movies \n")

#Dodawanie serialu
def add_series():
        s = Seriesinformation(title=input("Title of series: "), year=int(input("Series year: ")), type=input("Series type: "), seasonnum=int(input("Series season numbers: ")), episodenum=int(input("Series episode numbers: ")),numplays=random.randint(1,100))
        movieserialsbase.append(s)
        library.append(s)
        print("Successfully added series \n")

#Sortowanie według nazwy
def sort_title(title):
        return title.title

#Sortowanie według wyświetleń
def sort_plays(numplays):
    return numplays.numplays

#Biblioteka filmów i seriali
def show_library():
        print("Library of movies and series:\n ")
        library = sorted(movieserialsbase, key=sort_title)
        for i in library:    
            print(i)
        

#Lista top 3 filmów i seriali według wyświetleń
def top_titles():
    library = sorted(movieserialsbase, key=sort_plays)
    count = 3
    for i in range(count):
        if count != 0:
            print(library[i])
            count -= 1
        




def main():
   
    today = date.today()
    fdate = date.today().strftime('%d/%m/%y')
    
    print("Welcome to library of movies and series: \n")


    while True:
        print("""What would you like to do?:    
                1- Add movies
                2- Add series
                3- Show library of movies and series
                4- Top titles of today
                5- Exit""")
        
        x = input("Selected number: ")

        if x == '1': add_movies()
        if x == '2': add_series()
        if x == '3': 
            show_library()
        if x == '4': 
            print(f"The most popular movies and series of the day {fdate}")
            top_titles()
        if x == '5':
            print("Exiting bye...") 
            exit(1)       


if __name__ == "__main__":
    main() 
