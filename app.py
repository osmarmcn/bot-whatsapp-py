from openpyxl import*

workbook = load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']


for linha in pagina_clientes.iter_rows(min_row=2): 
    nome = linha[0].value
    telefone = linha[1].value
    pagamento = linha[2].value
    # https://web.whatsapp.com/send?phone={numero especifico}&text={mensagem especifica}
    #print(nome, telefone, pagamento)



