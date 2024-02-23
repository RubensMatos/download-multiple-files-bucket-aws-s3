# download-multiple-files-bucket-aws-s3

## Prerequisites / Pré-requisitos / Requisitos previos

Before using this script, you need to have Python installed in your environment. Python 3.6 or higher is recommended.

Antes de usar este script, você precisa ter o Python instalado em seu ambiente. Recomenda-se o Python 3.6 ou superior.

Antes de utilizar este script, asegúrese de tener Python instalado en su entorno. Se recomienda Python 3.6 o superior.

Additionally, you will need AWS credentials to access your S3 bucket. If you don't have them already, you can follow the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) to create an IAM user and generate the necessary credentials.

Além disso, você precisará de credenciais da AWS para acessar seu bucket S3. Se você ainda não as tiver, pode seguir a [documentação da AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) para criar um usuário IAM e gerar as credenciais necessárias.

Además, necesitará credenciales de AWS para acceder a su bucket de S3. Si aún no las tiene, puede seguir la [documentación de AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) para crear un usuario IAM y generar las credenciales necesarias.

```bash
pip install boto3