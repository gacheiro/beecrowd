# 2866 - Criptotexto
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2866

def main
    n = gets.to_i
    n.times do 
        msg = gets.chomp
        decoded = msg
                  .reverse
                  .split('')
                  .select{ |c| c == c.downcase } # poxa, ruby não tem um  `str.lower?` :(
                  .join
        puts decoded
    end
end

main
