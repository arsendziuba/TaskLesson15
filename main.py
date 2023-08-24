# def is_palindrome(s):
#     s = s.lower()  # Перетворимо рядок до нижнього регістру для порівняння без врахування регістру
#     s = ''.join(filter(str.isalnum, s))  # Видалимо всі не-буквено-цифрові символи
#     return s == s[::-1]  # Порівняємо рядок із його реверсом
#
# input_string = input("Введіть рядок: ")
# if is_palindrome(input_string):
#     print("Це паліндром!")
# else:
#     print("Це не паліндром.")

# def increase_even_numbers(numbers):
#     new_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             new_numbers.append(num + 1)
#         else:
#             new_numbers.append(num)
#     return new_numbers
#
#
# input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = increase_even_numbers(input_numbers)
# print(result)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# number = int(input("Введіть число: "))
# result = factorial(number)
# print(f"Факторіал числа {number} дорівнює {result}")

# def are_anagrams(str1, str2):
#     str1 = str1.lower()
#     str2 = str2.lower()
#
#     str1 = ''.join(sorted(str1))
#     str2 = ''.join(sorted(str2))
#
#     return str1 == str2
#

# string1 = input("Введіть перший рядок: ")
# string2 = input("Введіть другий рядок: ")
#
# if are_anagrams(string1, string2):
#     print("Ці рядки є анаграмами!")
# else:
#     print("Ці рядки не є анаграмами.")
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#
#     return True
#
#
#
# num = int(input("Введіть число: "))
# if is_prime(num):
#     print("Це число є простим.")
# else:
#     print("Це число не є простим.")

# def remove_duplicates(input_list):
#     unique_list = []
#     for item in input_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list
#
#
# input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# result = remove_duplicates(input_list)
# print(result)

# def fibonacci_sequence(n):
#     fib_sequence = [0, 1]
#
#     while fib_sequence[-1] + fib_sequence[-2] <= n:
#         next_fib = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_fib)
#
#     return fib_sequence
#
#
#
# number = int(input("Введіть число n: "))
# fib_series = fibonacci_sequence(number)
# print("Ряд Фібоначчі до числа", number, ":", fib_series)

# def count_vowels_and_consonants(input_string):
#     vowels = "aeiouAEIOU"
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     vowel_count = 0
#     consonant_count = 0
#
#     for char in input_string:
#         if char in vowels:
#             vowel_count += 1
#         elif char in consonants:
#             consonant_count += 1
#
#     return vowel_count, consonant_count
#
#
# text = input("Введіть рядок: ")
# vowels, consonants = count_vowels_and_consonants(text)
# print("Кількість голосних букв:", vowels)
# print("Кількість приголосних букв:", consonants)

# def calculate_average(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#
#     if count == 0:
#         return None
#
#     average = total / count
#     return average
#
#
#
# input_numbers = [2, 4, 6, 8, 10]
# average_value = calculate_average(input_numbers)
#
# if average_value is not None:
#     print("Середнє арифметичне:", average_value)
# else:
#     print("Список порожній.")

# def transform_string(input_string):
#     words = input_string.split()
#     transformed_words = []
#
#     for word in words:
#         if len(word) > 1:
#             transformed_word = word[0].upper() + word[1:-1].lower() + word[-1].upper()
#         else:
#             transformed_word = word.upper()
#         transformed_words.append(transformed_word)
#
#     return ' '.join(transformed_words)
#
#
#
# input_string = input("Введіть рядок: ")
# transformed_result = transform_string(input_string)
# print("Результат:", transformed_result)

# def square_numbers(numbers):
#     squared_list = [num ** 2 for num in numbers]
#     return squared_list
#

# input_numbers = [1, 2, 3, 4, 5]
# result = square_numbers(input_numbers)
# print(result)

# def is_palindrome(lst):
#     reversed_lst = lst[::-1]  # Створюємо обернений список
#     return lst == reversed_lst
#

# input_list = [1, 2, 3, 2, 1]
# if is_palindrome(input_list):
#     print("Цей список є паліндромом!")
# else:
#     print("Цей список не є паліндромом.")

# def sum_of_digits(number):
#     total_sum = 0
#     while number > 0:
#         total_sum += number % 10
#         number //= 10
#     return total_sum
#
#
# num = int(input("Введіть число: "))
# result = sum_of_digits(num)
# print("Сума цифр числа:", result)

# def sort_numbers(numbers):
#     sorted_list = sorted(numbers)
#     return sorted_list
#
#
# input_list = [5, 2, 9, 1, 7]
# sorted_result = sort_numbers(input_list)
# print(sorted_result)

# def is_perfect_number(number):
#     if number <= 0:
#         return False
#
#     divisors = [1]
#
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             divisors.append(i)
#             if i != number // i:
#                 divisors.append(number // i)
#
#     return sum(divisors) == number



# num = int(input("Введіть число: "))
# if is_perfect_number(num):
#     print("Це число є досконалим.")
# else:
#     print("Це число не є досконалим.")
#
