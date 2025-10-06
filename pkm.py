import random
import time

class Pokemon:
    def __init__(self, apelido, altura, peso, especie, tipagem, geracao, hp, ataque, defesa, movimentos):
        self.__apelido = apelido
        self.__altura = altura
        self.__peso = peso
        self.__especie = especie
        self.__tipagem = tipagem
        self.__geracao = geracao
        self.__hp = hp
        self.__hp_max = hp
        self.__ataque = ataque
        self.__defesa = defesa
        self.__movimentos = movimentos

    @property
    def apelido(self):
        return self.__apelido

    @property
    def hp(self):
        return self.__hp

    @property
    def movimentos(self):
        return self.__movimentos

    @property
    def tipagem(self):
        return self.__tipagem

    @hp.setter
    def hp(self, novo_hp):
        self.__hp = max(0, min(novo_hp, self.__hp_max))

    def barra_hp(self):
        tamanho_barra = 20
        proporcao = self.__hp / self.__hp_max
        barras = int(proporcao * tamanho_barra) * "█"
        espacos = (tamanho_barra - len(barras)) * " "
        return f"[{barras}{espacos}] {self.__hp}/{self.__hp_max} HP"

    def esta_vivo(self):
        return self.__hp > 0

    def atacar(self, outro_pokemon, movimento):
        if movimento["pp"] <= 0:
            print(f"{self.__apelido} não tem mais PP para {movimento['nome']}!")
            return False

        movimento["pp"] -= 1

        # Verificar precisão
        chance = random.randint(1, 100)
        if chance > movimento.get("precisao", 100):
            time.sleep(1)
            print(f"{self.__apelido} tentou usar {movimento['nome']}, mas errou!")
            return False

        tipo_mov = movimento.get("tipo_movimento", "dano")

        if tipo_mov == "dano":
            variacao = random.randint(-5, 5)
            dano = self.__ataque + movimento["poder"] - outro_pokemon._Pokemon__defesa + variacao

            vantagens = {"Água": "Fogo", "Fogo": "Planta", "Planta": "Água"}
            desvantagens = {"Água": "Planta", "Fogo": "Água", "Planta": "Fogo"}

            if vantagens.get(movimento["tipo"]) == outro_pokemon.tipagem:
                dano = int(dano * 1.5)
                time.sleep(1)
                print("É super eficaz!")
            elif desvantagens.get(movimento["tipo"]) == outro_pokemon.tipagem:
                dano = int(dano * 0.5)
                time.sleep(1)
                print("Não é muito eficaz...")

            if dano <= 0:
                dano = 1

            outro_pokemon.hp -= dano
            time.sleep(1)
            print(f"{self.__apelido} usou {movimento['nome']} e causou {dano} de dano em {outro_pokemon.apelido}!")

        elif tipo_mov == "status":
            efeito = movimento.get("efeito")
            alvo = movimento.get("alvo", "self")  # "self" ou "oponente"
            target_pokemon = self if alvo == "self" else outro_pokemon

            if efeito == "defesa_up":
                target_pokemon._Pokemon__defesa += 5
                time.sleep(1)
                print(f"{target_pokemon.apelido} teve sua defesa aumentada em 5!")
            elif efeito == "ataque_up":
                target_pokemon._Pokemon__ataque += 5
                time.sleep(1)
                print(f"{target_pokemon.apelido} teve seu ataque aumentado em 5!")
            elif efeito == "defesa_down":
                target_pokemon._Pokemon__defesa = max(0, target_pokemon._Pokemon__defesa - 5)
                time.sleep(1)
                print(f"{target_pokemon.apelido} teve sua defesa diminuída em 5!")
            elif efeito == "ataque_down":
                target_pokemon._Pokemon__ataque = max(0, target_pokemon._Pokemon__ataque - 5)
                time.sleep(1)
                print(f"{target_pokemon.apelido} teve seu ataque diminuído em 5!")

        return True

    def usar_pocao(self):
        cura = 30
        self.hp += cura
        print(f"{self.__apelido} usou uma Poção e recuperou {cura} HP!")

    def pokedex_informacoes(self):
        print(f"\n=== {self.__apelido} ===")
        print(f"Espécie: {self.__especie}")
        print(f"Tipo: {self.__tipagem}")
        print(f"Geração: {self.__geracao}")
        print(f"Altura: {self.__altura}, Peso: {self.__peso}")
        print(f"HP: {self.__hp}/{self.__hp_max}, Ataque: {self.__ataque}, Defesa: {self.__defesa}")
        print("\nMovimentos disponíveis:")
        for mov in self.__movimentos:
            print(f"- {mov['nome']} (Tipo: {mov['tipo']}, Poder: {mov['poder']}, PP: {mov['pp']}, Precisão: {mov.get('precisao',100)}%, Tipo Mov: {mov['tipo_movimento']})")
        print(f"=== {self.__apelido} ===")

