import contact_tracing
import random
import datetime

id = input("Welcome to Covid City. What is your id? ")
while (id.isdigit() == False):
    print("Your id must be a number")
    id = input("Welcome to Covid City. What is your id? ")

print("We start on " + contact_tracing.currentDate.strftime("%m/%d/%Y"))

def encounter():
    randomEncounter = random.randint(0, 10000)
    while (randomEncounter == id):
        randomEncounter = random.randint(0, 10000)
    contact_tracing.updateData(id, randomEncounter)
    print("You ran into id: " + str(randomEncounter))

def runDay():
    contact_tracing.garbageCollect()
    numEncounters = random.randint(1, 4)
    for i in range(numEncounters):
        encounter()
    print("End of day on " + contact_tracing.currentDate.strftime("%m/%d/%Y"))
    response = input("Would you like to self-report? (y/n)")
    while (response != 'y' and response != 'n'):
        response = input("Would you like to self-report? (y/n)")
    if (response == 'y'):
        print("Please self-isolate immediately")
        contact_tracing.selfReport(id)
    if (response == 'n'):
        print("Another day, another dollar")
        contact_tracing.currentDate += datetime.timedelta(days=(1))
        runDay()

runDay()

    
