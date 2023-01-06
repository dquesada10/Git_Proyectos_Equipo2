import sys
sys.path.append('.')
from mrjob.job import MRJob
from mrjob.step import MRStep
import re, json

#Definicion de variables
WORD_RE = re.compile(r"[\w']+")
COUNTRY_CODES=['US', 'GB', 'AU', 'CA', 'NZ']
LANGUAGE='en'

#Clase que hereda de MRJob y cuyo codigo analiza sentimientos en tweets
class MRFeelingsAnalysis(MRJob):

    #Pasos del MRJob
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_scores,
                  reducer=self.reducer_count_happiness),
            MRStep(reducer=self.reducer_find_max_country)
        ]

    #Step mapper
    def mapper_get_scores(self, _, line):
    
        #Como el fichero json es real, tiene lineas que dan error por eso metemos su lectura en un try-except
        try:   
            record = json.loads(line)

            #Creamos un diccionario de sentimientos usando el archivo AFINN:
            #list of English words rated between -5 y 5 The words have by Finn Årup Nielsen in 2009-2011.
            file = open('AFINN-111.txt')
            dic_score = {} # initialize an empty dictionary
            file
            for line in file:
                term, score = line.split("\t") # The file is tab-delimited.
                dic_score[term] = int(score) 

            if (record['lang'] == LANGUAGE) and (record['place']['country_code'] in COUNTRY_CODES):
                #Buscamos para cada palabra del texto del tweet buscampos en el diccionario y recuperamos su valor
                try:
                    tweet = record['text']
                    country= record['place']['country_code']
                    asign = []
                    for word in WORD_RE.findall(tweet):
                        try:
                            asign.append(dic_score[word.lower()])
                            media=round(sum(asign)/len(asign))

                            #Pasamos al reducer pais y puntuación media por cada tweet
                            yield(country, media)
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    #Step reducer felicidad medida de cada pais
    def reducer_count_happiness( self,country, score):   
        n = sum = 0
        #Sacamos el sentimiento medio por pais. Para ello acumulamos el score y el contador en cada vuelta(observacion)
        for i in score:
            n += 1
            sum += i  
        yield None, (round(sum/n,1), country)
        
        #print 'La puntuación media de los sentimientos en los tweets en : ', country, ' es: ', sum/n

    #Step reducer. Pais mas feliz (maximo)
    def reducer_find_max_country(self, _, word_count_pairs):
        m=max(word_count_pairs)
        yield(m)
        
        m_list = m
        a=round(m_list[0],1)
        b=m_list[1]
        print 'The happiest country between United States, Great Britain, Canada, New Zeland and Australia is: ', b, 'with a score of', a, 'for their twitter feelings'


#Clase que hereda de MRJob y cuyo codigo analiza los Hastags en los tweets
class MRHastags(MRJob):

    #Pasos del MRJob
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_hashtags,
                 reducer=self.reducer_hashtags_num),
            MRStep(reducer=self.reducer_top5_hashtags)
        ]

    #Step mapper
    def mapper_get_hashtags(self, _, line):
         
        #Para cada palabra del tweet buscamos las que tengan # en su primer caracter y las emitimos
        try:   
            record = json.loads(line)
            if (record['lang'] == LANGUAGE) and (record['place']['country_code'] in COUNTRY_CODES):
                try:
                    tweet=record['text'].split()
                    
                    for word in tweet:
                        if word[0]=='#':
                            yield (word.lower(),1)
                    
                except:
                    pass
        except:
            pass

    #Step reducer para contar el numero de ocurrencias de cada hastag distinto
    def reducer_hashtags_num(self, word, counts):
        num=sum(counts)
        yield None, (num, word)

    #Step reducer para ordenar las diferentes palabras hastag con su frecuencia de mayor a menor y quedarnor con las 5 mas frecuentes (top5)
    def reducer_top5_hashtags(self, _, word_count_pairs):
        print 'TOP5 Hastags between United States, Great Britain, Canada, New Zeland and Australia: '
        for i, word in enumerate(sorted(word_count_pairs, reverse=True)):
            yield (word)
            hastag=word[1]
            print hastag
            if i == 4:
                break
    
if __name__ == '__main__': 
    #MRFeelingsAnalysis.run()
    MRHastags.run()