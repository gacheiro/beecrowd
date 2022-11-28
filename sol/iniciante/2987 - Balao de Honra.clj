; 2987 - Balão de Honra
; https://www.urionlinejudge.com.br/judge/pt/problems/view/2987

(def letters "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

(let [l (read-line)]
  (println (inc (.indexOf letters l))))
