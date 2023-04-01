
# 12. Below are the notes used in music:
# C C# D D# E F F# G G# A A# B
# The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps
# past C and G is 7 steps past C. This works for any base. For example, the notes for D major
# are D, F#, A. We can represent the major chord steps as a list with two elements: [4,7]. The
# corresponding lists for some other chord types are shown below:
# Minor [3,7]               Dominant seventh [4,7,10]
# Augmented fifth [4,8]     Minor seventh [3,7,10]
# Minor fifth [4,6]         Major seventh [4,7,11]
# Major sixth [4,7,9]       Diminished seventh [3,6,10]
# Minor sixth [3,7,9]
# Write a program that asks the user for the key and the chord type and prints out the notes of
# the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists
# of steps.



class MusicChords:
    def get_chords():
        type = {'Major':[4,7], 'Minor':[3,7], 'Diminished':[3,6],
                'Augmented':[4,8], 'Minor Sixth':[3,7,9], 'Major Sixth':[4,7,9],  
                'Dominant Seventh':[4,7,10], 'Minor Seventh':[3,7,10], 'Major Seventh':[4,7,11], 
                'Minor Major Seventh':[3,7,11], 'Diminished Seventh':[3,6,10], 'Ninth':[4,7,11,2]}
        keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
        print('\nCHORD TYPES')
        for i in type.keys():
            print(i)
        print('N/B: Capitalize Each Word!!!!')
        key = str(input('\nEnter Key: ')).strip().title()
        ty = str(input('Enter chord type: ')).strip().title()
        chord = [key]
        for i in type[ty]:
            chord.append(keys[keys.index(key)+i])
        print('The notes of ' + key + ' ' + ty + ' are ' + '-'.join(chord))
    get_chords()

