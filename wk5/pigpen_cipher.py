#With help from Andrew Wong

from PIL import Image
filepath = input("Enter path: ")
 
# Reading in the file
im = Image.open(filepath)
 
 
# Get an array of intensity values (linear sequence from top left to bottom right)
pixels = list(im.getdata())
 
# Manually split the image based off the length of the entire image)
width, height = im.size
#print(width,"x",height)
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
#print(pixels[2][2])
 
isWhiteRow = lambda array: 0 not in array
isWhiteCol = lambda array, pos: 0 not in ([row[pos] for row in array])
isBlackRow = lambda array: 255 not in array
isBlackCol = lambda array, pos: 255 not in ([row[pos] for row in array])
 
# Now we want to separate each letter line - we are told that there is at least one horizontal line of pixels; so we just need to find where there is a pixel row that is completely white -> RGBA(255, 255, 255, 255)
 
# Clean up pixel grid
_pixels = []
for row in pixels:
  if not isWhiteRow(row) or not isWhiteRow(_pixels[-1] if _pixels else [(0,0,0,255)]):
    _pixels.append(row)
pixels = _pixels
pixels = pixels[1:] if isWhiteRow(pixels[0]) else pixels # Remove leading white row
pixels = pixels[:-1] if isWhiteRow(pixels[-1]) else pixels # Remove leading trailing white row
 
##
# So now we have an array that looks like this:
#  pixels = [
#    [RGB, RGB, RGB, RGB, RGB, ...],
#    [RGB, RGB, RGB, RGB, RGB, ...],
#    [RGB, RGB, RGB, RGB, RGB, ...],
#    [WHITE,  WHITE,  WHITE,  ... ],
#    [RGB, RGB, RGB, RGB, RGB, ...],
#                ...
#    [RGB, RGB, RGB, RGB, RGB, ...]
#  ]
##
# Next we will split the array by white rows
lettersequence = [[]]
[(lettersequence.append([]) if isWhiteRow(row) else lettersequence[-1].append(row)) for row in pixels]
 
#
# So now we have an array that looks like this:
#  lettersequence =
#    [
#      [
#        [RGB, RGB, RGB, RGB, RGB, ...],
#        [RGB, RGB, RGB, RGB, RGB, ...],
#        [RGB, RGB, RGB, RGB, RGB, ...]
#      ],
#      [
#        [RGB, RGB, RGB, RGB, RGB, ...],
#        [RGB, RGB, RGB, RGB, RGB, ...],
#        [RGB, RGB, RGB, RGB, RGB, ...]
#      ]
#    ]
##
 
# Again we want to split by the white lines, this time by column
letters = []
for letterrow in lettersequence:
  indexes = []
  [(indexes.append(c) if isWhiteCol(letterrow, c) else None) for c in range(len(letterrow[0]))]
  [(letters.append([row[indexes[i]+1:indexes[i+1]] for row in letterrow]) if indexes[i] != indexes[i+1] - 1 else None) for i in range(len(indexes)-1)]
 
#print(len(letters),"letters")
 
# Now we should have an array of arrays of tuples
#  letters =
#    [
#      [RGB, RGB, RGB, RGB, RGB, ...],
#      [RGB, RGB, RGB, RGB, RGB, ...],
#      [RGB, RGB, RGB, RGB, RGB, ...]
#    ],
#    [
#      [RGB, RGB, RGB, RGB, RGB, ...],
#      [RGB, RGB, RGB, RGB, RGB, ...],
#      [RGB, RGB, RGB, RGB, RGB, ...]
#    ]
#  ]
##
# Now, crop each letter into a square grid (Top left is the anchor for the letter)
letters = list(map(lambda letter: list(filter(lambda row: not isWhiteRow(row), letter)), letters))
'''for letter in letters:
  print(len(letter[0]), "x", len(letter))'''
output=''
for letter in letters:
  size=len(letter)
  mid=int(size/2)
  i=letter[mid][mid]==0
  if isBlackRow(letter[0]):
    if isBlackRow(letter[size-1]):
      if isBlackCol(letter, 0):
        if isBlackCol(letter, size-1):
          output+=['E','N'][i];continue
        else:
          output+=['F','O'][i];continue
      else:
        if isBlackCol(letter, size-1):
          output+=['D','M'][i];continue
    else:
      if isBlackCol(letter, 0):
        if isBlackCol(letter, size-1):
          output+=['H','Q'][i];continue
        else:
          output+=['I','R'][i];continue
      else:
        if isBlackCol(letter, size-1):
          output+=['G','P'][i];continue
  else:
    if isBlackCol(letter, 0):
      if isBlackCol(letter, size-1):
        output+=['B','K'][i];continue
      else:
        output+=['C','L'][i];continue
    else:
      if isBlackCol(letter, size-1):
        output+=['A','J'][i];continue
  if letter[0][0]==0:
    if letter[0][size-1]==0:
      output+=['S','W'][i]
    elif letter[size-1][0]==0:
      output+=['T','X'][i]
  elif letter[size-1][size-1]==0:
    if letter[0][size-1]==0:
      output+=['U','Y'][i]
    elif letter[size-1][0]==0:
      output+=['V','Z'][i]
  else: output+=' '
        
print(output)
    