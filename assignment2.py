#PythonHomework2
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
def songGenre():
	#local scoped variable
	genre='Bollywood'
	print("Genre : ", genre)
def releaseYear():
	year=2015
	print("Year : ", year)
def artists(singers):
	for singer in singers:
		print("Singer : ", singer)
def songName(songList):
	for song in songList:
		print(song)
def isHit():
	result=True
	return result
songGenre()
releaseYear()
artists(singers)
songName(songList)
print("Hit Album", isHit())
#print("genre:", genre) here we will get NameError as variable genre is having local scope and is accessible only within the function