customer = {
    "membership": "gold"
}

if customer["membership"] == "gold":
    print("Recommend Toyota Fortuner upgrade")
else:
    print("Recommend Hyundai Creta")
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a rental counter assistant"
        },
        {
            "role": "user",
            "content": "Customer is gold member, suggest vehicle"
        }
    ]
)

print(response.choices[0].message.content)