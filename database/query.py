class QueryGenerator:
    def __init__(self, chat_api):
        self.chat_api = chat_api

    def generate_query_ideas(self,schema, text_description):
      messages = [
        {"role": "system", "content": "You are a helpful Data Engineering assistant."},
        {"role": "user", "content": f"Output a valid json array with the keys query and description, containing 10 SQLite queries useful to perform analysis of our data based on the following schema: \n{schema}"}
    ]
      print("Generating query ideas..")
      query_ideas_array = self.chat_api.generate_chat_completion(messages, model="gpt-4", temperature=0.5)
      print(query_ideas_array)
      query_ideas_array=[i.get('query') for i in query_ideas_array]
      return query_ideas_array   
  
             
