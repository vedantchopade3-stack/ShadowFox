total_jumping_jacks = 100
completed = 0

while completed < total_jumping_jacks:

    # Perform 10 jumping jacks
    completed += 10
    print("You completed", completed, "jumping jacks.")

    # If all 100 are completed
    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    # Ask if user is tired
    tired = input("Are you tired? (yes/y or no/n): ")

    if tired == "yes" or tired == "y":

        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ")

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break

    # Show remaining jumping jacks
    remaining = total_jumping_jacks - completed
    print(remaining, "jumping jacks remaining.\n")