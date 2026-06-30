import os
import boto3
from pathlib import Path
from dotenv import load_dotenv

# CARREGA AS CHAVES SECRETAS
load_dotenv()

# ACESSO PARA A AWS (Cliente S3)
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='sa-east-1' 
)

nome_do_bucket = 'edaecommerce-120822897129-sa-east-1-an' 

# Aponta para a pasta onde os Parquets foram salvos
pasta_local = Path(r"C:\Users\daniel-pc\Documents\Projetos\Analise Exploratória E-Commerce\dados_limpos_parquet")

print("--- INICIANDO UPLOAD PARA O AWS S3 ---")

# O comando .glob('*.parquet') faz o Python procurar apenas os arquivos parquet na pasta
for caminho_arquivo in pasta_local.glob('*.parquet'):
    
    # Define como o arquivo vai se chamar lá dentro da AWS
    # Coloquei o prefixo 'camada_bronze/' para simular a arquitetura real de um Data Lake Medallion
    caminho_no_s3 = f"camada_bronze/{caminho_arquivo.name}"
    
    print(f"Enviando: {caminho_arquivo.name} ...")
    
    # O motor de upload puro e bruto
    s3_client.upload_file(
        Filename=str(caminho_arquivo),  
        Bucket=nome_do_bucket,          
        Key=caminho_no_s3               
    )

print("\nTodos os arquivos Parquet no Data Lake da AWS!")