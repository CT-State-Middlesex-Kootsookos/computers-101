jupyter-book build .  --builder pdfhtml
cp _build/pdf/book.pdf files/computers-101.pdf
jupyter-book build . 
ghp-import -n -p -f _build/html
