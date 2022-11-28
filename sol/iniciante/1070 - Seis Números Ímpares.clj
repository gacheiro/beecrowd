; 1070 - Seis Números Ímpares
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1070

(require '[clojure.string :as str])

(defn impares [n]
  (take 6 (for [x (drop n (range)) :when (odd? x)]
            x)))

(let [n (Integer/parseInt (read-line))]
  (println (str/join "\n" (impares n))))
