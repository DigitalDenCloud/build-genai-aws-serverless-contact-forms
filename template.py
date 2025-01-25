def generate_content_prompt():
    """
    Generates a template for requesting AI-based content from an AI model.

    Returns:
    str: A formatted string containing the prompt template for generating AI-based content.
    """
    # Define the template string
    template = """
    Generate a unique, original, and engaging piece of content about life, creativity, or personal growth.

    Important:
    1. Provide ONLY the content text.
    2. Do not include any introductory phrases or explanations.
    3. The content should be engaging and universally appealing.
    4. Start the response with the content immediately, avoiding any preamble.
    """
    return template

# NOTES:
# 1. This template is designed for use with AI language models.
# 2. It provides clear instructions to generate standalone AI-based content.
# 3. The output is structured to be easy to extract and integrate into applications.

# CUSTOMIZATION:
# - To change the topic:
#   Replace "life, creativity, or personal growth" with your desired topic.
#   Example: "technology, teamwork, or leadership."

# - To adjust the tone or style:
#   Add style-specific instructions in the "Important" section.
#   Example: "5. The content should have a formal and professional tone."

# - To tailor content for a specific use case:
#   Add more context in the "Important" section.
#   Example: "5. The content should be suitable for use in marketing materials."