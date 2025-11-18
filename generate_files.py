# generate_files.py
"""
Generates all required input files for the disease modelling project:
- locations.txt
- agents.txt
- monday.txt → sunday.txt
- event_files_list.txt

"""

# ------------------------
# LOCATIONS
# ------------------------
with open("locations.txt", "w") as f:
    f.write("3\n")
    f.write("Location Index\n")
    for i in range(3):
        f.write(f"{i}\n")

# ------------------------
# AGENTS
# ------------------------
header = "Agent Index: Type: Grade"

with open("agents.txt", "w") as f:
    f.write("50\n")                # your project uses 50 agents
    f.write(header + "\n")

    # create 50 agents, each with a 'Type' and 'Grade'
    for agent_id in range(50):
        grade = (agent_id // 5) + 1
        f.write(f"{agent_id}: Student:Grade {grade}\n")

# ------------------------
# EVENT FILES (WEEKENDS)
# ------------------------
event_header = "Location Index:Agents"

for filename in ["saturday.txt", "sunday.txt"]:
    with open(filename, "w") as f:
        f.write("0\n")                # 1 location
        f.write(event_header + "\n")
        f.write("0:\n")               # location 0 has no assigned agents

# ------------------------
# EVENT FILES (WEEKDAYS)
# ------------------------
weekday_files = [
    "monday.txt",
    "tuesday.txt",
    "wednesday.txt",
    "thursday.txt",
    "friday.txt",
]

for filename in weekday_files:
    with open(filename, "w") as f:
        f.write("3\n")                # 3 locations
        f.write(event_header + "\n")
        for loc in range(3):
            f.write(f"{loc}:\n")      # empty (you can manually fill your Wed file)

# ------------------------
# EVENT FILES LIST
# ------------------------
with open("event_files_list.txt", "w") as f:
    for name in weekday_files:
        f.write(f"<{name}>\n")
    f.write("<saturday.txt>\n")
    f.write("<sunday.txt>\n")
