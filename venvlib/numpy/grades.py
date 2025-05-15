import numpy as np

students = np.random.randint(60, 100, size=(5,4))
print(students)

print()


averages = students.mean(axis=1)

print("Student 1:", students[0,:], "Average:", averages[0])
print("Student 2:", students[1,:], "Average:", averages[1])
print("Student 3:", students[2,:], "Average:", averages[2])
print("Student 4:", students[3,:], "Average:", averages[3])
print("Student 5:", students[4,:], "Average:", averages[4])
print()

assignments = students.mean(axis=0)

print("Assignment 1 Average:", assignments[0])
print("Assignment 2 Average:", assignments[1])
print("Assignment 3 Average:", assignments[2])
print("Assignment 4 Average:", assignments[3])

print()

print("Highest Grade", students.max())

print()

print("Failing Grades:", students[students < 70])

print()

print("All Grades", students.flatten())

max_avg = averages.max()

best = np.where(averages == max_avg)[0]

print(best)

for i in best:
     print("Top Student", i + 1, "Grades:", students[i], "Average:", averages[i])


curve = np.clip(students + 5, 0, 100)
print("Curved Grades:", '\n' ,curve)