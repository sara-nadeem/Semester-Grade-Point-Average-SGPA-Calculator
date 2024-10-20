def getdata(course, Marks, Crhrs, size):
    for i in range(size):
        course[i] = input("Enter course name without space:\n")
        Marks[i] = int(input("Enter marks between 0 and 100:\n"))
        
        if Marks[i] < 0 or Marks[i] > 100:
            print("User has entered invalid marks\n")
            break
        
        Crhrs[i] = int(input("Enter credit hours:\n"))

def assigngrades(Marks, grade, scores, size):
    for i in range(size):
        if 90 <= Marks[i] <= 100:
            grade[i] = "A+"
            scores[i] = 4.00
        elif 86 <= Marks[i] <= 89:
            grade[i] = "A"
            scores[i] = 4.00
        elif 82 <= Marks[i] <= 85:
            grade[i] = "A-"
            scores[i] = 3.67
        elif 78 <= Marks[i] <= 81:
            grade[i] = "B+"
            scores[i] = 3.33
        elif 74 <= Marks[i] <= 77:
            grade[i] = "B"
            scores[i] = 3.00
        elif 70 <= Marks[i] <= 73:
            grade[i] = "B-"
            scores[i] = 2.67
        elif 66 <= Marks[i] <= 69:
            grade[i] = "C+"
            scores[i] = 2.33
        elif 62 <= Marks[i] <= 65:
            grade[i] = "C"
            scores[i] = 2.00
        elif 58 <= Marks[i] <= 61:
            grade[i] = "C-"
            scores[i] = 1.67
        elif 54 <= Marks[i] <= 57:
            grade[i] = "D+"
            scores[i] = 1.33
        elif 50 <= Marks[i] <= 53:
            grade[i] = "D"
            scores[i] = 1.00
        else:
            grade[i] = "F"
            scores[i] = 0.00

def getsgpa(Crhrs, size, scores, sgpa, crEnd):
    total_credit_hours = 17
    temp = 0.0
    
    for i in range(size):
        if scores[i] >= 1.00:
            crEnd += Crhrs[i]
    
    for i in range(size):
        temp += (scores[i] * Crhrs[i])
    
    sgpa[0] = temp / total_credit_hours

def printdata(course, grade, Marks, size, sgpa, crEnd):
    total_credit_hours = 17
    for i in range(size):
        print(f"{course[i]}: {Marks[i]}")
    
    print(f"Attempted total credit hours: {total_credit_hours}")
    print(f"Earned credit hours: {crEnd}")
    print(f"SGPA: {sgpa[0]}")

# Main function
def main():
    size = 8
    course = [''] * size
    Marks = [0] * size
    Crhrs = [0] * size
    grade = [''] * size
    scores = [0.0] * size
    crEnd = 0
    sgpa = [0.0]  # Using a list to pass by reference

    getdata(course, Marks, Crhrs, size)
    assigngrades(Marks, grade, scores, size)
    getsgpa(Crhrs, size, scores, sgpa, crEnd)
    printdata(course, grade, Marks, size, sgpa, crEnd)

if __name__ == "__main__":
    main()
