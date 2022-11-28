; 1074 - Par ou Ímpar
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1074

(let [n (Integer/parseInt (read-line))]
  (dotimes [_ n]
    (let [x (Integer/parseInt (read-line))]
      (cond
        (= 0 x)   ()
        (even? x) (print "EVEN ")
        :else     (print "ODD "))
      (cond
        (= x 0) (println "NULL")
        (> x 0) (println "POSITIVE")
        (< x 0) (println "NEGATIVE")))))
