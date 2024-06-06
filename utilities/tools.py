import allure


@allure.step("Check assertion")
def assertion(expected_result, current_result):
    test_status = expected_result == current_result
    print(f'\n{40 * "+"}\nExpected: {expected_result}\nCurrent : {current_result}\n{40 * "+"}\n')
    assert test_status
