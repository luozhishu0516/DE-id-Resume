import spacy
from spacy.matcher import Matcher

def open_text_file():
    text=""
    file_name = input("Please Enter File Name Here: ")
    try:
        with open(file_name, 'r') as f:
            text = f.read()
    except:
        print("Please Enter Your File Name Again:")
        open_text_file()
    return text

def resume_cleaning(txt):
    outp=""
    outp2=""
    nlp = spacy.load("/output/model-best")##Each computer might have different path for model, if this doesnt work please copy your own path
    doc=nlp(txt)
    for token in doc:
        if token.ent_type_ == "Name":
            outp = outp + " " + len(token) * "*"
        else:
            outp = outp + " " + token.text
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(outp)
    for token in doc:
        if token.like_email:
            outp2 = outp2 + " " + len(token) * "*"
        elif token.ent_type_=="CARDINAL":
            outp2 = outp2 + " " + len(token) * "*"
        else:
            outp2 = outp2 + " " + token.text
    f=open("clean_resume.txt", "w+")##Same as above please use your own Path
    f.write(outp2)
    f.close()

def main():
    text=open_text_file()
    resume_cleaning(text)

main()

