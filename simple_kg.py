import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

#load environment
load_dotenv()

NEO4J_URI=os.environ["NEO4J_URI"]
NEO4J_USERNAME=os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD=os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE=os.environ["NEO4J_DATABASE"]
AURA_INSTANCEID=os.environ["AURA_INSTANCEID"]
AURA_INSTANCENAME=os.environ["AURA_INSTANCENAME"]

AUTH=(NEO4J_USERNAME,NEO4J_PASSWORD)

#create driver for graph database
driver=GraphDatabase.driver(NEO4J_URI,auth=AUTH)

# def connect_query():
#     try:
#         with driver.session(database=NEO4J_DATABASE) as session:
#             print("I am in session")
#             result=session.run("MATCH (n) RETURN count(n)")
#             count=result.single().value()
#             print(f"Number of nodes : {count}")
#     except Exception as e:
#         print(f"Error :{e}")
#     finally:
#         driver.close()

#create entity
def create_entities(x):
    #Albert Node
    x.run("MERGE (a:Person {name: 'Albert Einstine'})")

    x.run("MERGE (p:Subject {name: 'Physics'})")
    x.run("MERGE (g:Country {name: 'Germany'})")
    x.run("MERGE (n:Nobelprize {name: 'Won Nobel Prize'})")

#create relationship
def create_relationship(x):
    x.run(""" 
 MATCH (a:Person {name: 'Albert Einstine'}),(p:Subject {name: 'Physics'})
 MERGE (a)-[:STUDIED]->(p)
      """)
    
    x.run(""" 
 MATCH (a:Person {name: 'Albert Einstine'}),(g:Country {name: 'Germany'})
 MERGE (a)-[:COUNTRY]->(g)
      """)
    
    x.run(""" 
 MATCH (a:Person {name: 'Albert Einstine'}),(n:Nobelprize {name: 'Won Nobel Prize'})
 MERGE (a)-[:Nobelprize]->(n)
      """)
    
# def query_graph(cypher_query):
#     try:
#         with driver.session(database=NEO4J_DATABASE) as session:
#             result=session.run(cypher_query)
#             for record in result:
#                 print(record["name"])
#     except Exception as e:
#         print(f"Error :{e}")
#     finally:
#         driver.close()

# def query_graph_path(cypher_query):
#     try:
#         with driver.session(database=NEO4J_DATABASE) as session:
#             result=session.run(cypher_query)
#             for record in result:
#                 print(record["path"])
#     except Exception as e:
#         print(f"Error :{e}")
#     finally:
#         driver.close()

def build_knowledge_graph():
    try:
        with driver.session(database=NEO4J_DATABASE) as session:
            session.execute_write(create_entities)
            session.execute_write(create_relationship)
    except Exception as e:
        print(f"Error {e}")
    finally:
        driver.close()

        

def clear_database():
    """
    Deletes all nodes and relationships in a Neo4j database.

    :param uri: Neo4j connection URI (e.g., "bolt://localhost:7687")
    :param user: Username for Neo4j
    :param password: Password for Neo4j
    """
   
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    
    #driver.close()
    print("✅ All nodes and relationships have been deleted.")




if __name__ == "__main__":
    print("Start creating nodes and relationships")
    clear_database()
    build_knowledge_graph()


    