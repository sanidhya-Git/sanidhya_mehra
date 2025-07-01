import matplotlib.pyplot as plt
sem1 = [75, 80, 85, 90, 95]
sem2 = [78, 82, 88, 92, 96]
students = ['S1', 'S2', 'S3', 'S4', 'S5']

plt.plot(students, sem1, label='Semester 1', linestyle='--', marker='o')
plt.plot(students, sem2, label='Semester 2', linestyle='-', marker='x')
plt.title('Semester Comparison')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.legend()
plt.grid(True)
plt.show()
