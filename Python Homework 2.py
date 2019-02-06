# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 20:19:18 2019

@author: bbrath
"""

Title = "MY FAVOURITE SONG ON GRADUATION DAYS"
album, composer, DurationinSec = "O mere sapno ki rani", "Bibhuti Rath", 234
def movie():
 movie = "Aradhana"
 return movie;
def MalePlayBack():
    MalePlayBack = "Kishore Kumar"
    return MalePlayBack;

def durationinSec():
    durationinSec = 234
    if durationinSec < 250:
       return True;
release_year = 1972
print(Title)
print("The song " + album + " is from movie " ,movie() , " by " , MalePlayBack() )
print("The duration of the song is less than 250 seconds", durationinSec())
print("The song release in year: ", release_year)

