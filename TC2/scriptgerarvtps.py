import pyautogui
import time
 
def texto(): 
    for i in range(1,6):
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.write(' ' + str(i) + ', ')
        #pyautogui.write(str(i) + ', ')
 
def main():
    time.sleep(3)
    texto()
 
main()


"""
Maquina Geral = (SigmaG, Q, δ, Base, F)
SigmaG = {
          Manutenção, Identidade Válida, Identidade Inválida, Voltar, 
          1, 2, 3, 4, 5, Reposição, Repor 1, Repor Tudo, Comprar, Cartão, Dinheiro
          Reposto 1 1, Reposto 1 2, Reposto 1 3, Reposto 1 4, Reposto 1 5, 
          Reposto Tudo 1, Reposto Tudo 2, Reposto Tudo 3, Reposto Tudo 4, Reposto Tudo 5, 
          Sem Estoque 1, Sem Estoque 2, Sem Estoque 3, Sem Estoque 4, Sem Estoque 5, 
          Com Estoque 1, Com Estoque 2, Com Estoque 3, Com Estoque 4, Com Estoque 5, 
          Falha 1, Falha 2, Falha 3, Falha 4, Falha 5, 
          Aceito 1, Aceito 2, Aceito 3, Aceito 4, Aceito 5
          }
Q = {
     Base, Manutenção Verificação, Manutenção, Reposição Verificação, Reposição, Venda,
     Reposição Item 1, Reposição Item 2, Reposição Item 3, Reposição Item 4, Reposição Item 5,
     Reposto 1 Item 1, Reposto 1 Item 2, Reposto 1 Item 3, Reposto 1 Item 4, Reposto 1 Item 5, 
     Reposto Tudo Item 1, Reposto Tudo Item 2, Reposto Tudo Item 3, Reposto Tudo Item 4, Reposto Tudo Item 5,
     Venda Item 1, Venda Item 2, Venda Item 3, Venda Item 4, Venda Item 5, 
     Método Pagamento 1, Método Pagamento 2, Método Pagamento 3, Método Pagamento 4, Método Pagamento 5, 
     Verificação Pagamento 1, Verificação Pagamento 2, Verificação Pagamento 3, Verificação Pagamento 4, Verificação Pagamento 5
     }
     
δ = {
     Q x SigmaG > Q x ∆*,
     Base x Manutenção > Manutenção Verificação x [Verificar Identificação]
     Manutenção Verificação x Identidade Inválida > Base x "Id inválida, tente novamente"
     Manutenção Verificação x Identidade Válida > Manutenção x "Maquina desabilitada para manutenção"
     }

F = {}

∆ = {
     
     }
"""
