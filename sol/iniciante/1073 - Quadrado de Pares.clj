; 1073 - Quadrado de Pares
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1073

(let [n (Integer/parseInt (read-line))]
  (doseq [x (range 1 (inc n)) :when (even? x)]
    (println (format "%d^2 = %d" x (* x x)))))
