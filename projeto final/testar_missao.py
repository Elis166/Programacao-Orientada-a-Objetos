import importlib.util

caminho = "missoes/missao-2.py"

spec = importlib.util.spec_from_file_location(
    "missao_armario", caminho
)

modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)

MissaoArmario = modulo.MissaoArmario

missao = MissaoArmario()
missao.menu_locais()
