; 1037 - Intervalo
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

(def x (Float/parseFloat (read-line)))

(defn get-interval [x]
  (cond
    (and (>= x 0) (<= x 25)) "Intervalo [0,25]"
    (and (> x 25) (<= x 50)) "Intervalo (25,50]"
    (and (> x 50) (<= x 75)) "Intervalo (50,75]"
    (and (> x 75) (<= x 100)) "Intervalo (75,100]"
    :else "Fora de intervalo"))

(println (get-interval x))
