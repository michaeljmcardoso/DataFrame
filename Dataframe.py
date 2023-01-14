import pandas as pd
dados = [
    ['Pyhon',10, 'verde', 'Brasil'],
    ['Java', 7.5, 'azul', 'China'],
    ['PHP', -1, 'branco', 'Corea'],
    ['JavaScript', 9.5, 'cinza', 'Japão']
]
df = pd.DataFrame(dados, columns=['Linguagem', 'Nota', 'Cor', 'País'])
print(df)
print(df.shape)
