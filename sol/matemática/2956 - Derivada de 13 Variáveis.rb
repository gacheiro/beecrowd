# 2956 - Derivada de 13 Variáveis
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2956

def main
    b, h = gets.split(' ').map(&:to_f)
    area = (b * h)/2.0
    puts "Concluimos que, dado o limite da entrada, a resposta seria:  y = f(x) = #{'%0.5f' % area}."
  end
  
  main
