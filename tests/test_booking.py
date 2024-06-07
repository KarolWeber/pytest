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
        """
        Verify the booking list is correctly retrieved.

        Steps:
        1. Login as Admin.
        2. Retrieve booking list.
        3. Confirm the data is a list.
        """
        admin = Admin()
        admin.authenticate()
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
        """
        Verify booking retrieval by ID.

        Steps:
        1. Login as Admin.
        2. Create a new booking.
        3. Retrieve booking by ID.
        4. Confirm the retrieved data matches the created data.
        """
        admin = Admin()
        admin.authenticate()
        create_booking = admin.booking.create()
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
        """
        Verify booking update functionality.

        Steps:
        1. Login as Admin.
        2. Create a new booking.
        3. Update the booking.
        4. Retrieve booking by ID.
        5. Confirm the updated data matches the retrieved data.
        """
        admin = Admin()
        admin.authenticate()
        create_booking = admin.booking.create()
        admin.booking.update_put(create_booking, firstname=booking_test_data.booking_edit_put['firstname'])
        booking_edited = admin.booking.get(booking_id=create_booking["bookingid"])
        assertion_list = [
            TestResultEvaluator.compare_results(info="Changed name",
                                                expected_result=booking_test_data.booking_edit_put["firstname"],
                                                current_result=booking_edited["firstname"])
        ]
        assert TestResultEvaluator(assertion_list).result

    @allure.step("Delete booking")
    def test_booking_delete(self):
        """
        Verify booking deletion functionality.

        Steps:
        1. Login as Admin.
        2. Create a new booking.
        3. Delete the booking.
        4. Verify delete status code.
        5. Confirm retrieval of deleted booking fails.
        """
        admin = Admin()
        admin.authenticate()
        create_booking = admin.booking.create()
        booking_delete = admin.booking.delete(booking_id=create_booking['bookingid'])
        check_delete = admin.booking.get(booking_id=create_booking["bookingid"])
        assertion_list = [
            TestResultEvaluator.compare_results(info="Delete status code",
                                                expected_result=201,
                                                current_result=booking_delete.status_code),

            TestResultEvaluator.compare_results(info="Get deleted booking status code",
                                                expected_result=404,
                                                current_result=check_delete.status_code)
        ]
        assert TestResultEvaluator(assertion_list).result




