; 1020 - Idade em Dias
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

(def days (Integer/parseInt (read-line)))

(defn print-age! [days]
  (let [y (int (/ days 365))
        m (int (/ (- days (* y 365)) 30))
        d (mod (- days (* m 30)) 365)]
    (println y "ano(s)")
    (println m "mes(es)")
    (println d "dia(s)")))

(print-age! days)
