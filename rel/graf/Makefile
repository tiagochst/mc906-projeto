#Relatorio
file=graficos
rel:
	latex $(file).tex
	latex $(file).tex
	dvips $(file).dvi -o
	ps2pdf13 $(file).ps
relshow:
	evince $(file).pdf
relClean:
	rm *.dvi *.aux *.out *.log
