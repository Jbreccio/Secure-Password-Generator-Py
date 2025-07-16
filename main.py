#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de Senhas Seguras
Autor:  Breccio, Jose Roberto
Data: 2025
Descrição: Gera senhas seguras com critérios personalizáveis
"""

import secrets
import string
import random
import os

class GeradorSenhas:
    def __init__(self):
        self.maiusculas = string.ascii_uppercase
        self.minusculas = string.ascii_lowercase
        self.numeros = string.digits
        self.simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.caracteres_ambiguos = "0O1Il"
        
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_titulo(self):
        """Exibe o título do programa"""
        print("=" * 40)
        print("🔐 GERADOR DE SENHAS SEGURAS")
        print("=" * 40)
    
    def obter_tamanho_senha(self):
        """Obtém o tamanho desejado da senha"""
        while True:
            try:
                tamanho = int(input("Tamanho da senha (8-128): "))
                if 8 <= tamanho <= 128:
                    return tamanho
                else:
                    print("❌ Tamanho deve estar entre 8 e 128 caracteres!")
            except ValueError:
                print("❌ Por favor, digite um número válido!")
    
    def obter_opcoes(self):
        """Obtém as opções de tipos de caracteres"""
        opcoes = {}
        
        print("\n📋 Configurações da senha:")
        opcoes['maiusculas'] = self.perguntar_sim_nao("Incluir maiúsculas (A-Z)?")
        opcoes['minusculas'] = self.perguntar_sim_nao("Incluir minúsculas (a-z)?")
        opcoes['numeros'] = self.perguntar_sim_nao("Incluir números (0-9)?")
        opcoes['simbolos'] = self.perguntar_sim_nao("Incluir símbolos (!@#$%...)?")
        opcoes['excluir_ambiguos'] = self.perguntar_sim_nao("Excluir caracteres ambíguos (0,O,1,I,l)?")
        
        # Verificar se pelo menos uma opção foi selecionada
        if not any([opcoes['maiusculas'], opcoes['minusculas'], opcoes['numeros'], opcoes['simbolos']]):
            print("❌ Você deve selecionar pelo menos um tipo de caractere!")
            return self.obter_opcoes()
        
        return opcoes
    
    def perguntar_sim_nao(self, pergunta):
        """Faz uma pergunta sim/não"""
        while True:
            resposta = input(f"{pergunta} (s/n): ").lower().strip()
            if resposta in ['s', 'sim', 'y', 'yes']:
                return True
            elif resposta in ['n', 'não', 'nao', 'no']:
                return False
            else:
                print("❌ Resposta inválida! Digite 's' para sim ou 'n' para não.")
    
    def obter_quantidade_senhas(self):
        """Obtém a quantidade de senhas a gerar"""
        while True:
            try:
                quantidade = int(input("Quantas senhas gerar? (1-10): "))
                if 1 <= quantidade <= 10:
                    return quantidade
                else:
                    print("❌ Quantidade deve estar entre 1 e 10!")
            except ValueError:
                print("❌ Por favor, digite um número válido!")
    
    def construir_conjunto_caracteres(self, opcoes):
        """Constrói o conjunto de caracteres baseado nas opções"""
        caracteres = ""
        
        if opcoes['maiusculas']:
            caracteres += self.maiusculas
        if opcoes['minusculas']:
            caracteres += self.minusculas
        if opcoes['numeros']:
            caracteres += self.numeros
        if opcoes['simbolos']:
            caracteres += self.simbolos
        
        # Remover caracteres ambíguos se solicitado
        if opcoes['excluir_ambiguos']:
            caracteres = ''.join(c for c in caracteres if c not in self.caracteres_ambiguos)
        
        return caracteres
    
    def gerar_senha(self, tamanho, opcoes):
        """Gera uma senha com os critérios especificados"""
        caracteres = self.construir_conjunto_caracteres(opcoes)
        
        # Garantir que a senha tenha pelo menos um caractere de cada tipo selecionado
        senha = []
        
        # Adicionar pelo menos um caractere de cada tipo selecionado
        if opcoes['maiusculas']:
            chars_maiusc = self.maiusculas
            if opcoes['excluir_ambiguos']:
                chars_maiusc = ''.join(c for c in chars_maiusc if c not in self.caracteres_ambiguos)
            senha.append(secrets.choice(chars_maiusc))
        
        if opcoes['minusculas']:
            chars_minusc = self.minusculas
            if opcoes['excluir_ambiguos']:
                chars_minusc = ''.join(c for c in chars_minusc if c not in self.caracteres_ambiguos)
            senha.append(secrets.choice(chars_minusc))
        
        if opcoes['numeros']:
            chars_num = self.numeros
            if opcoes['excluir_ambiguos']:
                chars_num = ''.join(c for c in chars_num if c not in self.caracteres_ambiguos)
            senha.append(secrets.choice(chars_num))
        
        if opcoes['simbolos']:
            senha.append(secrets.choice(self.simbolos))
        
        # Preencher o restante da senha
        while len(senha) < tamanho:
            senha.append(secrets.choice(caracteres))
        
        # Embaralhar a senha
        random.shuffle(senha)
        
        return ''.join(senha)
    
    def analisar_forca_senha(self, senha):
        """Analisa a força da senha"""
        pontos = 0
        
        # Critérios de pontuação
        if len(senha) >= 8:
            pontos += 1
        if len(senha) >= 12:
            pontos += 1
        if len(senha) >= 16:
            pontos += 1
        
        if any(c.isupper() for c in senha):
            pontos += 1
        if any(c.islower() for c in senha):
            pontos += 1
        if any(c.isdigit() for c in senha):
            pontos += 1
        if any(c in self.simbolos for c in senha):
            pontos += 1
        
        # Classificação
        if pontos <= 3:
            return "🔴 Fraca"
        elif pontos <= 5:
            return "🟡 Média"
        else:
            return "🟢 Forte"
    
    def mostrar_senhas_geradas(self, senhas):
        """Exibe as senhas geradas"""
        print(f"\n🔐 Senhas geradas:")
        print("-" * 50)
        
        for i, senha in enumerate(senhas, 1):
            forca = self.analisar_forca_senha(senha)
            print(f"{i}. {senha} (Força: {forca})")
    
    def mostrar_dicas_seguranca(self):
        """Exibe dicas de segurança"""
        print(f"\n💡 Dicas de Segurança:")
        print("• Nunca reutilize senhas importantes")
        print("• Use um gerenciador de senhas")
        print("• Ative autenticação de dois fatores")
        print("• Troque senhas regularmente")
        print("• Não compartilhe suas senhas")
    
    def salvar_senhas(self, senhas):
        """Pergunta se quer salvar as senhas em arquivo"""
        salvar = self.perguntar_sim_nao("\n💾 Deseja salvar as senhas em um arquivo?")
        
        if salvar:
            try:
                with open('senhas_geradas.txt', 'w', encoding='utf-8') as arquivo:
                    arquivo.write("🔐 SENHAS GERADAS\n")
                    arquivo.write("=" * 30 + "\n\n")
                    
                    for i, senha in enumerate(senhas, 1):
                        forca = self.analisar_forca_senha(senha)
                        arquivo.write(f"{i}. {senha} (Força: {forca})\n")
                    
                    arquivo.write(f"\nGerado em: {self.obter_data_atual()}\n")
                
                print("✅ Senhas salvas em 'senhas_geradas.txt'")
                print("⚠️  Lembre-se de excluir o arquivo após usar as senhas!")
                
            except Exception as e:
                print(f"❌ Erro ao salvar arquivo: {e}")
    
    def obter_data_atual(self):
        """Obtém a data atual formatada"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def executar(self):
        """Executa o gerador de senhas"""
        print("🎉 Bem-vindo ao Gerador de Senhas Seguras!")
        
        while True:
            self.limpar_tela()
            self.mostrar_titulo()
            
            # Obter configurações
            tamanho = self.obter_tamanho_senha()
            opcoes = self.obter_opcoes()
            quantidade = self.obter_quantidade_senhas()
            
            # Gerar senhas
            print("\n⏳ Gerando senhas seguras...")
            senhas = []
            
            for _ in range(quantidade):
                senha = self.gerar_senha(tamanho, opcoes)
                senhas.append(senha)
            
            # Mostrar resultados
            self.mostrar_senhas_geradas(senhas)
            self.mostrar_dicas_seguranca()
            
            # Opção de salvar
            self.salvar_senhas(senhas)
            
            # Perguntar se quer gerar mais senhas
            if not self.perguntar_sim_nao("\n🔄 Deseja gerar mais senhas?"):
                break
        
        print("\n👋 Obrigado por usar o Gerador de Senhas! Mantenha suas senhas seguras!")

def main():
    """Função principal"""
    gerador = GeradorSenhas()
    gerador.executar()

if __name__ == "__main__":
    main()
