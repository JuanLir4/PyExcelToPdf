# Conversor de XLSX para PDF

Este script em Python converte vários arquivos XLSX para um único arquivo PDF sem a necessidade de ter o Excel instalado na máquina. Por favor, esteja ciente de que, devido à natureza do processo de conversão, o layout e as medidas no PDF resultante podem não ser extremamente precisos.

## Instruções:

1. Coloque os arquivos XLSX que deseja converter na pasta 'docs'.
2. Execute o script.

```bash
python nome_do_seu_script.py
```

3. O PDF de saída será gerado como "output.pdf" no mesmo diretório do seu script.

## Dependências:

- pandas
- os
- reportlab

Instale as dependências usando:

```bash
pip install pandas os reportlab
```

## Notas Importantes:

- Certifique-se de que seus arquivos XLSX estão na pasta 'docs'.
- O script utiliza a biblioteca `pandas` para ler e concatenar os arquivos XLSX.
- A biblioteca `reportlab` é utilizada para criar o PDF e adicionar conteúdo.

## Aviso Legal:

- O layout do PDF pode não ser preciso devido à ausência do Excel para medidas exatas.

Sinta-se à vontade para personalizar o script de acordo com seus requisitos específicos. Se encontrar algum problema, consulte a documentação das bibliotecas utilizadas ou busque assistência na comunidade.

**Feliz programação!**
