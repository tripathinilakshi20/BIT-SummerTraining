# Day 4 Assignment - Python Data Structures

# Question 1: List Append
students = ['Rohit', 'Sneha', 'Kavya', 'Manish', 'Vikram']
students.append('Aarti')
print(students)

# Question 2: Tuple Indexing
cities = ('Prayagraj', 'Varanasi', 'Kanpur', 'Agra', 'Noida')
print(cities[2])

# Question 3: Set Add
courses = {'Python', 'Java', 'C++', 'Web Development'}
courses.add('AI')
print(sorted(courses))

# Question 4: Dictionary Access
student = {
    'name': 'Priyanshu Upadhyay',
    'course': 'Python Data AI',
    'batch': 'B',
    'city': 'Lucknow'
}
print(f"Name: {student['name']}")
print(f"Course: {student['course']}")

# Question 5: Filter Even Numbers
numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Question 6: Count Word Frequency
words = ["python", "ai", "python", "data", "ai", "python"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Question 7: Nested Student Dictionary
student_info = {
    'name': 'Priyanshu',
    'marks': {'python': 88, 'data': 92},
    'skills': ['Python', 'SQL']
}
student_info['skills'].append('Pandas')
print(student_info)

# Question 8: Common Elements
python_students = {"Aman", "Priya", "Raj", "Neha"}
ai_students = {"Raj", "Neha", "Vivek", "Shalu"}
common_students = python_students & ai_students
print(sorted(common_students))