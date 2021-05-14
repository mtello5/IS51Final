"""
This program will determine the amount of grades, the average grade, and the percentage of grades above the average grade on a final exam.
Text file will be read and made into a list of intergers
Number of grades = length of list of intergers
Average grade = sum of grades / # of total grades
Percentage of grades above average = grades > average / # of total grades 
"""
"""
main() will open "Final.txt" and create it to a list of intergers

calculate_above_average() will get the number of grades, find average grade, and find percentage of grades above average


"""
def main():
    infile = open ("Final.txt", 'r')
    grades = [line.rstrip () for line in infile]
    infile.close()
    return grades
grades = main()
def calculate_percent_above_average():
    infile = open ("Final.txt", 'r')
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    average = sum(grades) / len(grades)
    num = 0
    for grade in grades:
        if grade > average:
            num += 1
    print("Number of grades:", len(grades))
    print("Average grade:", average)
    print("Percentage of grades above average: {0:.2f}%"
                    . format(100 * num / len(grades)))

main()
calculate_percent_above_average()