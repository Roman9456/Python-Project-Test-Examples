import requests
import unittest

class TestYandexDiskAPI(unittest.TestCase):
    base_url = 'https://cloud-api.yandex.net/v1/disk'
    headers = {
        'Authorization': 'YANDEX TOKEN', 
    }

    def test_create_folder_success(self):
        folder_name = 'TestFolder'
        folder_info_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Check if the folder with the given name already exists
        response = requests.get(folder_info_url, headers=self.headers)
        if response.status_code == 200:
            # The folder already exists, just check for a successful response
            self.assertEqual(response.status_code, 200)
        else:
            # The folder doesn't exist, create it
            folder_url = f'{self.base_url}/resources?path=/{folder_name}'
            response = requests.put(folder_url, headers=self.headers)
            self.assertEqual(response.status_code, 201)  # Folder created successfully

        # Verify that the folder was indeed created and appears in the list of files
        response = requests.get(folder_info_url, headers=self.headers)
        self.assertEqual(response.status_code, 200)  # Folder information request successful

    def test_create_folder_error(self):
        folder_name = 'TestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Attempt to create a folder with the same name as an existing folder
        response = requests.put(folder_url, headers=self.headers)
        self.assertEqual(response.status_code, 409)  # Conflict, folder already exists

    def test_invalid_authorization(self):
        invalid_headers = {
            'Authorization': 'InvalidToken',  # Invalid token
        }
        folder_name = 'InvalidTestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Attempt to create a folder with an invalid authorization token
        response = requests.put(folder_url, headers=invalid_headers)
        self.assertEqual(response.status_code, 401)  # Unauthorized

if __name__ == '__main__':
    unittest.main()

