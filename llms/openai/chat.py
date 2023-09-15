import os
import openai
openai.organization = "org-ohlsr94lCc79YgQfjy0UGzst"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'