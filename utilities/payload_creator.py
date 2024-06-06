class PayloadCreator:

    class Login:
        @staticmethod
        def admin_login_payload(username, password):
            return {
                "username": username,
                "password": password
            }

    class Booking:
        @staticmethod
        def create_booking_payload(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
            return {
                "firstname": firstname,
                "lastname": lastname,
                "totalprice": totalprice,
                "depositpaid": depositpaid,
                "bookingdates": {
                    "checkin": checkin,
                    "checkout": checkout
                },
                "additionalneeds": additionalneeds
            }