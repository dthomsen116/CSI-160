import numbers
import random
import math
from urllib.parse import urlparse


def number_of_zeros(grades):
    grades = [75, 82.5, 97, 0, 87.5]
    x = 0

    for (i) in grades:

        if i == 0:
            x =+1
            print(x)
        else:
            x
            print(x)

    #return (int) - the number of 0 % grades



def median(numbers):
    list_length = len(numbers)
    numbers.sort()

    if list_length % 2 == 0:
        num1 = numbers[list_length // 2]
        num2 = numbers[list_length // 2 - 1]
        med_value = (num1 + num2) / 2
    else:
        med_value = numbers[list_length // 2]
    return med_value

    pass


def top_quartile(list):
    list.sort()

    leng = len(list)
    topquart = (math.ceil(leng / 4)) * 3

    if topquart > leng:
        topquart = (round(leng / 4)) * 3
        print(list[topquart:])
    else:
        topquart = (math.ceil(leng / 4)) * 3
        print(list[topquart:])
    """Return the top 25% of the grades in the supplied list of grades. Round up when determining how many grades to include in the top 25%.

    Hint: You will need to sort the list of grades

    params:
    grades (list of floats) Example [75, 82.5, 97, 0, 87.5]

    return (list of floats) - The top 25%
    """
    pass


def domain_name_extractor(url):
 domain = urlparse(url).netloc
 print(domain) # --> www.example.test



def test_number_of_zeros():
    print('Running number_of_zeros tests:')
    print('Test 1 passed -',
          number_of_zeros([75.0, 0.0, 97.0, 0.0, 87.5]) == 2)
    print('Test 2 passed -', number_of_zeros([]) == 0)


def test_median():
    print('Running median tests:')
    print('Test 1 passed -', median([10, 5, 8, 4, -1]) == 5)
    print('Test 2 passed -', median([10, 8, 4, -1]) == 6)


def test_top_quartile():
    print('Running top_quartile tests:')
    print('Test 1 passed -',
          top_quartile([97, 92.5, 84, 79, 67]) == [92.5, 97])
    print('Test 2 passed -', top_quartile([92.5, 86, 89, 75]) == [92.5])


def test_domain_name_extractor():
    print('Running domain_name_extractor tests:')
    print(
        'Test 1 passed -',
        domain_name_extractor('https://champlain.instructure.com/courses/8933')
        == 'champlain.instructure.com')
    print(
        'Test 2 passed -',
        domain_name_extractor('ftp://champlain.edu/myfile.pdf') ==
        'champlain.edu')


print('Running Unit Tests\n')
test_number_of_zeros()
print()
test_median()
print()
test_top_quartile()
print()
test_domain_name_extractor()
