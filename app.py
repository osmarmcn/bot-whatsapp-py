from openpyxl import*

workbook = load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']


for linha in pagina_clientes.iter_rows(min_row=2): 
    nome = linha[0].value
    telefone = linha[1].value
    pagamento = linha[2].value
    # https://web.whatsapp.com/send?phone={numero especifico}&text={mensagem especifica}
    #print(nome, telefone, pagamento)
















''''
iter_rows() - é uma função do openpyxl que vai passar por todas as linhas da lista.
obs: o parâmetro min_row=2 indica que vai começar na linha dois, tem que vericar na lista onde realmente começa a lista pdoendo ser uma linha diferente.




'''