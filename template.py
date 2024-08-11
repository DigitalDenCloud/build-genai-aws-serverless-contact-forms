def generate_inspirational_quote_template():
    """
    Generates a template for requesting an inspirational quote from an AI model.

    Returns:
    str: A formatted string containing the prompt template for generating an inspirational quote.
    """
    # Define the template string
    template = """
    Generate a unique, original, and thought-provoking inspirational quote about life, success, or personal growth.

    Important:
    1. Provide ONLY the quote text.
    2. Do not include any introductory phrases or explanations.
    3. The quote should be inspirational and universally applicable.
    4. Begin your response with the quote directly, without any preamble.

    Now, provide an original inspirational quote:
    """
    return template

# NOTES:
# 1. This template is designed for use with AI language models.
# 2. It provides clear instructions to generate a standalone quote.
# 3. The output is easy to extract and use without additional processing.

# CUSTOMIZATION:
# - To change the theme: 
#   Replace "life, success, or personal growth" with your desired topic.
#   Example: "technology, nature, or creativity"

# - To adjust the style:
#   Add style instructions in the "Important" section.
#   Example: "5. The quote should have a motivational tone."

# - To specify an audience:
#   Add audience information in the "Important" section.
#   Example: "5. The quote should be suitable for a young adult audience."