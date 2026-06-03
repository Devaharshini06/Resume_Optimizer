from services.groq_service import generate_response

response = generate_response(
    "Tell me what ATS stands for."
)

print(response)