# =================== POKÉMONS ===================
oshawott = Pokemon(
    "Oshawott", "0.5m", "5.9kg", "Lontra-do-Mar", "Água", "Geração V", 55, 55, 45,
    movimentos=[
        {"nome": "Water Gun", "poder": 10, "pp": 5, "tipo": "Água", "tipo_movimento": "dano", "precisao": 95},
        {"nome": "Tackle", "poder": 5, "pp": 10, "tipo": "Normal", "tipo_movimento": "dano", "precisao": 100},
        {"nome": "Aqua Jet", "poder": 8, "pp": 5, "tipo": "Água", "tipo_movimento": "dano", "precisao": 90},
        {"nome": "Shell Shield", "poder": 0, "pp": 5, "tipo": "Normal", "tipo_movimento": "status", "efeito": "defesa_up", "alvo": "self", "precisao": 100},
        {"nome": "Tide Crash", "poder": 0, "pp": 3, "tipo": "Água", "tipo_movimento": "status", "efeito": "ataque_down", "alvo": "oponente", "precisao": 90}
    ]
)

snivy = Pokemon(
    "Snivy", "0.6m", "8.1kg", "Serpente", "Planta", "Geração V", 45, 45, 55,
    movimentos=[
        {"nome": "Vine Whip", "poder": 10, "pp": 5, "tipo": "Planta", "tipo_movimento": "dano", "precisao": 95},
        {"nome": "Tackle", "poder": 5, "pp": 10, "tipo": "Normal", "tipo_movimento": "dano", "precisao": 100},
        {"nome": "Leaf Tornado", "poder": 12, "pp": 3, "tipo": "Planta", "tipo_movimento": "dano", "precisao": 85},
        {"nome": "Agility", "poder": 0, "pp": 3, "tipo": "Normal", "tipo_movimento": "status", "efeito": "ataque_up", "alvo": "self", "precisao": 100},
        {"nome": "Root Bind", "poder": 0, "pp": 3, "tipo": "Planta", "tipo_movimento": "status", "efeito": "defesa_down", "alvo": "oponente", "precisao": 90}
    ]
)

tepig = Pokemon(
    "Tepig", "0.5m", "9.9kg", "Leitão", "Fogo", "Geração V", 65, 63, 45,
    movimentos=[
        {"nome": "Ember", "poder": 10, "pp": 5, "tipo": "Fogo", "tipo_movimento": "dano", "precisao": 95},
        {"nome": "Tackle", "poder": 5, "pp": 10, "tipo": "Normal", "tipo_movimento": "dano", "precisao": 100},
        {"nome": "Flame Charge", "poder": 12, "pp": 3, "tipo": "Fogo", "tipo_movimento": "dano", "precisao": 90},
        {"nome": "Defense Curl", "poder": 0, "pp": 5, "tipo": "Normal", "tipo_movimento": "status", "efeito": "defesa_up", "alvo": "self", "precisao": 100},
        {"nome": "Smoky Bind", "poder": 0, "pp": 3, "tipo": "Fogo", "tipo_movimento": "status", "efeito": "ataque_down", "alvo": "oponente", "precisao": 90}
    ]
)

pokemons = {
    "1": oshawott,
    "2": snivy,
    "3": tepig
}

# =================== ESCOLHA DE POKÉMON ===================
def escolher_pokemon(jogador_num):
    print(f"\nJogador {jogador_num}, escolha seu Pokémon:")
    for chave, pkm in pokemons.items():
        print(f"{chave} - {pkm.apelido}")

    escolha = None
    while escolha not in pokemons:
        escolha = input("Digite o número do Pokémon escolhido: ")
        if escolha not in pokemons:
            print("Escolha inválida. Tente novamente.")

    # Criar nova instância para que cada jogador tenha Pokémon independente
    p = pokemons[escolha]
    novo_pokemon = Pokemon(p.apelido, p._Pokemon__altura, p._Pokemon__peso, p._Pokemon__especie,
                           p._Pokemon__tipagem, p._Pokemon__geracao, p.hp, p._Pokemon__ataque,
                           p._Pokemon__defesa, [dict(m) for m in p.movimentos])

    # Mostrar informações
    novo_pokemon.pokedex_informacoes()

    return novo_pokemon

