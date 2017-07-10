#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
import pprint

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()
    #print('all_text=',all_text)

    ### split off metadata
    content = all_text.split("X-FileName:") # 使用X-FileName: 将文本内容切片两段，X-FileName:后的为后半段，即第 1 段
    #print('content=',content)
    words = []
    if len(content) > 1: # 说明X-FileName:后有内容
        ### remove punctuation
        text_string = content[1].translate(str.maketrans("", "", string.punctuation)) #此处 py2 与 py3 translate 删除元素时，用法不同
        #print('text_string=',text_string)

        ### project part 2: comment out the line below
        #words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)


        from nltk.stem.snowball import SnowballStemmer
        stemmer = SnowballStemmer('english')

        for word in text_string.split():
            words.append(stemmer.stem(word))

        words = ' '.join(words) # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。list to str





    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print ('text=',text)



if __name__ == '__main__':
    main()

