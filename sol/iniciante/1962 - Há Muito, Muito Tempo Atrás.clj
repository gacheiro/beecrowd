; 1962 - Há Muito, Muito Tempo Atrás
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1962

(import java.util.Scanner)

(let [s (Scanner. System/in)
      n (.nextInt s)]
  (dotimes [_ n]
    (let [x (.nextInt s)
          y (- 2015 x)]
      (cond
        (<= y 0) (println (Math/abs (dec y)) "A.C.")
        :else    (println y "D.C.")))))
