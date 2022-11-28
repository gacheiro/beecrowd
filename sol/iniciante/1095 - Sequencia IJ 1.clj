; 1095 - Sequencia IJ 1
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1095

(loop [i 1
       j 60]
  (println (format "I=%d J=%d" i j))
  (when (> j 0)
    (recur (+ i 3) (- j 5))))
