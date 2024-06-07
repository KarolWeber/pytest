import allure
from src.api.endpoints import Endpoints
from test_data import booking_test_data
from utilities.helpers import api_call, HttpMethod
from utilities.payload_creator import PayloadCreator
from utilities.tools import build_url_with_query_params


class Booking:
    def __init__(self, admin):
        self._token = admin.token

    @allure.step("Get booking data")
    def get(self, booking_id=None, firstname=None, lastname=None, checkin=None, checkout=None):
        """
        Get reservation(s)
        Filter works only with firstname/lastname and checkin/checkout
        :param booking_id: Get booking with ID
        :param firstname: Search booking by firstname
        :param lastname: Search booking by lastname
        :param checkin: Search booking by checkin yyyy-mm-dd
        :param checkout: Search booking by checkout yyyy-mm-dd
        :return: all reservation if no booking_id or search parameters
        """
        url = Endpoints.booking
        if booking_id:
            url += f'/{booking_id}'
        url = build_url_with_query_params(url, firstname=firstname, lastname=lastname, checkin=checkin, checkout=checkout)
        response = api_call(method=HttpMethod.GET, url=url)
        if response.status_code == 200:
            return response.json()
        return response

    @allure.step("Create booking")
    def create(self, firstname=booking_test_data.booking_create['firstname'], lastname=booking_test_data.booking_create['lastname'],
               totalprice=booking_test_data.booking_create['totalprice'], depositpaid=booking_test_data.booking_create['depositpaid'],
               checkin=booking_test_data.booking_create['checkin'], checkout=booking_test_data.booking_create['checkout'],
               additionalneeds=booking_test_data.booking_create['additionalneeds']):
        payload = PayloadCreator.Booking.create_booking_payload(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds)
        response = api_call(method=HttpMethod.POST, url=Endpoints.booking, data=payload)
        if response.status_code == 200:
            return response.json()
        return response

    @allure.step("Edit booking")
    def update_put(self, booking, firstname=None, lastname=None, totalprice=None, depositpaid=None, checkin=None, checkout=None, additionalneeds=None):
        payload = PayloadCreator.Booking.create_booking_payload(
            firstname=firstname if firstname is not None else booking['booking']['firstname'],
            lastname=lastname if lastname is not None else booking['booking']['lastname'],
            totalprice=totalprice if totalprice is not None else booking['booking']['totalprice'],
            depositpaid=depositpaid if depositpaid is not None else booking['booking']['depositpaid'],
            checkin=checkin if checkin is not None else booking['booking']['bookingdates']['checkin'],
            checkout=checkout if checkout is not None else booking['booking']['bookingdates']['checkout'],
            additionalneeds=additionalneeds if additionalneeds is not None else booking['booking']['additionalneeds']
        )
        response = api_call(method=HttpMethod.PUT, url=f'{Endpoints.booking}/{booking["bookingid"]}', data=payload, user=self._token)
        if response.status_code == 200:
            return response.json()
        return response

    @allure.step("Delete booking")
    def delete(self, booking_id):
        return api_call(method=HttpMethod.DELETE, url=f'{Endpoints.booking}/{booking_id}', user=self._token)

