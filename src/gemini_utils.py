# Function to send reviews to Gemini
def get_gemini_response(client, prompt):

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response

    except Exception as e:
        print("\nGemini API request failed!")
        print(f"Error details: {e}")
        raise SystemExit(1)