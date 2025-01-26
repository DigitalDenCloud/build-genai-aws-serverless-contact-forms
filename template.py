def generate_quote_prompt():
    """
    Generates a strict template for requesting concise and original quotes from an AI model.

    Returns:
    str: A formatted string containing the prompt template for generating quotes.
    """
    # Define the template string
    template = """
    Provide a concise, original, and engaging quote about life, success, or personal growth.

    Important:
    1. Respond with ONLY the quote text.
    2. Do NOT include any phrases like 'Here is...' or meta-descriptions of the quote.
    3. The quote should be thoughtful, impactful, and limited to 2 sentences.
    4. Begin the response directly with the quote itself.
    """
    return template

# NOTES:
# 1. This template is designed for use with AI language models.
# 2. It provides clear instructions to generate a standalone quote.
# 3. The output is easy to extract and use without additional processing.

# CUSTOMIZATION:
# - To change the theme: 
#   Replace "life, success, or personal growth" with your desired topic.
#   Example: "technology, innovation, or teamwork."

# - To adjust the style:
#   Add style instructions in the "Important" section.
#   Example: "5. The quote should have a motivational tone."

# - To specify an audience:
#   Add audience information in the "Important" section.
#   Example: "5. The quote should be suitable for a professional audience."