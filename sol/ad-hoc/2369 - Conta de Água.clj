; 2369 - Conta de Água
; https://www.urionlinejudge.com.br/judge/pt/problems/view/2369

(defn a-pagar [consumo]
  (loop [x 0
         c consumo]
    (if (>= c 0)
      (cond
        (<= c 10)  (recur (+ x 7) -1)
        (<= c 30)  (recur (+ x (- c 10)) 10)
        (<= c 100) (recur (+ x (* (- c 30) 2)) 30)
        :else      (recur (+ x (* (- c 100) 5)) 100))
      x)))

(let [consumo (Integer/parseInt (read-line))]
  (println (a-pagar consumo)))