import pytest
import allure
from src.api.admin import Admin
from test_data import booking_test_data
from utilities.tools import TestResultEvaluator


@pytest.mark.booking
@allure.suite("Booking")
class TestBooking:
    @allure.title("Get all booking")
    def test_get_all_booking(self):
        admin = Admin()
        booking = admin.booking.get()
        expected = True
        current = isinstance(booking, list)
        assertion_list = [
            TestResultEvaluator.compare_results(info="Response is list",
                                                expected_result=expected,
                                                current_result=current)
            ]
        assert TestResultEvaluator(assertion_list)

    @allure.title("Get booking by ID")
    def test_get_booking_by_id(self):
        admin = Admin()
        admin.authenticate()
        create_booking = admin.booking.create(firstname=booking_test_data.booking_create['firstname'],
                                              lastname=booking_test_data.booking_create['lastname'],
                                              totalprice=booking_test_data.booking_create['totalprice'],
                                              depositpaid=booking_test_data.booking_create['depositpaid'],
                                              checkin=booking_test_data.booking_create['checkin'],
                                              checkout=booking_test_data.booking_create['checkout'],
                                              additionalneeds=booking_test_data.booking_create['additionalneeds'],
                                              )
        booking_id = create_booking['bookingid']
        created_booking = admin.booking.get(booking_id=booking_id)
        assertion_list = [
            TestResultEvaluator.compare_results(info="First name",
                                                expected_result=booking_test_data.booking_create['firstname'],
                                                current_result=created_booking['firstname']),
            TestResultEvaluator.compare_results(info="Last name",
                                                expected_result=booking_test_data.booking_create['lastname'],
                                                current_result=created_booking['lastname']),
            TestResultEvaluator.compare_results(info="Total price",
                                                expected_result=booking_test_data.booking_create['totalprice'],
                                                current_result=created_booking['totalprice']),
            TestResultEvaluator.compare_results(info="Deposit paid",
                                                expected_result=booking_test_data.booking_create['depositpaid'],
                                                current_result=created_booking['depositpaid']),
            TestResultEvaluator.compare_results(info="Check in",
                                                expected_result=booking_test_data.booking_create['checkin'],
                                                current_result=created_booking['bookingdates']['checkin']),
            TestResultEvaluator.compare_results(info="Check out",
                                                expected_result=booking_test_data.booking_create['checkout'],
                                                current_result=created_booking['bookingdates']['checkout']),
            TestResultEvaluator.compare_results(info="Additional needs",
                                                expected_result=booking_test_data.booking_create['additionalneeds'],
                                                current_result=created_booking['additionalneeds'])

        ]
        assert TestResultEvaluator(assertion_list)

    @allure.step("Edit booking -> PUT")
    def test_booking_edit_put(self):
        admin = Admin()
        admin.authenticate()
        create_booking = admin.booking.create(firstname=booking_test_data.booking_create['firstname'],
                                              lastname=booking_test_data.booking_create['lastname'],
                                              totalprice=booking_test_data.booking_create['totalprice'],
                                              depositpaid=booking_test_data.booking_create['depositpaid'],
                                              checkin=booking_test_data.booking_create['checkin'],
                                              checkout=booking_test_data.booking_create['checkout'],
                                              additionalneeds=booking_test_data.booking_create['additionalneeds'],
                                              )
        admin.booking.update_put(create_booking, firstname=booking_test_data.booking_edit_put['firstname'])
        booking_edited = admin.booking.get(booking_id=create_booking["bookingid"])
        assertion_list = [
            TestResultEvaluator.compare_results(info="Changed name",
                                                expected_result=booking_test_data.booking_edit_put["firstname"],
                                                current_result=booking_edited["firstname"])
        ]
        assert TestResultEvaluator(assertion_list).result





