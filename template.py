def generate_content_prompt():
    """
    Generates a strict template for requesting concise and direct AI-based content.

    Returns:
    str: A formatted string containing the prompt template for generating AI-based content.
    """
    # Define the template string
    template = """
    Provide a concise, original, and engaging piece of content about life, success, or personal growth.

    Important:
    1. Respond with ONLY the content text.
    2. Do NOT include any phrases like 'Here is...', 'This is...', or meta-descriptions of the content.
    3. The content should be thoughtful, impactful, and limited to 2 sentences.
    4. Begin the response directly with the content itself.
    """
    return template

# NOTES:
# 1. This template is designed for use with AI language models.
# 2. It provides clear instructions to generate concise, standalone content.
# 3. The output is easy to extract and use without additional processing.

# CUSTOMIZATION:
# - To change the theme:
#   Replace "life, success, or personal growth" with your desired topic.
#   Example: "technology, creativity, or teamwork"

# - To adjust the style:
#   Modify the "Important" section.
#   Example: Add an instruction like:
#   "5. Use a motivational tone to inspire the audience."

# - To specify a target audience:
#   Add audience details in the "Important" section.
#   Example: "5. The content should resonate with young professionals."

# - To adjust the length:
#   Change "limited to 2 sentences" to your desired length.
#   Example: "4. The content should be no more than 4 sentences."

# TROUBLESHOOTING:
# - If the AI still adds meta-descriptions or introductory text:
#   Ensure "Respond with ONLY the content text" is emphasised.
#   Try lowering the model's "temperature" setting for more deterministic output.