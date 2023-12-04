# def sum_positive_numbers(n):
#     # The base case is n being smaller than 1
#     if n < 1:
#         return 0

#     # The recursive case is adding this number to 
#     # the sum of the numbers smaller than this one.
#     return n + sum_positive_numbers(n-1)

# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15
# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n-1)
# x = factorial(10)
# print(x)
# def rows_asterisks(rows):
#     # Complete the outer loop range to control the number of rows
#     for x in range(1, rows +1): 
#         # Complete the inner loop range to control the number of 
#         # asterisks per row
#         for y in range(x): 
#             # Prints one asterisk and one space
#             print("*", end=" ")
#         # An empty print() function inserts a line break at the 
#         # end of the row 
#         print()


# rows_asterisks(5)
# # Should print the asterisk rows shown above
# num1 = 0
# num2 = 0

# for x in range(5):
#     num1 = x
#     for y in range(14):
#         num2 = y + 3

# print(num1 + num2)
# for x in range(1, 10, 3):
#     print(x)
# x = 1
# sum = 0
# while x <= 10:
#     sum += x
#     x += 1
# print(sum)
def counter(start, stop):
    y = start
    if y > stop:
        return_string = "Counting down: "
        while y >= stop: # Complete the while loop
           return_string +=str(y) # Add the numbers to the "return_string"
           if y > stop:
                return_string += ","
                y -=1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while y <= stop: # Complete the while loop
            return_string +=str(y) 
            # Add the numbers to the "return_string"
            if y < stop:
                return_string += ","
                y+=1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"