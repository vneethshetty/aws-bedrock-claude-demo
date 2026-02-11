import boto3
import json

def generate_response(prompt):
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name="ap-south-1"
    )

    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = client.invoke_model(
        modelId="apac.anthropic.claude-3-sonnet-20240229-v1:0",
        body=json.dumps(request_body),
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response["body"].read())
    return response_body["content"][0]["text"]


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    output = generate_response(user_prompt)

    print("\n=== AI Response ===\n")
    print(output)
