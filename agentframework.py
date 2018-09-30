# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:04:04 2018

@author: 201181205
"""

#import Python modules that will be used
import random
import math



class Agent():
    
    
    def __init__(self, environment,agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
		
		
	#instance method move. The environment is a torus 
    #agents will reappear on the opposite side of the environment 
    #if they wander of the edge. This is implemented with the % operator
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    #method eat - agents eating causes the store to increase by 10
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
           self.environment[self.y][self.x] -= 10
           self.store += 10
    #addition to the eat method - presently agents eat only 10 units, so allow
    #agents to eat any remaining units, if there is less than 10 units  left
    #without leaving a negative value. 
    #check for the condition that there is less than 10 units and more than 0
    #then get the agent to eat up left overs
        elif self.environment[self.y][self.x] > 0 and self.environment[self.y][self.x] < 10 :
             self.environment[self.y][self.x] -= 1
             self.store += 1
             
             
    #method greed_regurgitate         
    #agents who eats more than 100 units are classed as greedy and will regurgitate 
    #the extra units eaten
    def greed_regurgitate(self):
         if self.store >= 100:
             self.environment[self.y][self.x] += self.store
             self.store -= self.store
    
    def share_with_neighbours(self, neighbourhood):
        # Loop through the agents in self.agents .
        for agent in self.agents:
        # Calculate the distance between self and the current other agent:
            dist = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if dist <= neighbourhood:
                # Sum self.store and agent.store .
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                ave = sum/2
                # self.store = average
                self.store = ave
                # agent.store = average
                agent.store = ave
                print("sharing" + str(dist) + " " + str(ave))                

    def distance_between(self, agent):
        return(math.sqrt(((self.x - agent.x)**2) + ((self.y - agent.y)**2)))

# End if
# End loop           
            
    