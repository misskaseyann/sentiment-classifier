# Naive Bayes Text Sentiment Classification

Uses Naive Bayes and Bag of Words to give a binary classification of sentiment.

### Approach

I used Python as the programming language along with three different packages: os, numpy, and nltk. The os package is for reading multiple text files in a loop, numpy is used for n-dimensional vector arrays along with logarithmic functions, and nltk (more specifically PorterStemmer) is used for word stemming. The dataset I used was the IMDB Movie Review Dataset to distinguish positive and negative sentiment.

I have two classes in my sentiment classification package. The first class implements the bag-of-words model with parameters for a file path, stop word list, number of n-grams, and a Boolean for stemming. It is set to read text files in a directory and then tokenize them. The tokenize function makes the text lower case and then eliminates html tags, punctuation, quotation, extra spaces, and other odd characters. The program then splits all the text into an array of words and checks for any n-grams for that split. Stop words are also implemented but I experimented with whether I should add stop words or not (see experiments performed).  Stemming was implemented last before all the data was compiled together. After the program reads through all the documents, a vocabulary is made with the use of Python’s Dictionary data structure. This vocab, along with the documents, get made into feature vectors containing the number of words in the vocab being used. The second class is the Naïve Bayes classifier. This holds the mathematical logic for creating the prior and conditional probabilities. These are stored for future use when the prediction function is used with unclassified documents.

### Experiments Performed

I played with plenty of different settings to see what was most efficient. I did find that having no stop words and word stemming gave me a 1.16% increase in true positives. However, this was not enough of an increase to encourage further use when it used up longer computing time (upwards to thirty more minutes) due to the volume of words being run through the CPU and not the GPU. I tried using no stop words with 2 n-grams but this gave me too many “unique” words. I wasn’t able to record how large my vocabulary was due to the fact that I went to bed while letting my computer run, only to wake up to a SIGKILL message. My experimentation with n-grams because of this was cut short due to time. In the future, I hope to create some more efficient data structures to handle this experimentation. 

I tried experimenting with word stemming using the natural language tool kit. This actually made my classifier worse by up to 2% depending on whether or not I stripped digits from the text. I strongly believe that this function wouldn’t be entirely useless if it was used on legit literature but since the documents were scraped from the internet, proper English was not the top priority of the writers.

The importance of whether or not digits should be used in classifying a document was something I was also curious about. To me, it seemed as if digits would be white noise just like quotations or brackets. However, when I ran my classifier without digits and with digits, the digits allowed a performance increase of 0.8%. It is a small number in the positive direction but still means it is just white noise.

One other experiment I had was utilizing different stop word dictionaries. The main one I used for most of my experimentation was the Google search stop words. The other one was my own creation of stop words based on the most common words in the vocabulary of my documents being classified. This is of course a very specific case and would not exactly be translatable to other types of classification projects outside of movie reviews. My stop word dictionary included some common useless words that would be found in both the positive and negative reviews such as: actors, movie, scene, cast, characters, film.

#### Google stop words.
```
i,a,about,an,and,are,as,at,be,by,for,from,how,in,is,it,of,on,or,that,the,this,to,was,what,when,where,who,
will,with,the
```

<img src="http://i63.tinypic.com/2rmtbv4.png"/>

#### Hand curated stop words based on dataset.
```
the,and,a,of,to,is,in,it,i,this,that,was,as,for,with,movie,but,film,on,you,are,his,have,be,he,its,all,at,
by,an,they,from,who,so,her,or,about,has,if,some,there,what,when,even,she,my,would,which,see,their,were,
had,me,than,we,been,get,will,do,into,also,other,people,because,how,him,most,made,then,movies,make,way,
them,films,too,after,characters,think,watch,character,many,seen,being,plot,acting,where,your,end,start,
man,here,these,say,scene,scenes,while,go,such,something,im,those,watching,years,now,thing,actors,find,us,
again,director,cast,thats,things,got,around,series,both,ive,gets,role
```

### Problems Encountered

One interesting problem I ran into involved reading in the text files. When I trained the algorithm on an entire set of documents, everything would run fine. However, when I took a chunk of the training data for debugging purposes, the program would crash due to a UnicodeDecodeError. I tried to force different types of encoding such as utf-8 but then the program would throw another error involving invalid ASCII codes. The strangest part of this was it only happened on the micro dataset made from the larger dataset. I never found a solution to this issue.

### Effectiveness of Classifier

