# 2) Criação da Classe Carro
class Carro:
    # Este é o método construtor. Ele "molda" o objeto quando ele é criado.
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        # O duplo sublinhado (__) torna o atributo PRIVADO
        self.velocidade_instantanea = 500

    # Método PÚBLICO para alterar a velocidade de forma segura
    def acelerar(self, taxa_de_aceleracao):
        self.velocidade_instantanea += taxa_de_aceleracao

    # Método PÚBLICO para conseguirmos ler a velocidade na main
    def get_velocidade(self):
        return self.velocidade_instantanea


# --- INÍCIO DA MAIN ---
if __name__ == "__main__":
    meu_carro = Carro("Fusca", "Branco")

    # 0. Imprime ANTES de acelerar (vai mostrar 500)
    print(f"Velocidade inicial de fábrica: {meu_carro.get_velocidade()} km/h")

    # 1. Usando a forma correta (Pública)
    meu_carro.acelerar(15.5)
    print(f"Velocidade correta: {meu_carro.get_velocidade()} km/h")

    # 2. O TESTE DA PERGUNTA 1: Tentando acessar a variável privada direto
    print("Tentando ler a variável privada diretamente...")
    print(meu_carro.velocidade_instantanea)
