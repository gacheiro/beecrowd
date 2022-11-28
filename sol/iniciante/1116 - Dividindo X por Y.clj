; 1116 - Dividindo X por Y
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1116

(import java.util.Scanner)

(let [s (Scanner. System/in)
      n (.nextInt s)]
  (dotimes [_ n]
    (let [x (.nextInt s)
          y (.nextInt s)]
      (println (if (= y 0)
                 "divisao impossivel"
                 (format "%.1f" (float (/ x y))))))))
