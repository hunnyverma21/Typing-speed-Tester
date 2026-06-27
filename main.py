import time
import random

paragraphs = [
    "In the heart of the bustling city, the streets were alive with the sounds of honking cars and chattering pedestrians. The aroma of freshly baked bread wafted from the corner bakery, mingling with the scent of blooming flowers from the nearby park.",
    "As the sun set behind the towering skyscrapers, the city transformed into a canvas of twinkling lights. The neon signs flickered to life, casting colorful reflections on the wet pavement, while street performers entertained passersby with their music and acrobatics.",]

paragraph = random.choice(paragraphs)
print(paragraph)

input("\nPress Enter when you are ready...")

start_time = time.time() 
typed_text = input("Type here: ")
end_time =time.time()

time_taken = end_time-start_time    
print("time taken :",time_taken,"seconds")

if typed_text == paragraph:
    print("congratulations! you typed the paragraph correctly.")
else:
    print("Oops! There were some mistakes in your typing. Please try again.")