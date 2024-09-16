![Solution](/solution_architecture.png)

<h1 align="center">Build GenAI-Integrated Serverless Contact Forms for Static Websites With AWS Lambda, API Gateway, Bedrock, and SES</h1>

<p align="center">
  <a href="https://docs.digitalden.cloud/posts/build-genai-integrated-serverless-contact-forms-for-static-websites-with-aws-lambda-api-gateway-bedrock-and-ses/" target="_blank">
    <img src="https://img.shields.io/badge/Documentation-008CBA?style=for-the-badge&logo=read-the-docs&logoColor=white&labelColor=005f7f" alt="Documentation">
  </a>

This repository contains the necessary code and resources to implement a serverless contact form solution integrated with GenAI capabilities. For detailed instructions on how to implement and deploy this solution, please refer to the associated documentation.

## Contents

- [`lambda_function.py`](./lambda_function.py): Main Lambda function for handling contact form submissions and generating AI quotes
- [`lambda_test_event.json`](./lambda_test_event.json): Sample test event for the contact form Lambda function
- [`template.py`](./template.py): Template generator for AI inspirational quotes
- [`main.js`](./main.js): JavaScript code for contact form submission handling
- [`HTML5 UP Dimension Template`](./html5up-dimension): Template for the static website, including the contact form

## Solution Architecture

This architecture enables dynamic functionality for static websites without traditional server management, handling form processing, AI integration, and email communication seamlessly in the cloud. The serverless contact form solution follows these steps:

1. A static contact form on the website initiates the process.

2. When a visitor submits the form, it sends an HTTP POST request to Amazon API Gateway.

3. API Gateway receives this request and invokes the AWS Lambda function.

4. The Lambda function, the core of the solution:
   - Processes the form data
   - Contains a pre-defined prompt for inspirational quote generation
   - Invokes the Amazon Bedrock API with this prompt

5. Amazon Bedrock processes the prompt and generates a unique inspirational quote.

6. The Lambda function then:
   - Receives the response from the Bedrock API
   - Initiates the email-sending process using Amazon Simple Email Service (SES)

7. Amazon SES handles the email delivery:
   - Sends a notification email to the website owner
   - Sends a confirmation email, including the inspirational quote, to the website visitor

### Key Components

- **AWS Lambda**: Core logic for data processing and service orchestration
- **Amazon API Gateway**: RESTful API endpoint for the contact form
- **Amazon Bedrock**: AI service for generating inspirational quotes
- **Amazon SES**: Email delivery service

## Connect with Me

I'd love to connect with you and hear about your experiences with this project.

<p align="center">
  <a href="https://www.linkedin.com/in/digitalden/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=004a76" alt="LinkedIn">
  </a>
  <a href="https://www.youtube.com/@DigitalDenCloud" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=b30000" alt="YouTube">
  </a>
  <a href="https://digitalden.cloud" target="_blank">
    <img src="https://img.shields.io/badge/Website-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white&labelColor=2a75f3" alt="Website">
  </a>
</p>