import os
import requests
API_URL = os.environ.get('LLM_API_URL','https://api.openai.com/v1/chat/completions')
API_KEY = os.environ.get('OPENAI_API_KEY','')

def complete(prompt):
    if not API_KEY:
        return f"MOCK: {prompt}"
    headers={'Authorization':f'Bearer {API_KEY}','Content-Type':'application/json'}
    body={'model':'gpt-4o-mini','messages':[{'role':'user','content':prompt}]}
    r=requests.post(API_URL,json=body,headers=headers)
    return r.json()
