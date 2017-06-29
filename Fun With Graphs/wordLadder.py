from basicgraph import *
from bfs import *

# Assumption: breadth first search from startNode has already been executed
#
# Extract path from startNode to endNode (by working backwards from endNode),
# returning it as a list e.g. for 'shell'/'spill' the result might be  ['shell', 'spell', 'spill']
# if 'spell' is the parent of 'spill' and 'shell' is the parent of 'spell'
#
def extractWordLadder(startNode, endNode):
     path=[endNode]
     curr=endNode
     while curr!=startNode:
         curr=curr.getParent()
         path.append(curr)
     path.reverse()
     return path

# return True if there should be an edge between nodes for word1 and word2 in the
# word graph. Return False otherwise
def shouldHaveEdge(word1, word2):
    word1=word1.getName()
    word2=word2.getName()
    mistakes=0
    if(word1==word2):
        return True
    for i in range(0,len(word1)):
        if not (word1[i]==word2[i]):
            mistakes+=1
    if mistakes>1:
        return False
    else:
        return True
# return word ladder graph for the given file of five-letter words
#
def buildWordGraph(wordsFile = "words5.text"):
     file= open(wordsFile)
     wordlist=[]
     wordGraph=Graph()
     for line in file:
         stripped=line.rstrip()
         if not (line in wordlist):
            wordlist.append(stripped)
            wordGraph.addNode(Node(stripped))
     file.close()
     # should compare every word in O(nlogn)
     for i in range(0,len(wordlist)):
         for j in range(i+1,len(wordlist)):
             if(shouldHaveEdge(wordGraph.getNode(wordlist[i]),wordGraph.getNode(wordlist[j]))):
                 if not (wordGraph.hasEdge(wordGraph.getNode(wordlist[i]),wordGraph.getNode(wordlist[j]))):
                     wordGraph.addEdge(wordGraph.getNode(wordlist[i]),wordGraph.getNode(wordlist[j]))
     return wordGraph
# return list of words representing word ladder from startNode to endWord in wordGraph
#
def findWordLadder(startWord, endWord, wordGraph):
     # 1. do graph traversal starting from node for startWord
     startNode=wordGraph.getNode(startWord)
     endNode=wordGraph.getNode(endWord)
     bfs(wordGraph,startNode)
     # 2. extract word ladder from the graph
     return extractWordLadder(startNode, endNode)
     

# play the word ladder game using the given file of words
#
def wordLadder(wordsFile = "words5.text"):
     end=False
     # 1. build word graph for the given file of words
     wordGraph=buildWordGraph(wordsFile)
     # 2. user interaction loop:
     #     repeatedly ask user to enter two words, and then find and print the word ladder for those words
     while(end==False):
         startWord = input('Enter starting word: ')
         print("Your word was '{}'.".format(startWord))
         endWord= input('Enter word to path too: ')
         print("Your word was '{}'.".format(startWord))
         print("/n /n Your word ladder is: {}".format(findWordLadder(startWord,endWord,wordGraph)))
         contin= input('Hit Enter to continue or type "quit": ')
         if(contin=="quit"):
             end=True
