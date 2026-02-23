# -------------------------------------------------
# Program Name : Check Subset
# Description  : This program checks whether
#                one set is subset of another.
# -------------------------------------------------

# Creating sets
setX = {1, 2}
setY = {1, 2, 3, 4}

# Checking subset condition
if setX.issubset(setY):
    print("setX is a subset of setY")
else:
    print("setX is NOT a subset of setY")