# Importação de modo de interação com o sistema operacional
import os
# Importação de uma função que retorna uma aplicação WSGI
from django.core.wsgi import get_wsgi_application

# Identificação do arquivo de configurações que o Django deve usar
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LivrariaIGE.settings")

# Cria a aplicação WSGI
application = get_wsgi_application()
