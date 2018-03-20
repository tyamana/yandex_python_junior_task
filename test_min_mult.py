import min_multiplication


def test_compute_min_multiplication_of_list_elements_1():
    test_list = [-3, 2, 5, 7, 11, -6, -23, 0, -9]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == -23 * 11) else print('Error test 1')


def test_compute_min_multiplication_of_list_elements_2():
    test_list = [3, 2, 5, 7, 11, 6, 0, 9]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == 0) else print('Error test 2')


def test_compute_min_multiplication_of_list_elements_3():
    test_list = [-3, -2, -5, -7, -11, -6, -4, -9, -32]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == 6) else print('Error test 3')


def test_compute_min_multiplication_of_list_elements_4():
    test_list = [-3, -2, -5, -7, -18, -6, 0, -9, 32]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == -18 * 32) else print('Error test 4')


def test_compute_min_multiplication_of_list_elements_5():
    test_list = [3, 2, 5, 7, -11, 6, 0, 9]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == -11 * 9) else print('Error test 5')


def test_compute_min_multiplication_of_list_elements_6():
    test_list = [-3, 0, 0, 0, -11, 0, 0, -9]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == 0) else print('Error test 6')


def test_compute_min_multiplication_of_list_elements_7():
    test_list = [3, 0, -9]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == 3 * -9) else print('Error test 7')


def test_compute_min_multiplication_of_list_elements_8():
    test_list = [3, -9]
    result = min_multiplication.compute_min_multiplication_of_list_elements(test_list)
    print('OK') if (result == -27) else print('Error test 8')


test_compute_min_multiplication_of_list_elements_1()
test_compute_min_multiplication_of_list_elements_2()
test_compute_min_multiplication_of_list_elements_3()
test_compute_min_multiplication_of_list_elements_4()
test_compute_min_multiplication_of_list_elements_5()
test_compute_min_multiplication_of_list_elements_6()
test_compute_min_multiplication_of_list_elements_7()
test_compute_min_multiplication_of_list_elements_8()
