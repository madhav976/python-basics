students = """Name          Grade
Alice         85
Bob           42
Charlie       91
Diana         37
Eve           76
"""

def createFile():
    with open("students.txt", "w") as file:
        file.write(students)

def checkGrades(studentsFile, failedFile):
    with open(studentsFile, "r+") as sfile:
        with open(failedFile, "a+") as ffile:

            lines = sfile.readlines()
            header = lines[0]

            
            ffile.write(header)

            
            sfile.seek(0)
            sfile.write(header)

            for line in lines[1:]:
                name, grade = line.split()
                if int(grade) < 50:
                    ffile.write(line)   
                else:
                    sfile.write(line)   

            sfile.truncate()

def displayResults(studentsFile, failedFile):
    with open(studentsFile, "r") as sfile:
        print("Passing Students:")
        print(sfile.read())

    with open(failedFile, "r") as ffile:
        print("Failed Students:")
        print(ffile.read())


createFile()
checkGrades("students.txt", "failed.txt")
displayResults("students.txt", "failed.txt")
