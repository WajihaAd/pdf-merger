import pypdf as p
try:
  #merging a file
  merge=p.PdfWriter()
  for i in ["pdfkk.pdf","ReDFG (1).pdf","RTUH.pdf"]:
    merge.append(i)
  merge.write("resumefile.pdf")
  merge.close()
   #reading from file
  reader = p.PdfReader("pdfkk.pdf")
  page = reader.pages[0]
  print(page.extract_text())


    
    
  
except Exception as e:
  print(e)
