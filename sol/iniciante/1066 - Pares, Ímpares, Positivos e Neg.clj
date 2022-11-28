; 1066 - Pares, Ímpares, Positivos e Negativos
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1066

(let [xs (for [_ (range 5)]
           (Integer/parseInt (read-line)))]
  (println (count (filter even? xs)) "valor(es) par(es)")
  (println (count (filter odd? xs)) "valor(es) impar(es)")
  (println (count (filter #(> % 0) xs)) "valor(es) positivo(s)")
  (println (count (filter #(< % 0) xs)) "valor(es) negativo(s)"))
