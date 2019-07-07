# 1062 - Trilhos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1062

def possible?(n, ordem)
  # Essa função modifica o array :(
  pilha = []
  (1..n).each do |i| 
    pilha << i
    while !pilha.empty? && (pilha.last == ordem.first)
      pilha.pop   # remove o último
      ordem.shift # remove o primeiro
    end
  end
  pilha.empty?
end

def main
  loop do
    n = gets.to_i
    return if n.zero?
    loop do
      linha = gets.chomp
      break if linha == "0"
      ordem = linha.split(" ").map(&:to_i)
      puts possible?(n, ordem) ? "Yes" : "No"
    end
    puts ""
  end
end

main
