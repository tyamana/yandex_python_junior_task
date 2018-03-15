import login_check


def test_login_check_1():
    login = 'qwerty-.123456789'
    print('OK') if login_check.login_check(login) is True else print('Test error 1')


def test_login_check_2():
    login = 'qwerty-.0123456789123'
    print('OK') if login_check.login_check(login) is False else print('Test error 2')


def test_login_check_3():
    login = '2werty-.123456789'
    print('OK') if login_check.login_check(login) is False else print('Test error 3')


def test_login_check_4():
    login = 'qwerty-.12345678.'
    print('OK') if login_check.login_check(login) is False else print('Test error 4')


def test_login_check_5():
    login = 'qwer__ty-.1234567'
    print('OK') if login_check.login_check(login) is False else print('Test error 5')


def test_login_check_6():
    login = ''
    print('OK') if login_check.login_check(login) is False else print('Test error 6')

def test_login_check_7():
    login = 'ololev-kdoske.11'
    print('OK') if login_check.login_check(login) is True else print('Test error 7')

def test_login_check_8():
    login = 'ololo11 ur12'
    print('OK') if login_check.login_check(login) is False else print('Test error 8')

def test_login_check_9():
    login = 'a'
    print('OK') if login_check.login_check(login) is True else print('Test error 9')


test_login_check_1()
test_login_check_2()
test_login_check_3()
test_login_check_4()
test_login_check_5()
test_login_check_6()
test_login_check_7()
test_login_check_8()
test_login_check_9()
