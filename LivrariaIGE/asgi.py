# Importação de modo de interação com o sistema operacional
import os
# Importação de uma função que retorna uma aplicação ASGI para 
# o Django (gerenciamento as requisições HTTP)
from django.core.asgi import get_asgi_application

# Identificação do arquivo de configurações que o Django deve usar
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LivrariaIGE.settings")

# Cria a aplicação ASGI
application = get_asgi_application()
