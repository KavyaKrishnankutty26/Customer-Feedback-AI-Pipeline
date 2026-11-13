import unittest
from unittest.mock import Mock
from unittest.mock import patch

from src.gemini_utils import get_gemini_response

class TestGeminiErrorHandling(unittest.TestCase):

    @patch("builtins.print")
    def test_gemini_api_failure(self, mock_print):

        # Create a fake Gemini client
        client = Mock()

        # Simulate a Gemini API failure
        client.models.generate_content.side_effect = Exception(
            "Simulated Gemini API failure"
        )

        # Check whether our function stops execution
        with self.assertRaises(SystemExit) as error:
            get_gemini_response(client, "Test prompt")

        # Confirm that the program exits with error code 1
        self.assertEqual(error.exception.code, 1)

        # Confirm that the API failure message was printed
        mock_print.assert_any_call("\nGemini API request failed!")

    def test_gemini_api_success(self):

        # Create a fake Gemini client
        client = Mock()

        # Create a fake successful response
        expected_response = Mock()
        expected_response.text = '[{"review_number": 1, "sentiment": "Positive"}]'

        client.models.generate_content.return_value = expected_response

        # Call the function
        response = get_gemini_response(client, "Test prompt")

        # Check whether the response is returned correctly
        self.assertEqual(response.text, expected_response.text)


if __name__ == "__main__":
    unittest.main()