import anthropic


def query_claude(
        prompt,
        api_key,
        model="claude-3-opus-20240229",
        temperature=0.7):
    """
    Query Claude API with a prompt and return the response.

    Args:
        prompt: The formatted prompt string
        api_key: Anthropic API key
        model: Claude model to use
        temperature: Sampling temperature (0.0 to 1.0)

    Returns:
        Response text from Claude
    """
    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            max_tokens=2048,
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return response.content[0].text
    except Exception as e:
        return f"Error querying Claude API: {str(e)}"
