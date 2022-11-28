; 1044 - Múltiplos
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

(require '[clojure.string :as str])

(let [[x y] (map #(Integer/parseInt %)
                 (str/split (read-line) #" "))]
  (if (or (= (mod x y) 0) (= (mod y x) 0))
    (do (println "Sao Multiplos"))
    (do (println "Nao sao Multiplos"))))
