#from langchain_neo4j import Neo4jGraph
from langchain_community.graphs import Neo4jGraph
from dotenv import load_dotenv
from neo4j import GraphDatabase
import os
import warnings
warnings.filterwarnings('ignore')

#load environment
load_dotenv()

#Neo4j login details
NEO4J_URI=os.environ["NEO4J_URI"]
NEO4J_USERNAME=os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD=os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE=os.environ["NEO4J_DATABASE"]
AURA_INSTANCEID=os.environ["AURA_INSTANCEID"]
AURA_INSTANCENAME=os.environ["AURA_INSTANCENAME"]

AUTH=(NEO4J_USERNAME,NEO4J_PASSWORD)

#create driver for graph database
driver=GraphDatabase.driver(NEO4J_URI,auth=AUTH)

kg = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
) # database=NEO4J_DATABASE,

cypher = """
  MATCH (n) 
  RETURN count(n) as numberOfNodes
  """

result = kg.query(cypher)
print(f"There are {result[0]['numberOfNodes']} nodes in this graph.")