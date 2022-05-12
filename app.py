import browser
import report

def main():
    print('Bem vindo ao Finance. O quê você deseja fazer?')
    print('1 - Mostrar relatório')
    print('2 - Adicionar investimento')
    print('3 - Editar investimento')
    print('4 - Deletar investimento')
    option = input('Digite a opção desejada: ')
    handleInput(option)
    return

def showReport():
    report.defaultConfig()
    report.write_html()
    browser.openReport()
    return 

def addInvestment():
    return

def editInvestment():
    return

def deleteInvestment():
    return

def handleInput(option):
    switch = {
        '1': showReport(),
        '2': addInvestment(),
        '3': editInvestment(),
        '4': deleteInvestment(),
    }
    choosen = switch.get(option, 'default')
    if choosen == 'default':
        raise Exception('Erro: insira uma opção disponível')
    return choosen
     

main()

