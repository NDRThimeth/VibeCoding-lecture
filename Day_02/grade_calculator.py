# Grade Calculator Script

while True:
    # Get student name
    name = input("\nEnter student's name (or 'Exit' to quit): ")
    
    # Check for exit condition
    if name.lower() == "exit":
        print("Exiting program. Goodbye!")
        break
    
    # Get 3 subject marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))
    
    # Calculate average
    average = (mark1 + mark2 + mark3) / 3
    
    # Display result with grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    # Print formatted output
    print("\n" + "-" * 30)
    print(f"Name   : {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade  : {grade}")
    print("-" * 30)  