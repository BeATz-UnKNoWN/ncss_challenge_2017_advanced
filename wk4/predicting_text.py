# Implement the following Node class API.
# If you delete something important, this code is copied in specification.py
from collections import defaultdict

def traverseNodeAndCreate(parentNode, currWord, restWord):
  if restWord=='':parentNode.isWord=True;return
  newCurr = currWord+restWord[0]
  #if the first letter is already a key in the dictionary
  #we jump to that child node
  if restWord[0] in parentNode.childNodes:
    traverseNodeAndCreate(parentNode.childNodes[restWord[0]],newCurr,restWord[1:])
  else:
    #otherwise we create a new node
    node = Node(newCurr)
    #and add it to the parent's childNodes, with the key as a letter
    parentNode.childNodes[restWord[0]]=node
    #then we traverse to this new child node
    traverseNodeAndCreate(node,newCurr,restWord[1:])
  
def traverseNodeAndFind(parentNode, restPrefix):
  #if no prefix was specified, do nothing
  if len(restPrefix)==0:return None
  #if this is the final letter branch to check, return the child
  elif len(restPrefix)==1:return parentNode.childNodes[restPrefix]
  #if there are still more letter branches to traverse, do so
  elif restPrefix[0] in parentNode.childNodes:
    return traverseNodeAndFind(parentNode.childNodes[restPrefix[0]],restPrefix[1:])
  return None
  
def traverseNodeAndFindAll(parentNode, found):
  #if the current node is a word, add it to the list
  if parentNode.isWord: found.append(parentNode.prefix)
  #traverse each letter branch for each child node, recursively
  for branch in parentNode.childNodes:
    traverseNodeAndFindAll(parentNode.childNodes[branch], found)

class Node:
  def __init__(self, prefix):
    """
    Creates a Node with the given string prefix.
    The root node will be given prefix ''.
    You will need to track:
    - the prefix
    - whether this prefix is also a complete word
    - child nodes
    """
    self.prefix=prefix
    self.isWord=False
    '''
    childNodes will be a dictionary with the
    next letter following the parent's prefix as the key
    The values of the dictionary are nodes
    '''
    self.childNodes={}
    pass
  
  def get_prefix(self):
    """
    Returns the string prefix for this node.
    """
    return self.prefix
    pass
  
  def get_children(self):
    """
    Returns a list of child Node objects, in any order.
    """
    return [self.childNodes[key] for key in self.childNodes]
    pass
  
  def is_word(self):
    """
    Returns True if this node prefix is also a complete word.
    """
    return self.isWord
    pass
  
  def add_word(self, word):
    """
    Adds the complete word into the trie, causing child nodes to be created as needed.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> root.add_word('cheese')
    """
    traverseNodeAndCreate(self,'',word)
    pass
  
  def find(self, prefix):
    """
    Returns the node that matches the given prefix, or None if not found.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> node = root.find('te')
    """
    return traverseNodeAndFind(self,prefix)
    pass
  
  def words(self):
    """
    Returns a list of complete words that start with my prefix.
    The list should be in lexicographical order.
    """
    allWords=[]
    traverseNodeAndFindAll(self, allWords)
    return sorted(allWords)
    pass


if __name__ == '__main__':
  # Write your test code here. This code will not be run by the marker.

  # The first example in the question.
  root = Node('')
  for word in ['tea', 'ted', 'ten']:
    root.add_word(word)
  node = root.find('te')
  print(node.get_prefix())
  print(node.is_word())
  print(node.words())

  # The second example in the question.
  root = Node('')
  for word in ['inn', 'in', 'into', 'idle']:
    root.add_word(word)
  node = root.find('in')
  print(node.get_prefix())
  children = node.get_children()
  print(sorted([n.get_prefix() for n in children]))
  print(node.is_word())
  print(node.words())

  # The third example in the question.
  with open('the-man-from-snowy-river.txt') as f:
    words = f.read().split()
  root = Node('')
  for word in words:
    root.add_word(word)
  print(root.find('th').words())