# =================== ESCOLHA DE 4 MOVIMENTOS ===================
def escolher_movimentos(pokemon):
    print("\n=== Escolha de ataques ===")
    print(f"Escolha 4 movimentos para {pokemon.apelido}:")
    movimentos_disponiveis = pokemon.movimentos
    movimentos_escolhidos = []

    while len(movimentos_escolhidos) < 4:
        print("\nMovimentos disponíveis:")
        for i, mov in enumerate(movimentos_disponiveis):
            if mov not in movimentos_escolhidos:
                print(f"{i+1} - {mov['nome']} (PP: {mov['pp']}, Precisão: {mov.get('precisao',100)}%)")

        escolha = input(f"Escolha o {len(movimentos_escolhidos)+1}º movimento (digite o número): ")
        try:
            escolha_idx = int(escolha) - 1
            if escolha_idx < 0 or escolha_idx >= len(movimentos_disponiveis):
                print("Escolha inválida! Tente novamente.")
            elif movimentos_disponiveis[escolha_idx] in movimentos_escolhidos:
                print("Movimento já escolhido! Selecione outro.")
            else:
                movimentos_escolhidos.append(movimentos_disponiveis[escolha_idx])
        except ValueError:
            print("Entrada inválida! Digite um número.")

    pokemon._Pokemon__movimentos = movimentos_escolhidos
    print(f"\nMovimentos finais de {pokemon.apelido}: {[m['nome'] for m in movimentos_escolhidos]}")

# =================== BATALHA ===================
def batalha(pokemon1, pokemon2):
    pocao1, pocao2 = 3, 3
    turno = 1

    while pokemon1.esta_vivo() and pokemon2.esta_vivo():
        time.sleep(2)
        print(f"\n===== Turno {turno} =====")
        print(f"{pokemon1.apelido}: {pokemon1.barra_hp()} | {pokemon2.apelido}: {pokemon2.barra_hp()}")

        for jogador, atacante, defensor, pocao in [(1, pokemon1, pokemon2, pocao1), (2, pokemon2, pokemon1, pocao2)]:
            if not atacante.esta_vivo() or not defensor.esta_vivo():
                continue

            print(f"\nJogador {jogador}, é a vez de {atacante.apelido}")
            print("1 - Atacar")
            print(f"2 - Usar Poção ({pocao} restantes)")
            acao = input("Escolha a ação: ")

            if acao == "1":
                print("\nEscolha o movimento:")
                for i, mov in enumerate(atacante.movimentos):
                    print(f"{i+1} - {mov['nome']} (PP: {mov['pp']}, Precisão: {mov.get('precisao',100)}%)")
                mov_escolha = None
                while mov_escolha not in range(1, len(atacante.movimentos)+1):
                    try:
                        mov_escolha = int(input("\nNúmero do movimento: "))
                    except ValueError:
                        continue
                atacante.atacar(defensor, atacante.movimentos[mov_escolha-1])

            elif acao == "2":
                if pocao > 0:
                    atacante.usar_pocao()
                    if atacante == pokemon1:
                        pocao1 -= 1
                    else:
                        pocao2 -= 1
                else:
                    print("Sem poções restantes! Perdeu a vez.")
            else:
                print("Ação inválida! Perdeu a vez.")

            if not defensor.esta_vivo():
                time.sleep(1)
                print(f"\n{defensor.apelido} desmaiou!")
                time.sleep(1)
                print(f"\n{atacante.apelido} venceu a batalha!")
                return

        turno += 1

# =================== EXECUÇÃO PRINCIPAL ===================
def main():
    print("=== Batalha Pokémon PvP ===")
    pokemon_jogador1 = escolher_pokemon(1)
    escolher_movimentos(pokemon_jogador1)

    pokemon_jogador2 = escolher_pokemon(2)
    escolher_movimentos(pokemon_jogador2)

    batalha(pokemon_jogador1, pokemon_jogador2)

if __name__ == "__main__":
    main()
