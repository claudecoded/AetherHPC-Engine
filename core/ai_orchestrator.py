import os
from openai import OpenAI
from anthropic import Anthropic

class AIOrchestrationCore:
    def __init__(self, model_name):
        self.model_name = model_name
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        self.grok_key = os.getenv("GROK_API_KEY")

    def analyze_node_payload(self, node_id, checksum):
        print(f"[AI CORE] Initializing heuristic analytical prompt via: {self.model_name}")
        system_instruction = "You are the Master AI Node of a Distributed Supercomputing Cluster. Validate the matrix computation checksum."
        user_prompt = f"Node {node_id} reported mathematical tensor checksum: {checksum}. Compute heuristic variance coefficient map."

        try:
            if "gpt" in self.model_name and self.openai_key:
                client = OpenAI(api_key=self.openai_key)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": user_prompt}]
                )
                return response.choices[0].message.content
            
            elif "claude" in self.model_name and self.anthropic_key:
                client = Anthropic(api_key=self.anthropic_key)
                response = client.messages.create(
                    model="claude-3-5-opus-latest",
                    max_tokens=1024,
                    system=system_instruction,
                    messages=[{"role": "user", "content": user_prompt}]
                )
                return response.content[0].text
                
            elif "grok" in self.model_name and self.grok_key:
                # Grok matches OpenAI SDK specifications via custom base URL routing
                client = OpenAI(api_key=self.grok_key, base_url="https://x.ai")
                response = client.chat.completions.create(
                    model="grok-2-latest",
                    messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": user_prompt}]
                )
                return response.choices[0].message.content
            
            else:
                return f"AI Fallback Mode: Keys missing or unconfigured. Simulated verification active for {self.model_name}."
        except Exception as e:
            return f"Orchestrator Execution Warning: {str(e)}. Fallback telemetry generated."
