; 1045 - Tipos de Triângulos
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

(require '[clojure.string :as str])

(defn triangulo-info [a b c]
  (cond
    (>= a (+ b c)) (println "NAO FORMA TRIANGULO")
    (= (* a a) (+ (* b b) (* c c))) (println "TRIANGULO RETANGULO")
    (> (* a a) (+ (* b b) (* c c))) (println "TRIANGULO OBTUSANGULO")
    (< (* a a) (+ (* b b) (* c c))) (println "TRIANGULO ACUTANGULO"))
  (cond
    (= a b c) (println "TRIANGULO EQUILATERO")
    (or (= a b) (= b c) (= a c)) (println "TRIANGULO ISOSCELES")))

(let [lados (map #(Float/parseFloat %)
                 (str/split (read-line) #" "))
      a-b-c (reverse (sort lados))]
  (apply triangulo-info a-b-c))
