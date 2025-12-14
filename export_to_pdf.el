;; Emacs Lisp script to export org file to PDF
(require 'org)
(require 'ox-latex)

;; Set up LaTeX export with XeLaTeX
(setq org-latex-compiler "xelatex")
(setq org-latex-pdf-process
      '("xelatex -interaction nonstopmode -output-directory %o %f"
        "xelatex -interaction nonstopmode -output-directory %o %f"
        "xelatex -interaction nonstopmode -output-directory %o %f"))

;; Find and open the org file
(find-file "situational_gita_book.org")

;; Export to PDF
(org-latex-export-to-pdf)

;; Exit Emacs
(kill-emacs 0)
