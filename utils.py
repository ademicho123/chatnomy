import requests

def handle_file_upload(uploaded_file):
    """
    Reads the content of an uploaded file.
    Supports text-based and binary file formats.
    """
    try:
        file_content = uploaded_file.read()
        if isinstance(file_content, bytes):
            return file_content.decode("utf-8", errors="ignore")
        return file_content
    except Exception as e:
        return f"Error reading file: {str(e)}"

def query_together_api(api_key, api_url, prompt):
    """
    Sends a query to Together API with the provided prompt.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"prompt": prompt, "max_tokens": 300}
    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get("text", "No response text found.")
        return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"API request failed: {str(e)}"
