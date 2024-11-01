from connection import Connection

class CreatingDatabaseStructure():

    def __init__(self):
        CreatingDatabaseStructure.create_structure()
        
    @staticmethod    
    def create_table_production():
        _qry = """
        CREATE TABLE IF NOT EXISTS producao (
            cod SERIAL PRIMARY KEY,
            information VARCHAR NOT NULL,
            delivery DATE NOT NULL
        );
        """
        Connection.execute(_qry)
        
    @staticmethod
    def delete_all_records():
        _qry = "DELETE FROM producao;"
        Connection.execute(_qry)
        
    @staticmethod
    def insert_records():
        _qry = """
        INSERT INTO producao (information, delivery)
        SELECT 
            'Produto ' || generate_series(1, 50),  -- Descrição aleatória com nome do produto
            NOW()::date - (random() * 365)::int  -- Data aleatória no último ano
        FROM generate_series(1, 50);
        """
        Connection.execute(_qry)

    @staticmethod
    def create_structure():
        CreatingDatabaseStructure.create_table_production()
        CreatingDatabaseStructure.delete_all_records()
        CreatingDatabaseStructure.insert_records()