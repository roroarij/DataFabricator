class DataGenerator:
    def __init__(self, chat_api):
        self.chat_api = chat_api

    def generate_data(self, schema):
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate example data for the following SQLite schema using valid SQLITE  (without commentary):\n{schema}"}
    ]
        print("Generating Data...")
        insert_statement = self.chat_api.generate_chat_completion(messages)
        print("Generated example data:\n", insert_statement)
        return insert_statement
    
