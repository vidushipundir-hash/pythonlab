condition = "moderate"   # critical / moderate / normal
age = 70

if condition == "critical":
    priority = "High Priority"
elif condition == "moderate":
    priority = "Medium Priority"
else:
    priority = "Low Priority"

if age > 65 and condition == "moderate":
    priority = "High Priority (Upgraded)"

print("Patient Priority:", priority)