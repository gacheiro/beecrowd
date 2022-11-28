; 1146 - Sequências Crescentes
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1146

(require '[clojure.string :as str])

(loop []
  (let [x (Integer/parseInt (read-line))]
    (when (> x 0)
      (println (str/join " " (range 1 (inc x))))
      (recur))))
