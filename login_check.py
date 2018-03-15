import re


def login_check(login):
    if len(login) == 0 or len(login) > 20:
        return False

    if re.match('[a-zA-Z]', login[0]) is None:
        return False

    if re.match('[a-zA-Z0-9]', login[-1]) is None:
        return False

    res = re.match('[a-zA-Z0-9\.\-]*', login[1:-1])
    if res is None or len(res.group(0)) != len(login[1:-1]):
        return False

    return True
