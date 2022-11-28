; 1080 - Maior Posição
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1080

(let [xs (vec (for [i (range 100)]
                (Integer/parseInt (read-line))))
      max-x (apply max xs)]
  (println max-x)
  (println (inc (.indexOf xs max-x))))
