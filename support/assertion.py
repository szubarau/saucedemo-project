from support.assertion_errors import AssertionErrors
class Assertion:

    @staticmethod
    def assert_equal(expected_result, actual_result):
        assert expected_result == actual_result, AssertionErrors.EQUAL_ERROR.format(expected_result,actual_result)