The classifier I created was not the most effective. The best it could do overall in correctly classifying the sentiment of the IMDB dataset was 83.7%. For some reason it did better identifying negative documents with a rate of 89.4% correct. Positive documents were over 10% worse in classification with up to 78.0% correct. I experimented with different combinations of n-grams, tokenization, stemming, and stop words but it couldn’t get better than 89.4%.

<img src="http://i68.tinypic.com/10cj4g7.png" width=600/>

### Analysis of Results

Based on the paper Learning Word Vectors for Sentiment Analysis provided alongside the IMDB dataset that I trained this algorithm on, it appears that my classifier is not terribly far off. Using the same dataset, their classifier ranged from 83.96% to 88.89% correctness with two classes. 

<img src="http://i63.tinypic.com/u579e.png" width=400/>

What I feel hurt the classifier the most in its training is the data itself. The dataset is from IMDB user reviews which means the language used is not typical dictionary English. This creates a vocabulary that is very large with words that become noisy amongst other data points. I would like to see how well the classifier would do if it was instead trained on a dataset that was made up of movie reviews seen on casual blogs (such as Medium or Gawker) which utilize a high level vocabulary without getting too far into “internet” words and misspellings. I believe that the classifier would run much better this way. 

<img src="http://i65.tinypic.com/jhu2s9.png" width=400/>

### Misclassifications

The most misclassifications happened within the positive review dataset. Some examples are as followed with words bolded that I believe threw off the classifier:

##### Classified: Negative | Actual: Positive
>How many movies are there that you can think of when you see a movie like this? I can't count them but it sure seemed like the movie makers were trying to give me a hint. I was reminded so often of other movies, it became a big **distraction**. One of the borrowed memorable lines came from a movie from 2003 - Day After Tomorrow. One line by itself, is not so **bad** but this movie borrows so much from so many movies it becomes a **bad** risk. BUT... See The Movie! Despite its **downfalls** there is enough to make it interesting and maybe make it appear clever. While borrowing so much from other movies it never goes **overboard**. In fact, you'll probably find yourself battening down the hatches and riding the storm out. Why? ...Costner and Kutcher played their characters very well. I have never been a fan of Kutcher's and I nearly gave up on him in The Guardian, but he surfaced in good fashion. Costner carries the movie swimmingly with the best of Costner's ability. I don't think Mrs. Robinson had anything to do with his success. The supporting cast all around played their parts well. I had no problem with any of them in the end. But some of these characters were used too much. From here on out I can only nit-pick so I will save you the wear and tear. Enjoy the movie, the parts that work, work well enough to keep your head above water. Just **don't** expect a smooth ride. 7 of 10 but almost a **6**.

##### Classified: Negative | Actual: Positive
>I was fortunate enough to see this movie on pre-release last night and, though I **wasn't** expecting to, actually really enjoyed the movie for the most part. The rescues and sea effects were amazing to watch and definitely provided edge of the seat tense moments, probably all the more so knowing that there are guys who do this for a living. The **weaker** parts of the movie revolve largely around using **stereotypical** set scenes. I'm not going to **spoil** the movie but this really follows along the lines of An Officer and a Gentleman and those moments give it a little bit of a **cheesy aftertaste**. Like I said over all this movie is pretty good and worth checking out as long as you can get past the **clichés**.

##### Classified: Negative | Actual: Positive
>If you had asked me how the movie was throughout the film, I would have told you it was great! However, I left the theatre feeling **unsatisfied**. After thinking a little about it, I believe the **problem** was the pace of the ending. I feel that the majority of the movie moved kind of **slow**, and then the ending developed very fast. So, I would say the ending left me **disappointed**. I thought that the characters were well developed. Costner and Kutcher both portrayed their roles very well. Yes! Ashton Kutcher can act! Also, the **different** relationships between the characters seemed very real. Furthermore, I thought that the different plot lines were well developed. Overall, it was a good movie and I would recommend seeing it. In conclusion: Good Characters, Great Plot, **Poorly** Written/Edited Ending. Still, Go See It!!!

If I were to draw any general rules out of this, it would be that the English language is vast and the expression of sentiment is very complex. Pulling together the data with a bag-of-words model is one way to approach this problem but I think it would be good to use this alongside some other method that looks at each word in a sentence in order to fully comprehend its context. There is a difference between “This movie is so bad,” and “It’s so bad that it’s good.”

### Class Words

Certain words are more likely to end up in one class or the other because they are naturally used to describe what is “good” or “bad.” These words are what would be commonly used to describe feeling and opinion. In the table below, I capture common vocabulary found in the negative and positive datasets.

<img src="http://i68.tinypic.com/2ebv0uo.png" width=400/>

