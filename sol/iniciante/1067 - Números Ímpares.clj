; 1067 - Números Ímpares
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1067

(require '[clojure.string :as str])

(defn impares [n]
  (for [x (range (+ n 1)) :when (odd? x)]
    x))

(let [n (Integer/parseInt (read-line))]
  (println (str/join "\n" (impares n))))
