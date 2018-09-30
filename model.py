# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:04:04 2018

@author: 201181205
"""

#import Python modules that will be used
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import agentframework
import csv


#List to store the environment
environment = []
#List to store the agents
agents = []
#List to store the resources in store
storelist = []
#The total number of agents in the simulation
num_of_agents = 10

#Total number of iterations for moving agents
num_of_iterations = 100

neighbourhood = 20


#open the text file for the environment
try:
    f = open('in.txt', newline='')
except IOError:
    print ("Could not read file:", 'in.txt')
    exit()
    
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
print(environment)
f.close()

fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

#Create the agents
#Get the environment and agents into each agent
for i in range(num_of_agents):
	agents.append(agentframework.Agent(environment,agents))

carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
# Move the agents in random directions, agents will eat/store resources
#some agents eat resourses left over after all agents have eaten
#agents share resources with neighbours,.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].greed_regurgitate()
        agents[i].share_with_neighbours(neighbourhood)
        

#plots the y and x coordinates and display these for the environment
plt.ylim(0, 99)
plt.xlim(0, 99)
plt.imshow(environment)

#randomly scatters the agents within the environment according to y and x coordinates
for i in range(num_of_agents):
	plt.scatter(agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation.FuncAnimation(fig, update, interval=1)

plt.show()
    
#print the environment to a csv file with the name environment.cvs
try:
    f1 = open('environment.csv', 'w', newline='')
except IOError:
    print ("Could not read file:", 'environment.csv')
    exit()
    
f1 = open('environment.csv', 'w', newline='') 
writer = csv.writer(f1, delimiter=' ')
for row in environment:		
	writer.writerow(row)		# List of values.
f1.close()

#wprint the total amount stored by all agents on a line
#append the data to the file, rather than clearing it each time the program runs
#this is achieved by changing the mode 'w' to 'a+'
#also prints the location of  
try:
    f2 = open('store.csv', 'a+', newline='')
except IOError:
    print ("Could not read file:", 'store.csv')
    exit()

f2 = open('store.csv', 'a+', newline='') 
writer = csv.writer(f2, delimiter=' ')
total_stored = 0
for agent in agents:
    storelist.append(agent.store)
    total_stored += agent.store
writer.writerow(storelist)		# List of values.
    
print("The Total in the store is :" + str(total_stored))
f2.close()


