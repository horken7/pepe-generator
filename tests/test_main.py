import unittest
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient


class TestApp(unittest.TestCase):
    def test_return_pepe_no_data_directory(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value = MagicMock()
            mock_get.return_value.content = b"some_image_data"

            # importing inside of test since initializing the object is directly using dependency
            from pepe_generator import app

            client = TestClient(app)

            response = client.get("/")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b"some_image_data")
            self.assertEqual(response.headers["Content-Type"], "image/jpeg")
