consonant= ('b','c','d','f','g','h','j','k','l','m','n','q','r','s','t','v','w','x','y','z','p')
vowel=('a','e','i','o','u')
ay="ay"


def isPigLatin(word):
    result= ""
    if (word[0] in vowel):
        result= word+ 'ay'
        return result
    else:
        result=word
        for consonants in word: 
            firstletter= result[0]
            if firstletter in consonant:
                result= result[1:]+firstletter
            else:
                result= result+ay
                break
        return result



def piglatin():
    print("--------------------------------------------")
    sentence = input("Enter a sentence you want to translate: ")
    sentence= str.lower(sentence)
    piglist=[]
    for word in sentence.split():
        piglist.append(isPigLatin(word))
    print(piglist)
    print("--------------------------------------------")


def menu():
    print("Would you like to try again?")
    print("[1] Yes")
    print("[2] No")
    option=int(input("Enter your option:"))
    if option==1:
        piglatin()
        menu()
    elif option==2:
        print("Thank you for using this translator!")
        print("-----------END OF PROGRAM---------------------------------")
    else:
        print("wrong option")
        menu()

print("--------------------------------------------")
print("Pig Latin Translator")
piglatin()
menu()
