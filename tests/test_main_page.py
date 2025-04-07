import pytest
import allure
from config import USERNAME, PASSWORD

case_1 = ['Ivan', '', '00345', 'Error: Last Name is required']
case_2 = ['', 'Ivanov', '00345', 'Error: First Name is required']
case_3 = ['Ivan', 'Ivanov', '', 'Error: Postal Code is required']


def test_buy_goods(index_page, main_page):
    index_page.login(USERNAME,PASSWORD)
    index_page.verify_title_text()
    main_page.buy_goods(first_name='Ivan', last_name='Ivanov', postal_code='0045')
    main_page.verify_title_text()


@pytest.mark.parametrize('first_name,last_name,postal_code,expected_result', (case_1, case_2, case_3),
                         ids=['empty first name', 'empty last name','empty postal code'])
def test_not_buy_goods(index_page, main_page,first_name,last_name,postal_code,expected_result):
    index_page.login(USERNAME, PASSWORD)
    index_page.verify_title_text()
    main_page.not_buy_goods(first_name,last_name,postal_code)
    main_page.verify_title_text_unsuccessful_buy_goods(expected_result)
