class Farmacia:
    def __init__(self):
        self.estoque = {}  # Dicionário para armazenar medicamentos e suas quantidades

    def adicionar_medicamento(self, nome, quantidade, preco):
        """Adiciona um medicamento ao estoque ou atualiza a quantidade existente"""
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")

    def remover_medicamento(self, nome, quantidade):
        """Remove um medicamento do estoque"""
        if nome in self.estoque and self.estoque[nome]['quantidade'] >= quantidade:
            self.estoque[nome]['quantidade'] -= quantidade
            print(f"{quantidade} unidades de {nome} removidas do estoque.")
        else:
            print("Quantidade insuficiente no estoque ou medicamento não encontrado.")

    def registrar_venda(self, nome, quantidade):
        """Registra a venda de um medicamento e atualiza o estoque"""
        if nome in self.estoque and self.estoque[nome]['quantidade'] >= quantidade:
            self.estoque[nome]['quantidade'] -= quantidade
            total = self.estoque[nome]['preco'] * quantidade
            print(f"Venda registrada: {quantidade} unidades de {nome} por R${total:.2f}")
        else:
            print("Quantidade insuficiente para a venda ou medicamento não encontrado.")

    def exibir_estoque(self):
        """Exibe o estoque atual"""
        if not self.estoque:
            print("Estoque vazio.")
        else:
            print("Estoque atual:")
            for nome, info in self.estoque.items():
                print(f"{nome}: {info['quantidade']} unidades - R${info['preco']:.2f} cada")

# Exemplo de uso
farmacia = Farmacia()

# Adicionar medicamentos ao estoque
farmacia.adicionar_medicamento("Paracetamol", 100, 5.50)
farmacia.adicionar_medicamento("Ibuprofeno", 50, 8.30)

# Exibir o estoque
farmacia.exibir_estoque()

# Registrar uma venda
farmacia.registrar_venda("Paracetamol", 2)

# Exibir o estoque após a venda
farmacia.exibir_estoque()

# Remover medicamentos do estoque
farmacia.remover_medicamento("Ibuprofeno", 10)

# Exibir o estoque após a remoção
farmacia.exibir_estoque()
