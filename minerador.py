import json
import hashlib
import time
import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

ARQUIVO_BLOCOS = "blocos.json"
ARQUIVO_LOG = "log_mineracao.txt"
RECOMPENSA_BTC = 3.125

def carregar_blocos():
    if not os.path.exists(ARQUIVO_BLOCOS):
        return []
    with open(ARQUIVO_BLOCOS, "r") as f:
        return json.load(f)

def salvar_blocos(blocos):
    with open(ARQUIVO_BLOCOS, "w") as f:
        json.dump(blocos, f, indent=4)

def salvar_log(bloco, hash_final, tentativas, tempo):
    # Roda o log se ultrapassar 5 MB
    if os.path.exists(ARQUIVO_LOG) and os.path.getsize(ARQUIVO_LOG) > 5 * 1024 * 1024:
        nome_antigo = ARQUIVO_LOG.replace(".txt", f"_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
        os.rename(ARQUIVO_LOG, nome_antigo)

    with open(ARQUIVO_LOG, "a") as f:
        f.write(f"Bloco #{bloco['numero']} minerado em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Hash: {hash_final}\n")
        f.write(f"Nonce encontrado: {bloco['nonce']}\n")
        f.write(f"Tentativas: {tentativas}\n")
        f.write(f"Tempo: {tempo:.2f}s\n")
        f.write(f"Recompensa: {RECOMPENSA_BTC:.3f} BTC\n")
        f.write("-" * 50 + "\n")

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_blocos_pendentes(blocos):
    pendentes = [b for b in blocos if b['nonce'] is None]
    if not blocos:
        print("\nNenhum bloco encontrado.")
    elif not pendentes:
        print("\nNão há blocos pendentes de validação.")
    else:
        print("\nBlocos pendentes:")
        for bloco in pendentes:
            print(f"- Bloco #{bloco['numero']} (criado em {bloco['data']})")

def minerar_bloco(bloco, hash_anterior):
    dificuldade = bloco["dificuldade"]
    prefixo = "0" * dificuldade
    tentativas = 0
    inicio = time.time()
    nonce = 0

    while True:
        conteudo = f"{bloco['numero']}{bloco['data']}{bloco['conteudo']}{hash_anterior}{nonce}"
        hash_atual = hashlib.sha256(conteudo.encode()).hexdigest()
        tentativas += 1

        print(f"{datetime.now().strftime('%H:%M:%S')} | Tentativa: {tentativas:,} | Nonce: {nonce} | Hash: {hash_atual[:16]}...", end='\r')

        if hash_atual.startswith(prefixo):
            fim = time.time()
            bloco["nonce"] = str(nonce)
            bloco["hash"] = hash_atual
            salvar_blocos(blocos)
            salvar_log(bloco, hash_atual, tentativas, fim - inicio)

            print()  # quebra a linha
            print(Fore.GREEN + f"\n✅ Hash minerada: {hash_atual}")
            print(f"⏱️ Tempo: {fim - inicio:.2f}s | Tentativas: {tentativas}\n")
            return

        nonce += 1

def exibir_log():
    if not os.path.exists(ARQUIVO_LOG):
        print("\nNenhum log de mineração encontrado.")
        return
    with open(ARQUIVO_LOG, "r") as f:
        print(f.read())

# LOOP PRINCIPAL
while True:
    limpar_tela()
    blocos = carregar_blocos()
    exibir_blocos_pendentes(blocos)

    print("\nMenu:")
    print("1. Atualizar blocos")
    print("2. Iniciar mineração")
    print("3. Ver log de mineração")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        continue

    elif opcao == "2":
        pendentes = [b for b in blocos if b['nonce'] is None]
        if not pendentes:
            input("\nNenhum bloco pendente. Pressione ENTER para voltar ao menu.")
            continue

        try:
            numero_escolhido = int(input("\nDigite o número do bloco que deseja minerar: "))
        except ValueError:
            input("\nNúmero inválido. Pressione ENTER para voltar.")
            continue

        bloco = next((b for b in pendentes if b['numero'] == numero_escolhido), None)
        if not bloco:
            input("\nBloco não encontrado ou já minerado. Pressione ENTER para voltar.")
            continue

        # Validação de encadeamento
        if bloco['numero'] > 1:
            anterior = next((b for b in blocos if b['numero'] == bloco['numero'] - 1), None)
            if not anterior or anterior.get("hash") != bloco.get("prev"):
                input("\nErro: hash do bloco anterior não confere. Pressione ENTER para voltar.")
                continue

        limpar_tela()
        print("=" * 40)
        print(f"INICIANDO MINERAÇÃO - BLOCO {bloco['numero']}")
        print("=" * 40)

        minerar_bloco(bloco, bloco["prev"])
        input("Pressione ENTER para voltar ao menu.")

    elif opcao == "3":
        limpar_tela()
        exibir_log()
        input("\nPressione ENTER para voltar ao menu.")

    elif opcao == "4":
        print("\nEncerrando...")
        break

    else:
        input("\nOpção inválida. Pressione ENTER para continuar.")
