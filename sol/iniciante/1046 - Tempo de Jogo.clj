; 1046 - Tempo de Jogo
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

(require '[clojure.string :as str])

(defn duracao [a b]
  (if (< a b) 
    (- b a)
    (- (+ b 24) a)))

(let [input (map #(Integer/parseInt %)
                 (str/split (read-line) #" "))]
  (println (format "O JOGO DUROU %d HORA(S)" (apply duracao input))))
