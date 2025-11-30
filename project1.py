#Thodoris Apostolidis 62300008
#Giorgos Toufekoulas 6230103

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


class Ecosystem:

    def __init__(self,resources,species_list):
        self.resources=resources
        self.species_list=[]

    def add_species(self, species):
        if species not in self.species_list:
            self.species_list.append(species)
            print(f"Species {species} added to the ecosystem.")
        else:
            raise ValueError(f"Species {species} already exists in the ecosystem.")

    def search_species(self, speciesname):
        for species in self.species_list:
            if species.name == speciesname:
                return species
        raise ValueError(f"Species {speciesname} not found in the ecosystem.")

    def remove_species(self,speciesname):
        for species in self.species_list:
            if species.name == speciesname:
                self.species_list.remove(species)
                return f"Species {speciesname} removed from the ecosystem."
        raise ValueError(f"Species {species} not found in the ecosystem.")

    def update_species(self,speciesname):
        for species in self.species_list:
            if species.name == speciesname:
                new_name=str(input("Enter a new name."))
                new_population=int(input("Enter a new population."))
                new_growthrate=int(input("Enter a new growth rate."))
                new_mutationrate=float(input("Enter a new mutation rate."))
                species.name=new_name
                species.population=new_population
                species.growth_rate=new_growthrate
                species.mutation_rate=new_mutationrate
                return f"New Name: {species.name}, New Population: {species.population}, New Growth Rate: {species.growth_rate}, New Mutation Rate: {species.mutation_rate}"
        raise ValueError(f"Species {species} not found in the ecosystem.")

    def display(self):
        print(f"Ecosystem Resources: {self.resources}")
        if len(self.species_list)==0:
            print("No Species Found.")
        else:
                for species in self.species_list:
                    print(species)

    def update_resources(self, num_resources):
        print(f"Current amount of resources: {self.resources}")
        new_resources=self.resources+num_resources
        if new_resources<0:
            while True:
                num_resources=int(input("Can't lose that many resources. Enter a new change in resources."))
                new_resources=self.resources+num_resources
                if new_resources>=0:
                    break
        print(f"New Resources:{new_resources}")
        self.resources=new_resources

    def run_generation(self):
        for species in self.species_list:
            print(species.name)
            species.mutate()
            species.reproduce(self.resources)
            self.resources=self.resources-species.population
        if self.resources<0:
            return f"Not enough resources, {abs(self.resources)} animals left without food"
        elif self.resources==0:
            return f"Resources were exactly enough for the population."
        else:
            return f"Resources were enough. {self.resources} resources left."
#den xreiazetai __str__ giati exei to display


def simulate_generations(ecosystems, generations, resources):
    ecosystems.resources=resources
    gen_count=1
    while gen_count<=generations and ecosystems.resources>0:
        print(f"Generation{gen_count}")
        x=ecosystems.run_generation()  #gia na epistrefei to return
        print(x)
        gen_count+=1
        resources=ecosystems.resources
    if gen_count<generations:
        if resources==0 and gen_count==1: #gia ama valei input resources mhden
            return f"All animals left without food. Please input a positve number of resources."
        else:
            return f"The simulation ended at generation {gen_count} due to lack of resources. {abs(resources)} animals were left without food."
    else:
        if resources<=0:
            return f"Resources ran out at the last generation. {abs(resources)} animals left without food."  
        else:
            return f"Simulation complete. {resources} resources left."


def menu():
    print(
       """ 1. Create New Ecosystem
       2. Display Ecosystem Data
       3. Add New Species
       4. Search Species
       5. Update Species
       6. Remove Species
       7. Display Species List
       8. Update Resources
       9. Simulate Generations
       10. Exit"""
    )
menu()

def main():
    n=list(range(1,11))
    menu()
    choice=int(input("Please select an action."))
    while choice not in n:
        choice=int(input("Selection must be a number between 1-10, please pick again."))
    while True:
        if choice==1:
            EcName=str(input("Enter a name for the new ecosystem."))
            EcRes=int(input("Enter the amount of resources for the new ecosystem."))
            EcName=Ecosystem(EcRes,[])
            print()
        elif choice==10:
            print("Exiting.")
            break
        else:
            try:
                EcName
            except NameError:
               print("You must create an environment first.")
            else:
                if choice==2:
                    EcName.display()
                elif choice==3:
                    SpName=str(input("Enter species name."))
                    SpPop=int(input("Enter species population."))
                    SpGR=int(input("Enter species growth rate."))
                    SpMR=float(input("Enter species mutation rate."))
                    SpName=Species(SpName,SpPop,SpGR,SpMR)
                    EcName.add_species(SpName)
                elif choice==4:
                    SpName=str(input("Enter species name."))
                    print(EcName.search_species(SpName))
                elif choice==5:
                    SpName=str(input("Enter species name."))
                    print(EcName.update_species(SpName))
                elif choice==6:
                    SpName=str(input("Enter species name."))
                    print(EcName.remove_species(SpName))
                elif choice==7:
                    for species in EcName.species_list:
                        print(species)
                elif choice==8:
                    ResChange=int(input("Enter the desired change in resources."))
                    EcName.update_resources(ResChange)
                elif choice==9:
                    Gens=int(input("How many generations would you like to simulate?"))
                    Res=int(input("How many resources are available?"))
                    simulate_generations(EcName,Gens,Res)
        menu()
        choice=int(input("Please select an action."))
        while choice not in n:
            choice=int(input("Selection must be a number between 1-10, please pick again."))
main()
