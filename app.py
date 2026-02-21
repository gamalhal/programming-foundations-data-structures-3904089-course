
student_books_list = [5, 3, 0, 7, 2, 4, 6, 8, 1, 3, 9, 5, 2, 6, 7, 4]
#frist  student read 3 more books
# , second student read 1 more books
# , third student read 2 more books
student_books_list[0] += 3
student_books_list[1] += 1 
student_books_list[2] += 2
# update the list with the new values
student_books_list.append(3)  # Adding a new student who read 3 books
student_books_list.append(5) # Adding another new student who read 5 books
# Average Calculation
total_books = 0
for individual_books in student_books_list:
  total_books += individual_books
print(total_books)

average_books = total_books / len(student_books_list)
print(f"The average number of books read per student is {average_books:.2f}")

