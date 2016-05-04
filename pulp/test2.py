#!/usr/bin/env python
# @(#) $Jeannot: test1.py,v 1.11 2005/01/06 21:22:39 js Exp $

# Import PuLP modeler functions
from pulp import *

# A new LP problem
prob = LpProblem("test2", LpMinimize)

# Variables
# 0 <= x <= 4
xa1 = LpVariable("xa1", 0, None)
xa2 = LpVariable("xa2", 0, None)
xa3 = LpVariable("xa3", 0, None)
xb1 = LpVariable("xb1", 0, None)
xb2 = LpVariable("xb2", 0, None)
xb3 = LpVariable("xb3", 0, None)

# -1 <= y <= 1
#y = LpVariable("y", -1, 1)
# 0 <= z
#z = LpVariable("z", 0)
# Use None for +/- Infinity, i.e. z <= 0 -> LpVariable("z", None, 0)

# Objective
prob += 8*xa1 + 6*xa2 + 3*xa3 + 2*xb1 + 4*xb2 + 9*xb3 , "obj"
# (the name at the end is facultative)

# Constraints
prob += xa1 + xa2 + xa3 <= 70, "c1"
prob += xb1 + xb2 + xb3 <= 40, "c2"
prob += xa1 + xb1 >= 40, "c3"
prob += xa2 + xb2 >= 35, "c4"
prob += xa3 + xb2 >= 25, "c5"

#prob += x+z >= 10, "c2"
#prob += -y+z == 7, "c3"
# (the names at the end are facultative)

# Write the problem as an LP file
prob.writeLP("test2.lp")

# Solve the problem using the default solver
prob.solve()
# Use prob.solve(GLPK()) instead to choose GLPK as the solver
# Use GLPK(msg = 0) to suppress GLPK messages
# If GLPK is not in your path and you lack the pulpGLPK module,
# replace GLPK() with GLPK("/path/")
# Where /path/ is the path to glpsol (excluding glpsol itself).
# If you want to use CPLEX, use CPLEX() instead of GLPK().
# If you want to use XPRESS, use XPRESS() instead of GLPK().
# If you want to use COIN, use COIN() instead of GLPK(). In this last case,
# two paths may be provided (one to clp, one to cbc).

# Print the status of the solved LP
print("Status:", LpStatus[prob.status])

# Print the value of the variables at the optimum
for v in prob.variables():
	print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", value(prob.objective))