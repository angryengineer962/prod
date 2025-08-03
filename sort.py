#!/bin/python3
#--------------------------------------------------------
# Program by Bruce Wayne
#
#
# Version   Date    Info
# 1.0       2023    Initial Version
# 1.1       2024    Few simple changes
#--------------------------------------------------------

# List Sorting Examples in Python

def main():
    # 1. Basic number sorting
    numbers = [5, 2, 9, 1, 5, 6]
    print("Original numbers:", numbers)
    
    # Using sorted() - creates new list
    sorted_numbers = sorted(numbers)
    print("Sorted (new list):", sorted_numbers)
    print("Original unchanged:", numbers)
    
    # Using sort() - modifies original
    numbers.sort()
    print("Original after sort():", numbers)
    
    # 2. Reverse sorting
    numbers.sort(reverse=True)
    print("Reverse sorted:", numbers)
    
    # 3. String sorting
    fruits = ['banana', 'Apple', 'cherry', 'date']
    print("\nOriginal fruits:", fruits)
    fruits.sort()  # Case-sensitive
    print("Case-sensitive sort:", fruits)
    fruits.sort(key=str.lower)  # Case-insensitive
    print("Case-insensitive sort:", fruits)
    
    # 4. Sorting with custom key
    words = ['apple', 'banana', 'kiwi', 'orange']
    words.sort(key=len)  # Sort by length
    print("\nWords sorted by length:", words)
    
    # 5. Sorting complex objects
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    print("\nOriginal people:", people)
    
    # Sort by age
    people_sorted_by_age = sorted(people, key=lambda x: x['age'])
    print("Sorted by age:", people_sorted_by_age)
    
    # Sort by name length then alphabetically
    people_sorted_complex = sorted(people, key=lambda x: (len(x['name']), x['name']))
    print("Sorted by name length then name:", people_sorted_complex)

if __name__ == "__main__":
    main()
