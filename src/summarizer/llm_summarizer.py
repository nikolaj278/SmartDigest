import asyncio

from openai import OpenAI

from src.config.settings import DS_API_KEY
from src.preprocessing.prompt_builder import build_the_prompt



class Summarizer:
    """
    Define an object to connect to DeepSeek api, send a request and receive a summrized text.
    """
    def __init__(self):
        self.client = OpenAI(api_key=DS_API_KEY, base_url="https://api.deepseek.com")
        

    async def send_request(self, request):
        """Send the request to LLM model."""
        
        return self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": request}],
                    n=1
                ).choices[0].message.content

    async def task_maker(self, collected):
        """
        Build the prompts.
        Make and run the tasks with asynchronous send_request function.
        Return channel names, requests by channels and results of the requests.
        """
        requests = [build_the_prompt(msgs) for msgs in collected.values()]
        tasks = [self.send_request(r) for r in requests]
        results = await asyncio.gather(*tasks)
        # ch are tuples - (channel.name, channel.id)
        return {ch: (req, res) for ch, req, res in zip(collected.keys(), requests, results)}

    def summarize(self, collected):
        """Run asynchronous task_maker function."""
        
        return asyncio.run(self.task_maker(collected))
            

    

