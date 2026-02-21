
# Problem Statement: Compute the average number of books each student has read this year

student_books_list = [5,3,0,7,2,4,6,8,1,3,9,5,2,6,7,4]
num_of_students = len(student_books_list)
print(f"There are {num_of_students} students in the class.")

# sum /num of students 
items_at_index_0 = student_books_list[0]
total_books = sum(student_books_list)
average_books = total_books / num_of_students
print(f"Average books read per student: {average_books}")
# The average number of books read per student is 4.5
# in the above code, we first calculate the total number of books read by summing up all the values in the student_books_list. Then, we divide this total by the number of students to get the average number of books read per student. Finally, we print out the result.
# Note: The average number of books read per student is 4.5, which means that on average, each student has read 4.5 books this year.
# in this example in course that sole it same to this problem solve