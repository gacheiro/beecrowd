# 1129 - Leitura Ótica
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1129

def main
    loop do
        n = gets.to_i
        return if n.zero?

        n.times do
            alternativas = gets.split(" ").map do |x|
                if x.to_i <= 127
                    :preto
                else
                    :branco
                end
            end

            if alternativas.count(:preto) == 1
                index = alternativas.find_index(:preto)
                puts "ABCDE"[index]
            else
                puts "*"
            end
        end
    end
end

main
