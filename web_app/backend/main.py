import os
import json
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AI_API_BASE = os.getenv("AI_API_BASE")
AI_API_KEY = os.getenv("AI_API_KEY")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]
    locale: str = "en"

def get_system_prompt(locale: str) -> dict:
    if locale == "vi":
        return {
            "role": "system",
            "content": "Bạn là một hướng dẫn viên du lịch chuyên nghiệp về Bản Yên Hoà, Xã Mỹ Lý, Tỉnh Nghệ An. Hãy trả lời các câu hỏi bằng tiếng Việt."
        }
    else:
        return {
            "role": "system",
            "content": "You are a professional tour guide for Ban Yen Hoa, My Ly Commune, Nghe An Province. Please answer questions in English."
        }

def get_ai_response(messages, model="gemini-2.5-pro"):
    if not AI_API_BASE or AI_API_BASE == "your_api_base_here" or not AI_API_KEY or AI_API_KEY == "your_api_key_here":
        return "AI service not configured. Please set AI_API_BASE and AI_API_KEY in your .env file."

    url = f"{AI_API_BASE}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AI_API_KEY}"
    }
    data = {
        "model": model,
        "messages": messages
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error calling AI API: {e}")
        return f"Error: Could not connect to AI service at {AI_API_BASE}"
    except (KeyError, IndexError) as e:
        print(f"Error parsing AI response: {e}")
        return "Error: Invalid response from AI service"

@app.post("/api/chat")
async def chat(chat_request: ChatRequest):
    system_prompt = get_system_prompt(chat_request.locale)
    messages = [system_prompt] + [message.dict() for message in chat_request.messages]
    ai_response = get_ai_response(messages)
    if ai_response:
        return {"role": "assistant", "content": ai_response}
    else:
        return {"error": "Failed to get response from AI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
