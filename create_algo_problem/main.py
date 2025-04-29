#!/usr/bin/env python3
import os
import argparse
import sys

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def validate_execution_context():
    """Ensure script isn't run from restricted directories"""
    current_dir = os.getcwd()

    # Agora só restringe execução a partir do próprio diretório do script
    if current_dir == SCRIPT_DIR:
        print("❌ Execução proibida: Diretório do script detectado")
        print(f"📛 Caminho restrito: {SCRIPT_DIR}")
        print("💡 Dica: Execute a partir de um diretório onde deseja criar o projeto")
        return False

    return True


def create_project(project_name):
    """Create full project structure with verbose logging"""
    try:
        # Usa o diretório atual como base para criar o projeto
        base_projects_dir = os.getcwd()
        project_path = os.path.join(base_projects_dir, project_name)

        print(f"\n🔎 Validando projeto '{project_name}'...")
        if os.path.exists(project_path):
            print(f"⛔ Conflito: Projeto já existe em {project_path}")
            return False

        print("🚧 Iniciando criação do projeto 🚧")
        print(f"📌 Local base: {base_projects_dir}")
        print(f"🏗️ Construindo estrutura para: {project_name}")

        # Create main directories
        required_dirs = [
            ("codes", "Implementações de código"),
            ("tests", "Casos de teste"),
            ("notes", "Notas de pesquisa"),
        ]

        for dir_name, purpose in required_dirs:
            dir_path = os.path.join(project_path, dir_name)
            os.makedirs(dir_path)
            print(f"📂 Criado diretório {purpose}: {dir_path}")

        # Create empty description file
        desc_file = os.path.join(project_path, "description.md")
        open(desc_file, "w").close()
        print(f"📄 Criado arquivo de descrição: {desc_file}")

        print(f"\n✅ Projeto criado com sucesso em {project_path}")
        print(f"🗂️ Total de itens criados: {len(required_dirs) + 1}")
        return True
    except Exception as e:
        print(f"\n🔥 Falha crítica durante a criação: {str(e)}")
        return False


def main():
    # Configure command-line interface
    parser = argparse.ArgumentParser(
        prog="algo-scaffold",
        description="Inicializador de Projetos para Problemas de Algoritmos",
        epilog="Exemplo: algo-scaffold two-sum-problem",
    )

    parser.add_argument(
        "project",
        metavar="NOME_DO_PROJETO",
        help="Nome para o novo projeto de algoritmo",
    )

    args = parser.parse_args()

    # Validate environment first
    if not validate_execution_context():
        sys.exit(1)

    # Attempt project creation
    if not create_project(args.project):
        sys.exit(1)


if __name__ == "__main__":
    main()
