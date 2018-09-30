# Agent Based Model (ABM)

The files for this assignment are: agentframework.py, environment.csv, in.txt, model.py and store.csv
They should be kept together in a sinlge directory during execution. The file agentframework.py and model.py should be opened together and model.py executed to see the output.

This is an ABM with 10 agents randomly moving about a 100x100 pixel environment eating/storing a hypothetical resource that exists in the environment, sharing resources with their neighbours. The environment is created by reading a raster data file in.txt as a list. The environment's geometry is a torus so it allows agents that moves off the edge to reappear on the opposite side of the environment.

The file agentframework.py implements a class to encapsulate all the attributes and behaviour of the agents.

The environment and agents' activities are plotted using the matplotlib.pyplot module.

Partial codes for the assignment were supplied with the course notes and additional enhancements were added such as:

1. write out the environment as a text csv file, environment.csv

2.wite out the total amount of resources stored by all agent to a file stores.csv and allow this information to be appended to the file on each run.

3.Allow agents to eat units of resources remaining in the environment after each agent has eaten 10 units. Agents will eat remaining resources if there are less than 10 units but they should not leave the units of resources in the environment with a negative value.

4.Agents eating more than 100 units of resources are greedy and will regurgitate the excess.



