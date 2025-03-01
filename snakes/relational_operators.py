number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))

def get_relational():
    results = [] 

    if number1 == number2:
        results.append(f"{number1} == {number2}")
    if number1 != number2:
        results.append(f"{number1} != {number2}")
    if number1 > number2:
        results.append(f"{number1} > {number2}")
    if number1 < number2:
        results.append(f"{number1} < {number2}")
    if number1 >= number2:
        results.append(f"{number1} >= {number2}")
    if number1 <= number2:
        results.append(f"{number1} <= {number2}")

    return results  

relational_results = get_relational()
for result in relational_results:
    print(result)