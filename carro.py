# Importamos a biblioteca de tempo no topo do código
import time

# 2) Criação da Classe Carro
class Carro:
    # Este é o método construtor. Ele "molda" o objeto quando ele é criado.
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        # O duplo sublinhado (__) torna o atributo PRIVADO
        self.velocidade_instantanea = 0.0

    # Método PÚBLICO para alterar a velocidade de forma segura
    def acelerar(self, taxa_de_aceleracao):
        self.velocidade_instantanea += taxa_de_aceleracao

    # Método PÚBLICO para conseguirmos ler a velocidade na main
    def get_velocidade(self):
        return self.velocidade_instantanea


# --- INÍCIO DA MAIN ---
if __name__ == "__main__":
    meu_carro = Carro("Fusca", "Preto")

    print(f"Carro ligado. Velocidade inicial: {meu_carro.get_velocidade()} km/h")
    print("Iniciando a rampa de aceleração...\n")

    # Criamos um loop que vai se repetir 5 vezes
    for instante in range(5):
        # 1. Chamamos o método para somar 15.5 na velocidade atual
        meu_carro.acelerar(15.5)
        
        # 2. Imprimimos o resultado na tela
        print(f"Segundo {instante + 1}: Velocidade = {meu_carro.get_velocidade()} km/h")
        
        # 3. Pausamos o programa por 1 segundo antes do próximo ciclo
        time.sleep(1)

    print("\nTeste de aceleração finalizado!")