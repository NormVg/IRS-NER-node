import spacy

nlp_ner = spacy.load("model/model-best")
remove_ele = ["of","in","about","tell","song","movies","movie","is","on","the","buy","up","watch"]

async def NER(text,tag):
    doc = nlp_ner(text)
    for ent in doc.ents:
        if tag == ent.label_:
            print(ent.text,ent.label_)
            text_lst = str(ent.text).split(" ")
            for i in remove_ele:
                try:
                    text_lst.remove(i)
                except:pass
            text = " ".join(text_lst)
            return text
    
    return '000'

if __name__ == "__main__":
    while True:
        i = input("NER> ")
        NER(i)