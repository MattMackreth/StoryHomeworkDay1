# Initial story created
Story = {
    'hero': 'The Spartan',
    'villain': 'The Persian',
    'title': 'The Spartan vs The Persian',
    'author': 'Matthew Mackreth',
    'beginning': 'In the beginning The Spartan was peacefully making the most of his quiet village life.',
    'middle': 'Then The Persian invaded with a huge army and took over the village leaving The Spartan no choice.',
    'end': 'The Spartan had to fight The Persian, it was a ferocious battle and in the end ',
    'winner': 'The Spartan won.'
}
print(Story['title'])
print('By ' + Story['author'])
print(Story['beginning'])
print(Story['middle'])
print(Story['end'] + Story['winner'])
print("\nNow it's your turn!")
# Initial story output

userhero = input('Who is the hero? ')
uservillain = input('Who is the villain? ')
# Gets user hero and villain and inputs

userchoice = ''
while userchoice != 'hero' and userchoice != 'villain':
    userchoice = input('Who wins? Hero or Villain? ').lower()
    # Loops until user decides who wins with either Hero or Villain case insensitive
username = input('What is your name? ')
# Gets user's name for author field

# Replaces story characters with user's characters
Story['title'] = userhero + ' vs ' + uservillain
Story['beginning'] = Story['beginning'].replace(Story['villain'], uservillain)
Story['beginning'] = Story['beginning'].replace(Story['hero'], userhero)
Story['middle'] = Story['middle'].replace(Story['villain'], uservillain)
Story['middle'] = Story['middle'].replace(Story['hero'], userhero)
Story['end'] = Story['end'].replace(Story['villain'], uservillain)
Story['end'] = Story['end'].replace(Story['hero'], userhero)
Story['author'] = username

# Changes ending based on who user wants to win
if userchoice == 'hero':
    Story['winner'] = userhero + ' won'
else:
    Story['winner'] = uservillain + ' won'
Story['hero'] = userhero
Story['villain'] = uservillain

print('Brilliant! Now here is your story: \n')
# Output's user's story
print(Story['title'])
print('By ' + Story['author'])
print(Story['beginning'])
print(Story['middle'])
print(Story['end'] + Story['winner'])
