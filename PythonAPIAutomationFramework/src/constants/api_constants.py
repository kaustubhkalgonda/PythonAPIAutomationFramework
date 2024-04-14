#class which contains all the end points.

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"
    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"
    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    def url_update_patch_delete(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)


