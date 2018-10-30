# Role-Assignment
## A **Role Assignment** Module for automatic allocation of tasks to available bots in a dynamic soccer game enviornment.

STOx’s 2017 Team Description Paper http://wiki.robocup.org/images/6/67/Robocupssl2018-STOxs.pdf was used as a source for this creation. 

This new methodology has the following advantages:
- automatic assignment of agents to tasks, avoiding situations where missing agents might be assigned with tasks.
- optimal agents-tasks assignments, where the traveled distance of each agent is the lowest possible.
- creation of defensive and attacking plays that are automatically created by the system on the run in contrast to preprogrammed plays. 

In our approach we have defined a number of tasks that must be individually performed by bots in specific situations and these tasks are associated with a particular point in the field. For example a robot that must perform the task of robot-to-robot marking must stay in a position influenced by the position of the robot to be marked.

The framework includes two main modules, namely **Game Analyzer Module** and **Optimal Assignment Module**. The former is in charge of deciding which tasks need to be done depending on the current game state and the available agents, together with their locations. The module receives the complete set of possible tasks, the current game state and analyzes which tasks should be performed and the subset of agents that will participate in the assignment.

The optimal assignment module receives such information and outputs an assignment of agents to tasks such that the agents have to move minimum distance to implement the task using a cost function. The cost function used by my team is influenced by the **Hungarian Algorithm** (for information about the algorithm https://www.topcoder.com/community/data-science/data-science-tutorials/assignment-problem-and-hungarian-algorithm/ ).
 
The set of the **tasks** are as follows: 

-*Defender:* A task where the agents are required to locate near the defense area edge as in a wall, blocking potential shots to the goal.

-*Ball Handler:* This task is assigned to an agent that will be performing activities related with the ball. For example, in a defending situation, it could be the agent that will act as wall when the opponent team will kick the ball. In a defending free kick situation it must act as a wall. When attacking, in a free kick situation, the ball handler will be the agent that will kick the ball. In the situation that two agents have been assigned the task of being a ball handler in a defensive free kick situation, they must create a two agent wall.

-*Marker:* This is a task related to defending situations. Some threatening opponents  will be assigned markers to perform robot-to-robot mark.

-*Supporter:* In offensive situations, the supporters are agents that need to go to locations within the field to potentially receive passes. 

-*Attacker:* This task is assigned to an agent with the ball's possession. This agent can dribble the ball and will subsequently perform passes.

-*Distractor:* This task is assigned to agents that will perform distracting moves during the game.

-*Clearer:* This is usually assigned to agents in charge of clearing the ball near the defensive area.
