# src/llm.py

import os
from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI()

    def generate_daily_report(self, markdown_content, dry_run=False):
        system_pr = f"以下是项目的最新进展，根据功能合并同类项，形成一份简报，至少包含：1）新增功能；2）主要改进；3）修复问题；请使用中文回答我:\n\n"
        prompt = ""
        if dry_run:
            with open("daily_progress/prompt.txt", "w+",encoding='utf-8') as f:
                f.write(prompt)
            return "DRY RUN"

        print("Before call GPT")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":system_pr},
                {"role": "user", "content": markdown_content}
            ]
        )
        print("After call GPT")
        print(response)
        return response.choices[0].message.content
