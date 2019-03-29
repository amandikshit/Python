#PythonHomework1
#album is a variable of type str
album='Dhoom3'
type(album)
#totalNoOfSongs is a variable of type int
totalNoOfSongs=9
#songList is a variable of list data type
songList=['Malang','Kamli','Tu Hi Junoon','Bande Hain Hum Uske','Dhoom Tap','Dhoom : 3 Overture','Dhoom Machale Dhoom (Arabic)','Dhoom Machale Dhoom (Spanish)']
#totalDuration is a variable of type float
totalDuration=27.24
myFavSong='Malang'
favSongDuration=4.33
music='Pritam'
singers=['Sunidhi Chauhan','Mohit Chauhan']
print('Album Name', album)
print('No of Songs', totalNoOfSongs)
print('List of Songs:')
for s in songList:
	print(s)
print('Total Album Length :',totalDuration)
print('My Favourite Song', myFavSong)
for singer in singers:
	print(singer)
