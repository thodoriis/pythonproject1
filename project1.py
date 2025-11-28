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
        print(f"Past Population: {self.population - current_growth_rate}, New Population: {self.population}")

    def mutate(self):
        random_choice = random.choices ([0,1],weights=[self.mutation_rate,1-self.mutation_rate])[0]
        if random_choice == 0:
            self.growth_rate=self.growth_rate * random.choice([1.1,0.7])


    def __str__(self):
        return f"Species Name: {self.name}, Population: {self.population}, Growth Rate: {self.growth_rate}, Mutation Rate: {self.mutation_rate}"
        

d=Species("Dog",10000,200,random.random())
print(d)
d.reproduce(5000)
d.mutate()
print(d)


















class Ecosystem:

    def __init__(self,resources,species_list):
        self.resources=resources
        self.species_list=[]

    def add_species(self, species):
        if species not in self.species_list:
            self.species_list.append(species)
            print(f"Species {species} added to the ecosystem {self}.")
        else:
            raise ValueError(f"Species {species} already exists in the ecosystem {self}.")

    def search_species(self, species):
        if species in self.species_list:
            return species
        else:
            raise ValueError(f"Species {species} not found in the ecosystem {self}.")


    def remove_species(self,species):
        if species in self.species_list:
            self.species_list.remove(species)
            print(f"Species {species} removed from the ecosystem {self}.")
        else:
            raise ValueError(f"Species {species} not found in the ecosystem {self}.")
#isws
    def update_species(self,species):
        pass
            

    def display(self):
        pass

    def update_resources(self, num_resources):
        pass

    def run_generation(self):
        pass 


print(d)
e=Ecosystem(100000,[])
e.add_species(d)
print(e.search_species(d))
e.remove_species(d)
print(e.species_list)
