import allure
import urllib.parse


@allure.step("Check assertion(s)")
class TestResultEvaluator:
    def __init__(self, result_list):
        self.result = True
        self.info = ""
        for index, result in enumerate(result_list):
            if index == 0:
                self.info += f'\n{"*" * 80}\n'
            self.info += f'{result["info"]}'
            if index < len(result_list) - 1:
                self.info += f'\n{"-" * 80}\n'
            if not result["status"]:
                self.result = False
        if result_list:
            self.info += f'\n{"*" * 80}\n'
        print(self.info)

    @staticmethod
    def compare_results(info, expected_result, current_result):
        status = expected_result == current_result
        info = f'{info.ljust(76 if status is True else 75)}{str(status)}\nExpected: {expected_result}\nCurrent : {current_result}'
        return {"status": status, "info": info}


def build_url_with_query_params(url, **kwargs):
    query_params = {key: value for key, value in kwargs.items() if value is not None}
    query_string = urllib.parse.urlencode(query_params)
    if query_string:
        return f"{url}?{query_string}"
    else:
        return url
