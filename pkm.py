import random
class pokemon():
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

    def pokedex_informacoes(self):
        informacoes = f"{self.__apelido} é um pokemon {self.__especie} do tipo {self.__tipagem} introduzido na {self.__geracao}, tem a altura de {self.__altura} e pesa {self.__peso}"
        print(informacoes)

#<---------------------------------------------------------------------------------------->
#sistema de ataque
def atacar(self, outro_pokemon):
        dano = self.ataque - outro_pokemon.defesa
        if dano <= 0:
            dano = 1  # garante que pelo menos 1 de dano seja causado
        #Vai diminuir depedendo da defesa
        outro_pokemon.hp -= dano
        print(f"{self.apelido} attacked {outro_pokemon.apelido} and caused {dano} of damage!") #texto de quantidade de dano
        if outro_pokemon.hp <= 0:
            outro_pokemon.hp = 0
            print(f"{outro_pokemon.apelido} fainted!")

#certificar que o pokemon está com HP sobrando
def esta_vivo(self):
    return self.hp > 0
#<---------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------->
oshawott = pokemon(apelido="Oshawott", altura="0.5m", peso="5.9kg", especie="Lontra-do-Mar", tipagem="Água", geracao="Geração V", hp=55, ataque=55, defesa=45)
snivy = pokemon(apelido="Snivy", altura="0.6m", peso="8.1kg", especie="Serpente", tipagem="Planta", geracao="Geração V", hp=45, ataque=45, defesa=55)
tepig = pokemon(apelido="Tepig", altura="0.5m", peso="9.9kg", especie="Leitão", tipagem="Fogo", geracao="Geração V", hp=65, ataque=63, defesa=45)

#lista para a escolha dos pokemons
pokemons = {
    "1": oshawott,
    "2": snivy,
    "3": tepig
}

oshawott.pokedex_informacoes()
snivy.pokedex_informacoes()
tepig.pokedex_informacoes()
#<---------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------->
#Sistema de batalha
def batalha(pokemon1, pokemon2):
    print(f"\nGo! {pokemon1.apelido} and {pokemon2.apelido}!")
    turnos = 1
    while pokemon1.esta_vivo() and pokemon2.esta_vivo():
        print(f"\nTurn {turnos}")
        # pokemon1 ataca pokemon2
        pokemon1.atacar(pokemon2)
        if not pokemon2.esta_vivo():
            print(f"{pokemon1.apelido} venceu a batalha!")
            break
        # pokemon2 ataca pokemon1
        pokemon2.atacar(pokemon1)
        if not pokemon1.esta_vivo():
            print(f"{pokemon2.apelido} venceu a batalha!")
            break
        print(f"HP {pokemon1.apelido}: {pokemon1.hp} | HP {pokemon2.apelido}: {pokemon2.hp}")
        turnos += 1


def escolher_pokemon(jogador_num):
    print(f"\nJogador {jogador_num}, escolha seu Pokémon:")
    for chave, pokemon in pokemons.items():
        print(f"{chave} - {pokemon.apelido}")
    escolha = None
    while escolha not in pokemons:
        escolha = input("Digite o número do Pokémon escolhido: ")
        if escolha not in pokemons:
            print("Escolha inválida. Tente novamente.")
    # Para cada batalha, cria uma cópia nova para não perder HP original
    p = pokemons[escolha]
    return Pokemon(p.apelido, p.altura, p.peso, p.especie, p.tipagem, p.geracao, p.hp, p.ataque, p.defesa)

def main():
    pokemon_jogador1 = escolher_pokemon(1)
    pokemon_jogador2 = escolher_pokemon(2)
    batalha(pokemon_jogador1, pokemon_jogador2)

if __name__ == "__main__":
    main()
