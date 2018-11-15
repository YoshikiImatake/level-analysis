import Analyzer


full_text = ""
while True:
	try:
		text = input()
		text += "\n"
		full_text += text
	except EOFError:
		break

a1 = Analyzer.Analyzer(full_text, False)
a1.sentence_length()