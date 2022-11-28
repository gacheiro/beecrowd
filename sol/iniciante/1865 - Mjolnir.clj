; 1865 - Mjolnir
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1865

(require '[clojure.string :as str])

(let [n (Integer/parseInt (read-line))]
  (dotimes [_ n]
    (println
      (if (str/starts-with? (read-line) "Thor ")
        "Y"
        "N"))))
