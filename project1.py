import random

class Species:

    def __init__(self,name,population,growth_rate,mutation_rate):
        self.name=name 
        self.population=population
        self.growth_rate=growth_rate
        self.mutation_rate=mutation_rate    


    def reproduce(self,food_availability):
        if food_availability < self.population  :
            current_growth_rate=self.growth_rate//2
        else :
            current_growth_rate=self.growth_rate
        
        self.population += current_growth_rate
        print(self.population)

    def mutate(self):
        random_choice = random.choices ([0,1],weights=[self.mutation_rate,1-self.mutation_rate])[0]
        if random_choice == 0:
            self.growth_rate=self.growth_rate * random.choice([1.1,0.7])


    def data(self):
        print ( f"Species Name: {self.name}, Population: {self.population} ")
        

d=Species("Dog",10000,200,random.random())
d.reproduce(5000)
d.mutate()
d.data()


















class Ecosystem:

    def __init__(self,resources,species_list):
        self.resources=resources
        self.species_list=species_list

    def add_species(self, species):
        pass

    def search_species(self, species):
        pass

    def remove_species(self,species):
        pass

    def update_species(self,species):
        pass      

    def display(self):
        pass

    def update_resources(self, num_resources):
        pass

    def run_generation(self):
        pass 


jgniwvin