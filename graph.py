from neo4j import GraphDatabase

class Neo4JConnector:
    def __init__(self, uri, user, password) -> None:
       self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)
    
    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
               "SET a.message = $message "
               "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

#connector = Neo4JConnector("bolt://44.199.227.120:7687", "neo4j", "spars-molecule-tomorrows")
connector = Neo4JConnector("bolt://localhost:7689", "neo4j", "12345678")
connector.print_greeting("hello everyone")
connector.close()
