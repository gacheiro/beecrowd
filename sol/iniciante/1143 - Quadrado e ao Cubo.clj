; 1143 - Quadrado e ao Cubo
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1143

(let [n (Integer/parseInt (read-line))]
  (doseq [i (range 1 (inc n))]
    (println (format "%d %.0f %.0f" i (Math/pow i 2) (Math/pow i 3)))))
