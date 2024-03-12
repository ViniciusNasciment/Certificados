# Certificados script para geração de certificados

Este commit adiciona um script em Python para gerar certificados a partir de dados contidos em uma planilha Excel. O script utiliza as bibliotecas openpyxl e PIL (Pillow) para carregar informações dos alunos a partir da planilha 'planilha_alunos.xlsx' e criar certificados individuais com base em um modelo padrão ('certificado_padrao.jpg').

# Detalhes das alterações:
- Iteração sobre as linhas da planilha para obter informações dos alunos.
- Utilização de diferentes fontes para nome, informações gerais e datas nos certificados.
- Inclusão da data de início, data final, carga horária e data de emissão nos certificados.
- Salvamento dos certificados com nomes únicos no formato 'Índice Nome certificado.png'.

Este script simplifica o processo de geração de certificados, tornando-o mais eficiente e personalizado para cada aluno.

# Caminhos dos arquivos utilizados:
- 'planilha_alunos.xlsx': Planilha contendo informações dos alunos.
- 'certificado_padrao.jpg': Modelo padrão de certificado.
- 'tahomabd.ttf', 'tahoma.ttf': Fontes utilizadas no certificado.




