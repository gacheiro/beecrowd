; 1115 - Quadrante
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1115

(import java.util.Scanner)

(def s (Scanner. System/in))

(loop [x (.nextInt s)
       y (.nextInt s)]
  (when (and (not= x 0) (not= y 0))
    (println
      (cond
        (and (> x 0) (> y 0)) "primeiro"
        (and (< x 0) (> y 0)) "segundo"
        (and (< x 0) (< y 0)) "terceiro"
        (and (> x 0) (< y 0)) "quarto"))
    (recur (.nextInt s) (.nextInt s))))