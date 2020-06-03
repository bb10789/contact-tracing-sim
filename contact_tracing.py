import random
import time
import datetime

# Updated every day
currentDate = datetime.datetime(2020, 5, 11)

covid_data = dict()

# Person i has come into contact with person j
def updateData(i, j):
    if currentDate in covid_data.keys():
        covid_data_today = covid_data[currentDate]
        if i in covid_data_today.keys():
            covid_data[currentDate][i].append(j)
        else:
            covid_data[currentDate][i] = []
            covid_data[currentDate][i].append(j)
        if j in covid_data_today.keys():
            covid_data[currentDate][j].append(i)
        else:
            covid_data[currentDate][j] = []
            covid_data[currentDate][j].append(i)
    else:
        covid_data[currentDate] = dict()
        covid_data_today = covid_data[currentDate]
        if i in covid_data_today.keys():
            covid_data[currentDate][i].append(j)
        else:
            covid_data[currentDate][i] = []
            covid_data[currentDate][i].append(j)
        if j in covid_data_today.keys():
            covid_data[currentDate][j].append(i)
        else:
            covid_data[currentDate][j] = []
            covid_data[currentDate][j].append(i)

def garbageCollect():
    # Called every day, to remove unnecessary data from our database
    oldDate = currentDate - datetime.timedelta(days=15)
    if oldDate in covid_data.keys():
        covid_data.pop(oldDate)

def notify(i):
    # Notify user i that they've been in contact with a covid self-reportee in 
    # the past 2 weeks
    print('User ' + str(i) + ' was in contact with a covid self-reportee in the past 2 weeks')

def selfReport(i):
    # User i self-reports
    infected = []
    for k in range(15):
        date = currentDate - datetime.timedelta(days=(14-k))
        if date in covid_data.keys():
            if i in covid_data[date].keys():
                for j in covid_data[date][i]:
                    if (not (infected and j in infected)):
                        notify(j)
                        infected.append(j)
                    
    return infected

#quicktest [Uncomment to see for yourself]

if (__name__ == '__main__'):
    # Generate two weeks of spoofed data
    for i in range(14):
        # Simulate 4000 random interactions from a population of 20,000 that day
        for j in range(4000):
            interaction = random.sample(range(0, 20000), 2)
            updateData(interaction[0], interaction[1])
        currentDate = currentDate + datetime.timedelta(days=1)

    #Simulate 100 random self-reports
    for i in range(100):
        selfReport(random.randrange(0, 20000, 1))

