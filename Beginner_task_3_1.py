justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
#num  of members in the justice league
print(len(justice_league))
#Adding new members to the justice league
a=["Batgirl","Nightwing"]
justice_league.extend(a)
print(justice_league)
# Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:")
print(justice_league)
# Separate Aquaman and Flash by inserting Green Lantern between them
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Green Lantern")
print("After separating Aquaman and Flash:")
print(justice_league)
# Replace old team with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl",
                  "Martian Manhunter", "Green Arrow"]
print("New Justice League team:")
print(justice_league)
# Sort alphabetically
justice_league.sort()
print("Justice League team in alphabetical order:")
print(justice_league)