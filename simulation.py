import contact_tracing
import random
import datetime

pop_size = input("How many people live in Covid City? ")
while (pop_size.isdigit() == False or int(pop_size) < 2):
    print("Covid City must have an integer population of at least 2")
    pop_size = input("How many people live in Covid City? ")

id = input("Welcome to Covid City. What is your id? ")
while (id.isdigit() == False or int(id) > int(pop_size)):
    print("Your id must be a number and smaller than Covid City's population")
    id = input("Welcome to Covid City. What is your id? ")
print("We start on " + contact_tracing.currentDate.strftime("%m/%d/%Y"))

def encounter():
    randomEncounter = random.randint(0, int(pop_size))
    while (randomEncounter == int(id)):
        randomEncounter = random.randint(0, int(pop_size))
    contact_tracing.updateData(int(id), randomEncounter)
    print("You ran into id: " + str(randomEncounter))

def runDay():
    print("\nToday is " + contact_tracing.currentDate.strftime("%m/%d/%Y"))
    contact_tracing.garbageCollect()
    numEncounters = random.randint(1, 4)
    for i in range(numEncounters):
        encounter()
    print("End of day on " + contact_tracing.currentDate.strftime("%m/%d/%Y"))
    response = input("Would you like to self-report? (y/n) ")
    while (response != 'y' and response != 'n'):
        response = input("Would you like to self-report? (y/n) ")
    if (response == 'y'):
        print("Please self-isolate immediately")
        contact_tracing.selfReport(int(id))
    if (response == 'n'):
        contact_tracing.currentDate += datetime.timedelta(days=(1))
        # Random person gets infected every day, including you
        randId = random.randint(0, int(pop_size))
        print(str(randId) + " was infected")
        if (randId == int(id)):
            print("Please self-isolate immediately")
            contact_tracing.selfReport(int(id))
        else:
            infected = contact_tracing.selfReport(randId)
            if (infected and int(id) in infected):
                print("You may have had Covid Exposure!")
                print("Please see your doctor and consdier self-isolating")
            else:
                print("Another day, another dollar")
                runDay()

runDay()

    
