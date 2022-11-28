; 1040 - Média 3
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

(import java.util.Scanner)

(let [s (Scanner. System/in)
      n1 (.nextFloat s)
      n2 (.nextFloat s)
      n3 (.nextFloat s)
      n4 (.nextFloat s)
      media (/ (+ (* n1 2) (* n2 3) (* n3 4) n4) 10)]
  (println (format "Media: %.1f" media))
  (cond
    (>= media 7) (println "Aluno aprovado.")
    (< media 5)  (println "Aluno reprovado."))
  (when (and (>= media 5) (< media 7))
    (println "Aluno em exame.")
    (let [n5 (.nextFloat s)
          media-final (/ (+ media n5) 2)]
      (cond
        (>= media-final 5) (println "Aluno aprovado.")
        :else              (println "Aluno reprovado"))
      (println (format "Media final: %.1f" media-final)))))
