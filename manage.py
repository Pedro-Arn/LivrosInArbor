#!/usr/bin/env python
# Linha de comando do Django para tarefas administrativas
import os
# Importação do módulo que fornece funções para interagir com o interpretador Python
import sys


def main():
    # Execução de tarefas administrativas
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LivrariaIGE.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
