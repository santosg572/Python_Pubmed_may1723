from pymed import PubMed

pubmed = PubMed(tool="MyTool", email="my@email.address")

#query = "ANTs[Title/Abstract]"

query = "psychopy[Title/Abstract]"

results = pubmed.query(query, max_results=500)

for article in results:
 print(article.toJSON())

