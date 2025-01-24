import unittest

def is_vowel(letter): #Fråga 1
    lista = ["a","e","i","o","u","y","å","ä","ö"]
    if letter in lista:
        return True
    else:
        return False

def grade_evaluation(score):   #Fråga 2
    if score >= 95:
        return "A"
    elif score >= 70:
        return "C"
    elif score > 50:
        return "E"
    else:
        return "F"

def temperature_check(temp):  #Fråga 3
    if temp >30:
        return "varm"
    elif temp > 10:
        return "lagom"
    else:
        return "kall"

def factorial(n):   #Fråga 4
    count = 1
    for i in range(n):
        count += count * i
    return count

def sum_of_even_numbers(n):  #Fråga 5
    sum = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            sum += i
    return sum

def print_stars(n):
    pyramid = []
    for i in range(1, n+1):
        spaces = ' ' * (n - i)        # Beräkna antalet mellanslag för att centrera stjärnorna
        stars = '*' * (2 * i - 1)     # Beräkna antalet stjärnor på varje rad
        pyramid.append(spaces + stars + spaces)  # Lägg till raden i listan
    return pyramid

def count_occurrences(lst, elem):   #Fråga 7
        x = lst.count(elem)
        return x

def remove_duplicates(lst):   #Fråga 8
    return list(dict.fromkeys(lst))

def merge_dictionaries(dict1, dict2):   #Fråga 9
    new_dict = {}
    new_dict.update(dict1)
    new_dict.update(dict2)
    return new_dict

def find_key_by_value(my_dict, value):   #Fråga 10
    for key,val in my_dict.items():
        if val == value:
            return key
        
        
class TestPythonTasks(unittest.TestCase):

    # If/else uppgifter

    def test_is_vowel(self):
        """
        Uppgift 1: Kontrollera om en bokstav är en vokal eller konsonant
        """
        self.assertTrue(is_vowel('a'))
        self.assertTrue(is_vowel('e'))
        self.assertFalse(is_vowel('b'))

    def test_grade_evaluation(self):
        """
        Uppgift 2: Bedöm betyg (A-F) baserat på en poäng (0-100)
        """
        self.assertEqual(grade_evaluation(95), 'A')
        self.assertEqual(grade_evaluation(70), 'C')
        self.assertEqual(grade_evaluation(50), 'F')

    def test_temperature_check(self):
        """
        Uppgift 3: Kontrollera om temperaturen är kall, varm eller lagom
        """
        self.assertEqual(temperature_check(5), "kall")
        self.assertEqual(temperature_check(22), "lagom")
        self.assertEqual(temperature_check(35), "varm")

    # Loopar uppgifter

    def test_factorial(self):
        """
        Uppgift 4: Beräkna fakulteten av ett tal
        """
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_sum_of_even_numbers(self):
        """
        Uppgift 5: Summera alla jämna tal upp till ett givet tal
        """
        self.assertEqual(sum_of_even_numbers(10), 30)  # 2 + 4 + 6 + 8 + 10
        self.assertEqual(sum_of_even_numbers(5), 6)  # 2 + 4

    def test_print_stars(self):
        """
        Uppgift 6: Skriv ut en pyramid av stjärnor (returnera som lista med strängar)
        """
        self.assertEqual(print_stars(3), ['  *  ', ' *** ', '*****'])

    # Listor uppgifter

    def test_count_occurrences(self):
        """
        Uppgift 7: Räkna antalet förekomster av ett element i en lista
        """
        self.assertEqual(count_occurrences([1, 2, 2, 3, 3, 3], 2), 2)
        self.assertEqual(count_occurrences(['a', 'b', 'a', 'c', 'a'], 'a'), 3)

    def test_remove_duplicates(self):
        """
        Uppgift 8: Ta bort dubbletter från en lista
        """
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates(['a', 'b', 'a', 'c', 'b']), ['a', 'b', 'c'])

    # Dict uppgifter

    def test_merge_dictionaries(self):
        """
        Uppgift 9: Slå ihop två dictionaries
        """
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), {'a': 1, 'b': 3, 'c': 4})

    def test_find_key_by_value(self):
        """
        Uppgift 10: Hitta en nyckel baserat på ett värde i en dictionary
        """
        my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
        self.assertEqual(find_key_by_value(my_dict, 2), 'banana')
        self.assertEqual(find_key_by_value(my_dict, 5), None)

if __name__ == '__main__':
    unittest.main()
