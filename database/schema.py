class SchemaGenerator:
    def __init__(self, chat_api):
        self.chat_api = chat_api

    def generate_schema(self, text_description):
      messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a valid SQLite schema for {text_description} (without commentary)"}
    ]
      print("Generating Schema...")
      schema = self.chat_api.generate_chat_completion(messages, temperature=0.5)
      print("Generated schema:\n", schema)
      return schema

