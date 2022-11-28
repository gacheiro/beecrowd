; 1060 - Números Positivos
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

(let [seq (for [_ (range 6)
                :let [x (Float/parseFloat (read-line))]
                :when (> x 0)]
            x)]
  (println (count seq) "valores positivos"))
