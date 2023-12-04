     # formating style1
#def to_celsius(x):
#     return (x-32)*5/9
# for x in range(0, 101, 10):
#     print("{:>3} F | {:>6.2f} c".format(x, to_celsius(x))) # 3 and 6 indicate the spacing and .2f indicates two decimal floating point

#another formating style 2.
# price = 7.5
# with_tax = price*1.09
# print(price, with_tax)
# #another formating style 3.
# price = 7.5
# with_tax = price*1.09
# print("base price: ${:.2f}, with_tax: ${:.2f}".format(price, with_tax))
     #1...# enumerate function to iterate over lists and tubles!!!
# winers = ["Ashly", "Angela", "Rees"]
# for index, person in enumerate(winers):
#     print("{} - {}".format(index+1, person))

# animals = ["lion", "dolphin", "zebra", "giraffe"]
# chars = 0
# for animal in animals:
#     chars +=len(animal)
#     #print("total chatacters: {}, average length: {}".format(chars, chars/len(animals)))
# print("total chatacters: {}, average length: {}".format(chars, chars/len(animals)))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{}<{}>".format(email, name))
    return result
print(full_emails([("alex@example.com", "alex diago"), ("wagnewm@example.com", "wagnew moges")]))