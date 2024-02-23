import boto3
import os

# Create a boto3 session using AWS access keys
# Cria uma sessão boto3 usando as chaves de acesso da AWS
# Crear una sesión de boto3 usando las claves de acceso de AWS
session = boto3.Session(aws_access_key_id='###', aws_secret_access_key='###')

# Create an S3 resource object
# Cria um objeto de recurso S3
# Crear un objeto de recurso S3
s3 = session.resource('s3')

# Specify the S3 bucket
# Especifique o bucket S3
# Especificar el bucket de S3
my_bucket = s3.Bucket('BUCKET_NAME')

# Directory where the files will be downloaded
# Diretório onde os arquivos serão baixados
# Directorio donde se descargarán los archivos
download_dir = 'downloads/'

# Check if the download directory exists, if not, create it
# Verifica se o diretório de download existe, se não, cria
# Compruebe si el directorio de descarga existe, si no, créelo
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Replace the line below to perform reading and downloading within a specific folder in the bucket
# Substitua a linha abaixo para realizar a leitura e o download dentro de uma pasta específica no bucket
# Reemplace la línea a continuación para realizar la lectura y descarga dentro de una carpeta específica en el bucket
#for my_bucket_object in my_bucket.objects.filter(Prefix='prestadores/'):

# Iterate through all objects in the S3 bucket
# Itera através de todos os objetos no bucket S3
# Iterar a través de todos los objetos en el bucket de S3
for my_bucket_object in my_bucket.objects.all():
    # Get the filename
    # Obter o nome do arquivo
    # Obtener el nombre del archivo
    filename = my_bucket_object.key
    
    # Download the file only if it is not a directory
    # Baixa o arquivo apenas se não for um diretório
    # Descargar el archivo solo si no es un directorio
    if not filename.endswith('/'):
        local_filepath = os.path.join(download_dir, filename)
        s3.meta.client.download_file('BUCKET_NAME', filename, local_filepath)
    
        # Print the downloaded file name
        # Imprime o nome do arquivo baixado
        # Imprimir el nombre del archivo descargado
        print(f"Downloaded file: {filename}")