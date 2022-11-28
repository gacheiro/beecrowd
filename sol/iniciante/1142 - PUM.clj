; 1142 - PUM
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1142

(let [n (Integer/parseInt (read-line))]
  (loop [i n
         x 1]
    (when (> i 0)
      (println x (+ x 1) (+ x 2) "PUM")
      (recur (dec i) (+ x 4)))))
