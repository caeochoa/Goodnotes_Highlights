# Goodnotes Highlights
A python script that takes a pdf highlighted in Goodnotes and exports all the highlights into plain text.

Inspired by [Extracting PDF Highlights using Python](https://medium.com/@vinitvaibhav9/extracting-pdf-highlights-using-python-9512af43a6d) and using the python library [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/intro.html)

## Instructions
The script is in the `ghighlights.py` file. Just run it in the terminal and you'll be prompted for the filename (ideally in the same folder as the script).

## Features
- Extracts all text highlighted with Goodnotes annotations as plain text
- Changes the Goodnotes highlights into normal ones in a new PDF file called `highlights_`+original name
- Also tells the difference between different colours of highlights and can do something different to the text in each case.
  - Here it adds the #hmm tag to text highlighted blue so I can find that text later in my Roam database for further reading.

## Further improvements
  - The normal highlights could be better adapted to the text by using **start** and **stop** or **clip**, but for some reason those don't seem to identify all the text in the document
  - Could include a method to automatically export the tables and diagrams
  - Would be nice if script could automatically differentiate between different highlights, currently it just puts them all together and you have to manually separate them
  - It still includes some words and text that shouldn't be included, we have to be careful when highlighting

