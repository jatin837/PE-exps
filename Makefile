pdf: out.md
	pandoc -o out.pdf out.md

show: out.pdf
	okular out.pdf
