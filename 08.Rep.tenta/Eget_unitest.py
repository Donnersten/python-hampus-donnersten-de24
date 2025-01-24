import unittest

def check_number(number):   #Fråga 1
    if number == 0:
        return "noll"
    elif number < 0:
        return "negativt"
    elif number > 0:
        return "positivt"

def even_or_odd(num):  #Fråga 2
    if num % 2 == 0:
        return "jämnt"
    else:
        return "udda"

def age_group(age):   #Fråga 3
    if age <= 12:
        return "barn"
    elif 12 < age < 19:
        return "tonåring"
    else:
        return "vuxen"

def sum_to_100(): #Fråga 4
    sum = 0
    for i in range(1,101):
        sum += i 
    return sum

def countdown():  #Fråga 5
    sum = []
    for i in range(1,11):
        sum.append(i)
    sum.reverse()
    return sum

def multiplication_table(value):   #Fråga 6
    new_list = []
    for i in range(1,11):
        i = value * i
        new_list.append(i)
    return new_list

def find_max(lst):   #Fråga 7
    max_list = max(lst)
    return max_list

def reverse_list(lst): #Fråga 8
    lst.reverse()
    return lst

def get_student_grade(student_grades, name):    #Fråga 9
    return student_grades.get(name, "Betyg ej tillgängligt")

def update_dictionary(my_dict, key, value):    #Fråga 10
    my_dict[key] = value
    return my_dict

# If/else, loopar, listor och dict - uppgifter
class TestPythonTasks(unittest.TestCase):

    # If/else uppgifter

    def test_positive_negative_or_zero(self):
        """
        Uppgift 1: Kontrollera om ett tal är positivt, negativt eller noll
        """
        self.assertEqual(check_number(10), "positivt")
        self.assertEqual(check_number(-5), "negativt")
        self.assertEqual(check_number(0), "noll")

    def test_even_or_odd(self):
        """
        Uppgift 2: Kontrollera om tal är jämnt eller udda
        """
        self.assertEqual(even_or_odd(4), "jämnt")
        self.assertEqual(even_or_odd(7), "udda")

    def test_age_group(self):
        """
        Uppgift 3: Enkel ålderskontroll: Barn (0-12), tonåring (13-19), vuxen (20+)
        """
        self.assertEqual(age_group(10), "barn")
        self.assertEqual(age_group(16), "tonåring")
        self.assertEqual(age_group(25), "vuxen")

    # Loopar uppgifter

    def test_sum_to_100(self):
        """
        Uppgift 4: Summera alla tal från 1 till 100
        """
        self.assertEqual(sum_to_100(), 5050)

    def test_countdown(self):
        """
        Uppgift 5: Räkna ner från 10 till 1 och returnera listan med resultatet
        """
        self.assertEqual(countdown(), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_multiplication_table(self):
        """
        Uppgift 6: Skapa en multiplikationstabell för ett tal, returnera en lista med produkter
        """
        self.assertEqual(multiplication_table(3), [3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    # Listor uppgifter

    def test_find_max_in_list(self):
        """
        Uppgift 7: Hitta det största talet i en lista
        """
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-1, -2, -3, -4]), -1)

    def test_reverse_list(self):
        """
        Uppgift 8: Vänd på en lista
        """
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list(["a", "b", "c"]), ["c", "b", "a"])

    # Dict uppgifter

    def test_get_student_grade(self):
        """
        Uppgift 9: Hämta en students betyg från en dictionary
        """
        student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
        self.assertEqual(get_student_grade(student_grades, 'Alice'), 'A')
        self.assertEqual(get_student_grade(student_grades, 'Charlie'), 'C')

    def test_update_dictionary(self):
        """
        Uppgift 10: Lägg till en ny nyckel och värde i en dictionary
        """
        my_dict = {'apple': 1, 'banana': 2}
        self.assertEqual(update_dictionary(my_dict, 'orange', 3), {'apple': 1, 'banana': 2, 'orange': 3})

if __name__ == '__main__':
    unittest.main()
