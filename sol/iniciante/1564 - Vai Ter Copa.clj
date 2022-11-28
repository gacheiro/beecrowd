; 1564 - Vai Ter Copa?
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1564

(import java.util.Scanner)

(let [s (Scanner. System/in)]
  (loop []
    (when (.hasNextInt s)
      (if (= 0 (.nextInt s))
        (println "vai ter copa!")
        (println "vai ter duas!"))
      (recur))))
