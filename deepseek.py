import requests

def query_deepseek(prompt, api_key, model="deepseek-chat", temperature=0.7):
    """
    Query DeepSeek API with a prompt and return the response.

    Args:
        prompt: The formatted prompt string
        api_key: DeepSeek API key
        model: DeepSeek model to use
        temperature: Sampling temperature (0.0 to 1.0)

    Returns:
        Response text from DeepSeek
    """
    try:
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
    except Exception as e:
        print(f"Error querying DeepSeek API: {type(e).__name__} - {str(e)}")
        return None

