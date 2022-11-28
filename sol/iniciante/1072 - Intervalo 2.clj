; 1072 - Intervalo 2
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1072

(defn inside? [x]
  (and (>= x 10) (<= x 20)))

(let [n (Integer/parseInt (read-line))
      numbers (for [_ (range n)]
                (Integer/parseInt (read-line)))
      inside (count (filter inside? numbers))
      outside (- n inside)]
  (println (format "%d in\n%d out" inside outside)))
