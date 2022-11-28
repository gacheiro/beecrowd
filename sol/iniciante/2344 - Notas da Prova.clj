; 2344 - Notas da Prova
; https://www.urionlinejudge.com.br/judge/pt/problems/view/2344

(let [x (Integer/parseInt (read-line))]
  (println (cond
             (>= x 86) "A"
             (>= x 61) "B"
             (>= x 36) "C"
             (>= x 1)  "D"
             :else     "E")))
