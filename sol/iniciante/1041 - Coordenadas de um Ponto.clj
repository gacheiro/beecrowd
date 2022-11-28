; 1041 - Coordenadas de um Ponto
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

(require '[clojure.string :as str])

(defn get-quadrante [x y]
  (cond
    (and (= x 0.0) (= y 0.0)) "Origem"
    (and (> x 0) (> y 0)) "Q1"
    (and (< x 0) (> y 0)) "Q2"
    (and (< x 0) (< y 0)) "Q3"
    (and (> x 0) (< y 0)) "Q4"
    (= y 0.0) "Eixo X"
    (= x 0.0) "Eixo Y"))

(let [[x y] (map #(Float/parseFloat %)
                  (str/split (read-line) #" "))]
  (println (get-quadrante x y)))
