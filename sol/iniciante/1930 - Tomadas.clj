; 1930 - Tomadas
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1930

(import java.util.Scanner)

(let [s (Scanner. System/in)
      t1 (.nextInt s)
      t2 (.nextInt s)
      t3 (.nextInt s)
      t4 (.nextInt s)]
  (println (+ t1 t2 t3 t4 -3)))
