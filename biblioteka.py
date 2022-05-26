import random
from datetime import date

class Base:
    def __init__(self, type_card, title, year):
        self.type_card = type_card
        self.title = title
        self.year = year
        
        



class Movieinformation(Base):
    def __init__(self, title, year, type, numplays):
        super().__init__("Movie",title, year)
        
        self.type = type
        self.numplays = numplays
        
          
    def play(self):
        self.numplays += 1
        return self.numplays

    def info(self):
        informations = self.title + "\t" + f"({str(self.year)})"
        return informations
        
class Seriesinformation(Base):
    def __init__(self, title, year, type, episodenum, seasonnum, numplays):
        super().__init__("Series",title, year)
        self.typ = type
        self.episodenum = episodenum
        self.seasonnum = seasonnum
        self.numplays = numplays
    
    def play(self):
        self.numplays += 1
        return self.numplays

    def info(self):
        informations = self.title + " " + "S" + str(self.seasonnum) + "E" + str(self.episodenum)
        return informations




class Library:
    movieserialsbase = []

    def get_series(self):
        print("Series list: ")
        for i in self.movieserialsbase:
            if i.type == 'Series':
                print(i)
            sorted(i)
    
    def get_movies(self):
        print("Movies list: ")
        for i in self.movieserialbase:
            if i.type == 'Movies':
                print(i)
            sorted(i)

    def search(self):
        find = input("Find Movie or serial by its title: ")
        for i in self.movieserialsbase:
            if find == i.title:
                print(i.title)

    def generate_views(self):
        moviesample = Movieinformation(title)
        
        seriessample = Seriesinformation(title)
        
        sample = random.sample(zip(moviesample,seriessample), 1)
        print(sample)
        if sample == moviesample
        #sample = random.sample(self.movieserialsbase(self.title), 1)
        #print(sample)
        #title = self.movieserialsbase)
        #numplay = title(self.numplays)
        #randomnum = random.randint(1,100)
        #numplay.append(randomnum)
        
                
        
    



    def views_times_ten(self, generate_views):
        for i in range(11):
            generate_views()
            i += 1

    def top_titles(self):
        viewcount = 0
        content_type = input("Show top titles of movies or series? ")
        if content_type == 'Movies':
            for i in self.movieserialsbase:
                for x in range(4):
                    for y in self.movieserialsbase:
                        if y.type == 'Movies':
                            if i.numplays > viewcount:
                                viewcount += i.numplays
                                print(i.title)
                                x += 1
        elif content_type == 'series':
            for i in self.movieserialsbase:
                for x in range(4):
                    for y in self.movieserialsbase:
                        if y.type == 'Series':
                            if i.numplays > viewcount:
                                viewcount += i.numplays
                                print(i.title)
                                x += 1
    
    def add_movies_series(self):
        type_card = input("Choose movies or series: ")
        if type_card == 'movies':
            movies_title = input("Ttile of movie: ")
            movies_year = int(input("Movie year: "))
            movies_type = input("Movie type: ")
            movie_numplays = random.randint(1,100)
            newMovie = Movieinformation(movies_title, movies_year, movies_type, movie_numplays)
            self.movieserialsbase.append(newMovie)

        
        elif type_card == 'series':
            series_title = input("Title of series: ")
            series_year = int(input("Series year: "))
            series_type = input("Series type: ")
            series_season = int(input("Series season numbers: "))
            series_episode = int(input("Series episode numbers: "))
            series_numplays = random.randint(1,100)
            newSeries = Seriesinformation(series_title, series_year, series_type,series_season, series_episode, series_numplays)
            self.movieserialsbase.append(newSeries)
            
        
        
    def show_library(self):
        print("Library of movies and series: ")
        for i in self.movieserialsbase:
            if i.type_card == 'Movie':
                print(i.info())
            elif i.type_card == 'Series':    
                print(i.info())
        




def main():
    library = Library()
    today = date.today()
    fdate = date.today().strftime('%d/%m/%y')

    print("Movie library: ")
    
    library.add_movies_series()
    library.show_library()

    
    #library.generate_views()
    print(f"The most popular movies and series of the day {fdate}")
    #library.top_titles()


if __name__ == "__main__":
    main() 
