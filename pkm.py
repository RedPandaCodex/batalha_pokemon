import random

class Pokemon:
    def __init__(self, apelido, altura, peso, especie, tipagem, geracao, hp, ataque, defesa):
        self.__apelido = apelido
        self.__altura = altura
        self.__peso = peso
        self.__especie = especie
        self.__tipagem = tipagem
        self.__geracao = geracao
        self.__hp = hp
        self.__ataque = ataque
        self.__defesa = defesa

    # Getters (necessários para acessar os atributos privados)
    @property
    def apelido(self):
        return self.__apelido

    @property
    def hp(self):
        return self.__hp

    @property
    def ataque(self):
        return self.__ataque

    @property
    def defesa(self):
        return self.__defesa

    @hp.setter
    def hp(self, novo_hp):
        self.__hp = max(0, novo_hp)  # Garante que o HP nunca seja negativo

    def pokedex_informacoes(self):
        informacoes = f"{self.__apelido} é um Pokémon {self.__especie} do tipo {self.__tipagem} introduzido na {self.__geracao}, tem a altura de {self.__altura} e pesa {self.__peso}."
        print(informacoes)

    def atacar(self, outro_pokemon):
        dano = self.__ataque - outro_pokemon.defesa
        if dano <= 0:
            dano = 1  # Garante que pelo menos 1 de dano seja causado
        outro_pokemon.hp -= dano
        print(f"{self.__apelido} atacou {outro_pokemon.apelido} e causou {dano} de dano!")
        if outro_pokemon.hp <= 0:
            print(f"{outro_pokemon.apelido} desmaiou!")

    def esta_vivo(self):
        return self.__hp > 0

# Instâncias dos pokémons
oshawott = Pokemon("Oshawott", "0.5m", "5.9kg", "Lontra-do-Mar", "Água", "Geração V", 55, 55, 45)
snivy = Pokemon("Snivy", "0.6m", "8.1kg", "Serpente", "Planta", "Geração V", 45, 45, 55)
tepig = Pokemon("Tepig", "0.5m", "9.9kg", "Leitão", "Fogo", "Geração V", 65, 63, 45)

pokemons = {
    "1": oshawott,
    "2": snivy,
    "3": tepig
}

# Mostra informações dos pokémons
oshawott.pokedex_informacoes()
snivy.pokedex_informacoes()
tepig.pokedex_informacoes()

# Função de batalha
def batalha(pokemon1, pokemon2):
    print(f"\nGo! {pokemon1.apelido} vs {pokemon2.apelido}!")
    turno = 1
    while pokemon1.esta_vivo() and pokemon2.esta_vivo():
        print(f"\nTurno {turno}")
        pokemon1.atacar(pokemon2)
        if not pokemon2.esta_vivo():
            print(f"{pokemon1.apelido} venceu a batalha!")
            break
        pokemon2.atacar(pokemon1)
        if not pokemon1.esta_vivo():
            print(f"{pokemon2.apelido} venceu a batalha!")
            break
        print(f"HP {pokemon1.apelido}: {pokemon1.hp} | HP {pokemon2.apelido}: {pokemon2.hp}")
        turno += 1

# Escolha de pokémon pelo jogador
def escolher_pokemon(jogador_num):
    print(f"\nJogador {jogador_num}, escolha seu Pokémon:")
    for chave, pokemon in pokemons.items():
        print(f"{chave} - {pokemon.apelido}")
    escolha = None
    while escolha not in pokemons:
        escolha = input("Digite o número do Pokémon escolhido: ")
        if escolha not in pokemons:
            print("Pokémon inválido. Tente novamente.")
    # Criar nova instância com os mesmos atributos
    p = pokemons[escolha]
    return Pokemon(p.apelido, p._Pokemon__altura, p._Pokemon__peso, p._Pokemon__especie, p._Pokemon__tipagem, p._Pokemon__geracao, p.hp, p.ataque, p.defesa)

# Função principal
def main():
    pokemon_jogador1 = escolher_pokemon(1)
    pokemon_jogador2 = escolher_pokemon(2)
    batalha(pokemon_jogador1, pokemon_jogador2)

if __name__ == "__main__":
    main()
