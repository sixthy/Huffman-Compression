# Huffman Compression Project

Projeto desenvolvido em Python para compressão e descompressão de arquivos de texto utilizando o algoritmo de Huffman.

O objetivo do projeto é demonstrar como funciona a codificação de Huffman, uma técnica de compressão sem perdas que reduz o tamanho dos dados com base na frequência dos caracteres presentes no texto.

---

## Tecnologias utilizadas

- Python
- Estruturas de dados
- Árvore binária
- Algoritmo de Huffman
- Manipulação de arquivos `.txt`
- Manipulação de arquivos binários `.bin`

---

## Funcionalidades

- Leitura de arquivos de texto
- Cálculo da frequência dos caracteres
- Criação da árvore de Huffman
- Geração dos códigos binários para cada caractere
- Compressão de textos para arquivos binários
- Descompressão dos arquivos comprimidos
- Comparação entre arquivos originais e arquivos descomprimidos
- Organização dos arquivos de entrada, comprimidos e descomprimidos

---

## Estrutura principal do projeto

```txt
huffman/
├── main.py
├── README.md
├── Installing.md
├── .gitignore
│
├── Huffman/
│   ├── encode.py
│   ├── decodeHuffman.py
│   └── huffmanTree.py
│
├── Node/
│   └── node.py
│
├── Tree/
│   ├── bodyTree.py
│   └── traverseTree.py
│
├── Input/
│   ├── Text1.txt
│   ├── Text2.txt
│   ├── Text3.txt
│   ├── Text4.txt
│   ├── Text5.txt
│   └── Text6.txt
│
├── Compressed_Files/
│   ├── Text1_encoded.bin
│   ├── Text2_encoded.bin
│   ├── Text3_encoded.bin
│   ├── Text4_encoded.bin
│   ├── Text5_encoded.bin
│   └── Text6_encoded.bin
│
└── Decompressed_Files/
    ├── Text1_decoded.txt
    ├── Text2_decoded.txt
    ├── Text3_decoded.txt
    ├── Text4_decoded.txt
    ├── Text5_decoded.txt
    └── Text6_decoded.txt
```

---

## Como funciona o algoritmo de Huffman

O algoritmo de Huffman é um método de compressão sem perdas.

Ele funciona da seguinte forma:

1. Lê o conteúdo do arquivo de texto.
2. Conta a frequência de cada caractere.
3. Cria nós com base nessas frequências.
4. Monta uma árvore binária de Huffman.
5. Gera códigos binários menores para caracteres mais frequentes.
6. Substitui cada caractere do texto pelo seu código binário.
7. Salva o resultado comprimido em um arquivo `.bin`.
8. Usa a mesma árvore/códigos para reconstruir o texto original na descompressão.

---

## Pré-requisitos

Antes de rodar o projeto, instale:

- Python 3

Verifique se o Python está instalado:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/sixthy/huffman.git
```

Entre na pasta do projeto:

```bash
cd huffman
```

Caso queira usar ambiente virtual, crie um ambiente com:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Ative o ambiente virtual no Linux/Mac:

```bash
source .venv/bin/activate
```

---

## Módulos principais

### main.py

Arquivo principal do projeto.

Responsável por iniciar o processo de compressão e descompressão dos arquivos.

---

### Huffman/encode.py

Responsável pela parte de codificação dos dados.

Transforma o conteúdo do texto original em uma sequência binária baseada nos códigos gerados pela árvore de Huffman.

---

### Huffman/decodeHuffman.py

Responsável pela decodificação dos dados comprimidos.

Reconstrói o texto original a partir do arquivo binário comprimido.

---

### Huffman/huffmanTree.py

Responsável pela criação e organização da árvore de Huffman.

A árvore é construída com base na frequência dos caracteres encontrados no texto.

---

### Node/node.py

Define a estrutura de um nó utilizado na árvore de Huffman.

Cada nó pode representar um caractere, uma frequência e referências para outros nós.

---

### Tree/bodyTree.py

Contém a lógica relacionada ao corpo da árvore de Huffman.

Ajuda na construção e organização dos nós dentro da árvore.

---

### Tree/traverseTree.py

Responsável por percorrer a árvore e gerar os códigos binários de cada caractere.

---

## Exemplo de fluxo

1. O arquivo `Text1.txt` é lido da pasta `Input/`.
2. O programa calcula a frequência de cada caractere.
3. Uma árvore de Huffman é criada.
4. O texto é convertido em códigos binários.
5. O arquivo comprimido é salvo em `Compressed_Files/Text1_encoded.bin`.
6. O arquivo é descomprimido.
7. O resultado é salvo em `Decompressed_Files/Text1_decoded.txt`.
8. O conteúdo descomprimido deve ser equivalente ao texto original.

---

## Benefícios da compressão de Huffman

- Reduz o tamanho de arquivos de texto
- Mantém os dados originais sem perda
- Demonstra uso prático de árvores binárias
- Ajuda a entender algoritmos de compressão
- Trabalha conceitos de frequência, prioridade e codificação

---

## Status 

Projeto funcional para estudo e demonstração do algoritmo de Huffman.

