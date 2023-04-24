from api.chat_api import ChatAPI
from database.connection import DatabaseConnection
from database.schema import SchemaGenerator
from database.data import DataGenerator
from database.query import QueryGenerator

API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def main():
    # Initialize the Chat API
    chat_api = ChatAPI(api_key=API_KEY, api_endpoint=API_ENDPOINT)

    # Initialize the Schema Generator
    schema_generator = SchemaGenerator(chat_api=chat_api)

    # Generate the schema
    description = "a database of parcel level information"
    schema = schema_generator.generate_schema(description)

    # Initialize the Data Generator
    data_generator = DataGenerator(chat_api=chat_api)

    # Generate the data
    insert_statements = data_generator.generate_data(schema)

    # Initialize the Database Connection
    db_connection = DatabaseConnection()

    # Create the database connection
    db_connection.create_connection()

    # Execute the schema creation query
    db_connection.execute_query(schema)

    # Execute the data insertion queries
    
    db_connection.execute_query(insert_statements)
    #db_connection.list_items('parcels')

    # Initialize the Query Generator
    query_generator = QueryGenerator(chat_api=chat_api)

    # Generate query ideas
    query_ideas = query_generator.generate_query_ideas(schema, description)
    # Print query ideas
    print("Query Ideas:")
    for query_idea in query_ideas:
        print(query_idea)
        db_connection.execute_query(query_idea) 
        

    # Close the database connection
    db_connection.close_connection()

if __name__ == "__main__":
    main()
