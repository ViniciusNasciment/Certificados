
import openpyxl

from PIL import Image, ImageDraw, ImageFont

workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2,max_row=15)):

    nome_curso =        linha[0].value
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value
    data_inicio =       linha[3].value
    data_final  =       linha[4].value
    carga_horaria  =    linha[5].value
    data_emissao   =    linha[6].value

             # FONTES (LETRAS E NUMEROS)
    fonte_nome  = ImageFont.truetype('./tahomabd.ttf',95)
    fonte_geral = ImageFont.truetype('./tahoma.ttf',85)
    fonte_data  = ImageFont.truetype('./tahoma.ttf',55)

             #IMAGEN DO CERTIFICADO
    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1015,819), nome_participante,fill='black',font=fonte_nome)
    desenhar.text((1055,950), nome_curso,fill='black',font=fonte_geral)
    desenhar.text((1430,1063), tipo_participacao,fill='black',font=fonte_geral)
    desenhar.text((1490, 1182),str(carga_horaria),fill='black',font=fonte_geral)
    
        ## PARTE DE BAIXO DO CERTIFICADO
    desenhar.text((739,1773), data_inicio,fill='black',font=fonte_data)
    desenhar.text((740,1933), data_final,fill='black',font=fonte_data)
    desenhar.text((2217,1933), data_emissao,fill='black',font=fonte_data)

    image.save(f'./{indice} {nome_participante} certificado.png')



