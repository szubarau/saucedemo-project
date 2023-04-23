import pytest

case_1 = ['standard_user', '', 'Epic sadface: Password is required']
case_2 = ['', 'secret_sauce', 'Epic sadface: Username is required']
case_3 = ['standard_user', '12345', 'Epic sadface: Username and password do not match any user in this service']
case_4 = ['locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.']


def test_login(index_page):
    index_page.login()
    index_page.verify_title_text()


def test_logout(index_page):
    index_page.login()
    index_page.logout()
    index_page.verify_title_text_logout()


@pytest.mark.parametrize('user_name,password,expected_result', (case_1, case_2, case_3, case_4),
                         ids=['empty_password', 'empty_username', 'incorrect_password', 'user is lock'])
def test_unsuccessful(index_page, user_name, password, expected_result):
    index_page.login(user_name,password)
    index_page.verify_title_text_unsuccessful_login(expected_result)
