MAIN = presentation
XELATEX = xelatex
BIBTEX = bibtex

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(XELATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN) || true
	$(XELATEX) $(MAIN).tex
	$(XELATEX) $(MAIN).tex

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.bbl *.blg *.synctex.gz *.fls *.fdb_latexmk *.xdv

distclean: clean
	rm -f $(MAIN).pdf

