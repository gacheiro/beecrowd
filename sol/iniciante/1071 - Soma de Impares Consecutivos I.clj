; 1071 - Soma de Impares Consecutivos I
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1071

(defn seq-de-impares [x, y]
  (for [i (range x y) :when (odd? i)]
    i))

(let [x (Integer/parseInt (read-line))
      y (Integer/parseInt (read-line))
      a (min x y)
      b (max x y)]
  ; imprime a soma dos numeros impares no intervalo (a, b)
  (println (apply + (seq-de-impares (inc a) b))))
