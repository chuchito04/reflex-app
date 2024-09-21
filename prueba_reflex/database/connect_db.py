from sqlmodel import create_engine

paimef_dev = "mysql+pymysql://paimef_user:Cromero252525@3.141.197.87[:3306]/purpura_semujeres"

localhost = "mysql+pymysql://root@127.0.0.1:3306/municipios"

def connect():
    engine = create_engine(localhost)
    return engine