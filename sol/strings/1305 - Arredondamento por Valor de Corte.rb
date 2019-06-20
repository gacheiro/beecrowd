# 1305 - Arredondamento por Valor de Corte
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1305

def main
    loop do
        num = gets
        cutoff = gets
        return if num.nil?

        fnum = num.to_f
        fcutoff = cutoff.to_f

        if fnum % 1 > fcutoff
            puts fnum.ceil
        else
            puts fnum.floor
        end
    end
end

main
