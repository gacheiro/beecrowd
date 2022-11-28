; 1759 - Ho Ho Ho
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1759

(require '[clojure.string :as str])

(let [n (Integer/parseInt (read-line))]
  (println (format "%s!" (str/join " " (take n (repeat "Ho"))))))
