import random
import os

hangman = ["
.-=-.      
|   |,
  |       
  |       
.-=-.      
|   |,
   _______
  |       
  |      
.-=-.      
|   |,
   _______
  |       |
  |      
.-=-.      
|   |,
   _______
  |       |
  |       O
.-=-.     
|   |,
   _______
  |       |
  |      _O 
.-=-.     
|   |,
   _______
  |       |
  |      _O_ 
.-=-.     
|   |,
   _______
  |       |
  |      _O_ 
.-=-.     | 
|   |,
   _______
  |       |
  |      _O_ 
.-=-.     | 
|   |    /,
   _______
  |       |
  |      _O_ 
.-=-.     | 
|   |    /\ 
"]

words = ['work', 'lion', 'mail', 'pork', 'play', 'game', 'frog', 'card', 'blue', 'fish']

word = random.choice(words)