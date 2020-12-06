#ex23.py Strings, Bytes, and Character Encodings
# python ex23.py utf-8 0
# python ex23.py utf-16 strict
# python ex23.py big5 strict
import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)
		
def print_line(line, encoding, errors):
	next_lang = line.strip() #What does strip function do
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	
	print(next_lang,">===<", raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages,encoding, error)
brokenString = "فارسی"
print(brokenString)
