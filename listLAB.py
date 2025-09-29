hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY',
              'STAIRWAY TO HEAVEN','RIDERS ON THE STORM',
              'WISH YOU WERE HERE']

print(hitsTitles)

hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')

print(hitsTitles)

hitsTitles.insert(2,  'HOTEL CALIFORNIA')

print(hitsTitles)

hitsTitles.insert(0,  'THE SOUND OF SILENCE')

print(hitsTitles)

print(hitsTitles.index('HOTEL CALIFORNIA'))

hitsTitles.remove('HOTEL CALIFORNIA')

hitsTitles.remove('THE SOUND OF SILENCE')
hitsTitles.insert(0,'ENJOY THE SILENCE')

print(hitsTitles)

hitsToRead = hitsTitles.copy()

hitsToRead.reverse()

hitsToRead.sort()

hitsToRead.pop(0)
hitsToRead.pop(1)

additionalSongs = ['NOTHING COMPARES 2 U' , 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs) 

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()


