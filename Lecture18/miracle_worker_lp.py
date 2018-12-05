# import PuLP
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Miracle Worker", LpMaximize)

# Create problem variables
x=LpVariable("Medicine_1_units",0,None,LpInteger)
y=LpVariable("Medicine_2_units",0, None, LpInteger)

# The objective function is added to 'prob' first
prob += 25*x + 20*y, "Health restored; to be maximized"
# The two constraints are entered
prob += 3*x + 4*y <= 25, "Herb A constraint"
prob += 2*x + y <= 10, "Herb B constraint"

# The problem data is written to an .lp file
prob.writeLP("MiracleWorker.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()


for v in prob.variables():
    print(v.name, "=", v.varValue)