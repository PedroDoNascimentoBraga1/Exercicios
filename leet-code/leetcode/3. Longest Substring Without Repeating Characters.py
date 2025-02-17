class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Encontra o comprimento da maior substring sem caracteres repetidos."""

        def comparar(string, comparativo):
            return comparativo not in string  # Verifica diretamente se o caractere está na string

        guardar = []  # Lista temporária para armazenar a substring atual
        maior = []  # Lista que armazena a maior substring encontrada

        for char in s:
            if comparar(guardar, char):
                guardar.append(char)
            else:
                if len(guardar) > len(maior):
                    maior = list(guardar)  # Faz uma cópia da lista
                while char in guardar:  # Remove os elementos até eliminar o duplicado
                    guardar.pop(0)
                guardar.append(char)

        if len(guardar) > len(maior):  # Confirmação final
            maior = list(guardar)

        return len(maior)
