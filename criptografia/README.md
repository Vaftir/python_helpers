## Visão Geral

A classe **Criptografia** implementa um esquema simples de cifra linear para transformar texto em uma sequência hexadecidual e vice‑versa, usando parâmetros $c\_a$ e $c\_b$ como coeficientes da transformação.

* **Cifra (encriptar)**:

  $$
    \text{valor\_encriptado} = (\text{ord}(caractere) \times c_a) + c_b
  $$

  O resultado é formatado em 6 dígitos hexadecimais concatenados.
* **Decifra (desencriptar)**:

  $$
    \text{valor\_original} = \frac{(\text{hex\_para\_int} - c_b)}{c_a}
  $$

  Cada bloco de 6 caracteres hex é revertido ao caractere original.

---

## Estrutura do Projeto

```
.
├── modules/
│   └── criptografia/
│       └── Criptografia.py    # Classe de encriptação e desencriptação
└── README.md                  # Este arquivo
```

---

## Dependências

* Python 3.6+
* Biblioteca padrão: nenhuma dependência externa

---

## Configuração dos Coeficientes

Antes de usar, defina valores inteiros para `self.c_a` e `self.c_b` no construtor. Por exemplo:

```python
self.c_a = 3
self.c_b = 5
```

Esses valores controlam a multiplicação e o deslocamento na fórmula de encriptação.

---

## Uso

```python
from modules.criptografia.Criptografia import Criptografia

# Instancia e configura coeficientes
crypto = Criptografia()
crypto.c_a = 3
crypto.c_b = 5

texto_original = "Olá, Mundo!"
# Encriptar
texto_encriptado = crypto.encriptar(texto_original)
print("Encriptado:", texto_encriptado)
# → por exemplo: 0001dd0001e600001e10001e0e001e250001e26...

# Desencriptar
texto_desencriptado = crypto.desencriptar(texto_encriptado)
print("Desencriptado:", texto_desencriptado)
# → "Olá, Mundo!"
```

---

## Métodos

### `encriptar(s_textoEncriptar: str) → str`

* Itera cada caractere da string.
* Converte para código Unicode (`ord`).
* Aplica a fórmula linear e formata em hexadecimal de 6 dígitos.
* Retorna a concatenação de todos os blocos hex.

### `desencriptar(s_textoDesencriptar: str) → str`

* Lê a string de 6 em 6 caracteres (hex).
* Converte cada bloco de hex em inteiro.
* Reverte a fórmula para obter o código Unicode original.
* Concatena e retorna a string decifrada.

---

## Observações e Boas Práticas

* **Valores de Coeficientes**: Escolha $c_a$ e $c_b$ de forma que $c_a\neq0$ e que não causem overflow além do representável em 6 dígitos hexadecimais.
* **Segurança**: Este método é educacional e **não** fornece segurança criptográfica real. Para aplicações de produção, utilize bibliotecas padrão como `cryptography`.
* **Formato Fixo**: O uso fixo de 6 dígitos hex por caractere simplifica o parsing, mas aumenta o tamanho da saída.

---

## Licença

MIT License — sinta-se à vontade para adaptar e aprimorar conforme necessário.
