# 1548 - Fila do Recreio
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1548

def notas_iguais(notas_a, notas_b)
    'Retorna o número de notas iguais com o mesmo índice.'
    notas_a.zip(notas_b).count { |a, b| a == b }
end

def notas_iguais2(notas_a, notas_b)
    'Retorna o número de notas iguais com o mesmo índice.
    Essa versão é mais rápida, mas eu não gostei muito.'
    n = notas_a
      .zip(notas_b)
      .map { |a, b| a == b ? 1 : 0 }
      .reduce(:+)
end

def main
    n = gets.to_i
    n.times do
        _ = gets.to_i
        notas = gets.split(' ').map(&:to_i)
        puts(notas_iguais(notas, notas.sort.reverse))
    end
end
  
main
