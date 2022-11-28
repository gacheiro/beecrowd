; 1059 - Números Pares
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1059

(require '[clojure.string :as str])

(defn get-pares [n]
  (for [x (range 1 n) :when (even? x)]
    x))

(println (str/join "\n" (get-pares 101)))
