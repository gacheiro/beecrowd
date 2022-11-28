; 1866 - Conta
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1866

(import java.util.Scanner)

(let [s (Scanner. System/in)
      n (.nextInt s)]
  (dotimes [_ n]
    (let [x (.nextInt s)]
      (cond
        (odd? x) (println 1)
        :else    (println 0)))))
