def generate_content_prompt():
    """
    Generates a template for requesting AI-based content from an AI model.

    Returns:
    str: A formatted string containing the prompt template for generating AI-based content.
    """
    # Define the template string
    template = """
    Generate a unique, original, and thought-provoking piece of content about life, success, or personal growth.

    Important:
    1. Provide ONLY the content text.
    2. Do not include any introductory phrases or explanations.
    3. The content should be inspirational and universally applicable.
    4. Begin your response with the content directly, without any preamble.

    Now, provide an original piece of content:
    """
    return template

# NOTES:
# 1. This template is designed for use with AI language models.
# 2. It provides clear instructions to generate a standalone piece of content.
# 3. The output is easy to extract and use without additional processing.

# CUSTOMIZATION:
# - To change the theme: 
#   Replace "life, success, or personal growth" with your desired topic.
#   Example: "technology, nature, or creativity"

# - To adjust the style:
#   Add style instructions in the "Important" section.
#   Example: "5. The content should have a motivational tone."

# - To specify an audience:
#   Add audience information in the "Important" section.
#   Example: "5. The content should be suitable for a young adult audience."