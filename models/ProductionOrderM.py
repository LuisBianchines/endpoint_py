from connection import Connection
import uuid
from datetime import datetime

class ProductionOrderModel:
    cod = None
    information = None
    delivery = None

    def show_production(param):
        sql = """SELECT * FROM producao"""
        filters = []
        try:
            if param:
                try:
                    # Tenta converter o parâmetro para o formato yyyy-MM-dd
                    param_date = datetime.strptime(param, '%d/%m/%Y').strftime('%Y-%m-%d')
                    filters.append(f"CAST(delivery AS TEXT) ILIKE '%%{param_date}%%'")
                except ValueError:
                    # Se a conversão falhar, trata o parâmetro como uma string normal
                    filters.append(f"information ILIKE '%%{param}%%'")
                    filters.append(f"CAST(delivery AS TEXT) ILIKE '%%{param}%%'")
                    filters.append(f"cod::text ILIKE '%%{param}%%'")  # Convertendo cod para texto para usar ILIKE

            if filters:
                sql += " WHERE " + " OR ".join(filters)  # Usando OR para combinar os filtros
            
            sql += " LIMIT 50"
            
            res = Connection.open_query_param_to_json(sql,(param,))
            
            return res,200
        except Exception as error:
            return {
                'message': str(error)
            },400

       
