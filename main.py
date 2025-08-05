import random

courses = ["Eagle City", "Alpina Forest", "Kanaloa Beach", "Vortex Valley", "Imperial Garden", "Green Country Club (Green C.C.)", "Balata Country Club (Balata C.C.)", "Nam Rong Bay C.C.", "Pine Hills G.C.", "Akigase Keikoku C.C."]
print(random.choice(courses))

courseholes = ["IN", "OUT"]
print(random.choice(courseholes))

teeType = ["Regular", "Long", "Championship"]
print(random.choice(teeType))

cuptype = ["Teeny", "Normal", "Mega", "Tornado"]
print(random.choice(cuptype))

courseVariant = ["Normal", "Mirrored"]
print("Course Variant: " + random.choice(courseVariant))

timeOfDay = ["Morning","Noon","Evening","Rain/Cloudy"]
print(random.choice(timeOfDay))

egRules = ["No hit within 15 sec.: +1", "Bunker: +1", "Use Power Mode: +1", "Super input: +1", "Rough: +1", "Hit a tree: +1",
"100% power: +1", "Backspin: +1", "Auto Impact", "Variable gauge speed", "Putt lines visible", "Gauge on the rampage",
"Gauge vanishes", "Auto Perfect Impact", "No spins allowed", "No woods allowed", "Gauge flag icon hidden",
"Ball landing cursor hidden", "Grid hidden", "No approach mode", "No wind", "Very strong wind", "Rain/cloudy",
"Strong wind", "Storm", "Constant downpour", "Super-Hard Pin"]
while True:
    rules = random.sample(egRules, k=2)
    if "No wind" in rules and "Very strong wind" in rules:
        continue
    print("\n".join(rules))
    break


#this is a com