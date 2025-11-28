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
            print(f"Past Growth Rate: {self.growth_rate}")
            self.growth_rate=round(self.growth_rate * random.choice([1.1,0.7]))
            print(f"New Growth Rate: {self.growth_rate}")
        else:
            print("No Mutation Happened.")

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
        if species in self.species_list:
            new_name=str(input("Enter a new name."))
            new_population=int(input("Enter a new population."))
            new_growthrate=int(input("Enter a new growth rate."))
            new_mutationrate=float(input("Enter a new mutation rate."))
            species.name=new_name
            species.population=new_population
            species.growth_rate=new_growthrate
            species.mutation_rate=new_mutationrate
            return f"New Name: {species.name}, New Population: {species.population}, New Growth Rate: {species.growth_rate}, New Mutation Rate: {species.mutation_rate}"
        else:
            raise ValueError(f"Species {species} not found in the ecosystem {self}.")

    def display(self):
        print(f"Ecosystem Resources: {self.resources}")
        if len(self.species_list)==0:
            print("No Species Found.")
        else:
                for species in self.species_list:
                    print(f"{species}")

    def update_resources(self, num_resources):
        print(f"Current amount of resources: {self.resources}")
        new_resources=self.resources+num_resources
        if new_resources<0:
            while True:
                num_resources=int(input("Can't lose that many resources. Enter a new change in resources"))
                new_resources=self.resources+num_resources
                if new_resources>=0:
                    break
        print(f"New Resources:{new_resources}")
        self.resources=new_resources

    def run_generation(self):
        population_sum=0
        for species in self.species_list:
            species.mutate()
            species.reproduce(self.resources)
            population_sum=population_sum + species.population
            self.resources=self.resources-species.population
        
        if self.resources<0:
            return f"Not enough resources, {abs(self.resources)} animals left without food"
        elif self.resources==0:
            return f"Resources were exactly enough for the population."
        else:
            return f"Resources were enough. {self.resources} resources left."
#den xreiazetai __str__ giati exei to display
e=Ecosystem(100000,[])
e.add_species(d)
e.add_species(c)
e.add_species(f)
f=Species("Elephant",2,9000000,0.99)
print(e.search_species(d))
print(e.species_list)
e.remove_species(d)
c=Species("Cat",20,40,random.random())
e.search_species(f)
e.update_species(c)
print(e.species_list)
print(e.display())
e.display()
q=Ecosystem(23000,[])
q.display()
e.run_generation()
e.update_resources(-600000)