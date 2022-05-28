
import browser
import report
import helpers

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
    """
    Triggers report writing and show report using browser.
    """
    report.defaultConfig()
    report.write_html()
    browser.openReport()
    return 

def addInvestment():
    investment_types = helpers.get_investment_types()
    print('Escolha um tipo de investimento: ')
    for typ in investment_types:
        print(f'{typ}')
    user_invest_type = input()
    labels = helpers.get_investment_label(user_invest_type)
    user_inputs = []
    for label in labels:
        user_inputs.append(input(f'{label}: '))
    helpers.insertInDb(user_invest_type, user_inputs)
    return


def editInvestment():
    investment_types = helpers.get_investment_types()
    print('Que tipo de investimento você gostaria de editar?')

    for typ in investment_types:
        print(f'{typ}')

    user_invest_type = input()
    investment_list = helpers.retrieve_investment(user_invest_type)
    print(investment_list)
    print('Qual investimento você gostaria de editar? (começando do 1)')
    invest_index = int(input()) - 1
    choosen_investment = investment_list[invest_index]
    print(choosen_investment)
    print('Qual dado você gostaria de alterar? (começando do 1)')
    edit_index = int(input()) - 1
    print(f'O que você gostaria de colocar no lugar do dado selecionado? Dado selecionado: {choosen_investment[edit_index]}')
    new_value = input()
    labels = helpers.get_investment_label(user_invest_type)
    helpers.updateAtTable(table=user_invest_type, column=labels[edit_index], old_value=choosen_investment[edit_index], new_value=new_value)

    return

def deleteInvestment():
    investment_types = helpers.get_investment_types()
    print('Que tipo de investimento você gostaria de deletar?')

    for typ in investment_types:
        print(f'{typ}')

    user_invest_type = input()
    investment_list = helpers.retrieve_investment(user_invest_type)
    print(investment_list)
    print('Qual investimento você gostaria de deletar? (começando do 1)')
    delete_invest_index = int(input()) - 1
    investment = investment_list[delete_invest_index][0]

    helpers.deleteAtIndexDb(user_invest_type, investment)
    return

def handleInput(option):
    if option == '1':
        showReport()
    elif option == '2':
        addInvestment()
    elif option == '3':
        editInvestment()
    elif option == '4':
        deleteInvestment()
    else:
        raise Exception('Erro: insira uma opção disponível')
    return 
     

main()


#TODO FIX VALIDATION OF CASES (STRING NOT PASSING EDIT, EQUAL VALUES GOING WRONG ON INSERT QUERY)