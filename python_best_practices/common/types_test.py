import unittest

from python_best_practices.common.types import User, map_dict_to_dataclass


class TestMapDictToDataclass(unittest.TestCase):
    def test_successful_mapping(self):
        # Sample data for successful mapping
        user_data = {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        }

        # Attempt to map the dict to the User dataclass
        user = map_dict_to_dataclass(user_data, User)

        # Assert that the mapping was successful by comparing fields
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Leanne Graham")
        self.assertEqual(user.username, "Bret")
        self.assertEqual(user.email, "Sincere@april.biz")
        self.assertEqual(user.address.street, "Kulas Light")
        self.assertEqual(user.address.geo.lat, "-37.3159")
        self.assertEqual(user.company.name, "Romaguera-Crona")

    def test_key_error_on_missing_field(self):
        # Data with a missing required field (e.g., 'id')
        user_data_missing_field = {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        }

        # Check that a KeyError is raised when a required field is missing
        with self.assertRaises(KeyError):
            map_dict_to_dataclass(user_data_missing_field, User)


if __name__ == "__main__":
    unittest.main()
