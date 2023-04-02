import random
import json

genres = ['rock', 'rap', 'metal', 'jazz', 'pop', 'country']
artists = [
    'The Beatles',
    'Led Zeppelin',
    'Pink Floyd',
    'The Rolling Stones',
    'Queen',
    'AC/DC',
    'Black Sabbath',
    'The Who',
    'Guns N\' Roses',
    'Nirvana',
    'Metallica',
    'U2',
    'The Doors',
    'Jimi Hendrix',
    'Bruce Springsteen',
    'David Bowie',
    'The Eagles',
    'Tom Petty',
    'Fleetwood Mac',
    'Van Halen',
    'Rush',
    'Notorious B.I.G.',    'Tupac',    'Nas',    'Jay-Z',    'Eminem',    'Kendrick Lamar',    'Drake',    'Kanye West',    'Outkast',    'Wu-Tang Clan',    'Public Enemy',    'Run-DMC',    'Beastie Boys',    'LL Cool J',    'Ice Cube',    'Snoop Dogg',    '50 Cent',    'Lil Wayne',    'Missy Elliott',    'Busta Rhymes',    'A Tribe Called Quest',    'Mos Def',    'Common',    'Chance the Rapper',    'Cardi B',    'J. Cole',    'Travis Scott',    'Migos',    'Post Malone',    'Tyler, The Creator',    'Childish Gambino',    'Lauryn Hill',    'The Roots',    'Gang Starr',    'Rakim',    'KRS-One',    'Big Daddy Kane',    'Grandmaster Flash and the Furious Five',    'De La Soul',    'Fugees',    'N.W.A.',    'Scarface',    'DMX',    'Ludacris',    'Big L',    'Ghostface Killah',    'Raekwon',    'GZA',    'MF DOOM',    'Black Star',    'Run the Jewels',    'Danny Brown',
    'Louis Armstrong',    'Duke Ellington',    'Miles Davis',    'Charlie Parker',    'John Coltrane',    'Ella Fitzgerald',    'Billie Holiday',    'Thelonious Monk',    'Dave Brubeck',    'Art Blakey',    'Chet Baker',    'Herbie Hancock',    'Sonny Rollins',    'Ornette Coleman',    'Dizzy Gillespie',    'Stan Getz',    'Cannonball Adderley',    'Charles Mingus',    'Oscar Peterson',    'Wes Montgomery',    'Django Reinhardt',    'Pat Metheny',    'Sarah Vaughan',    'Coleman Hawkins',    'Lester Young',    'Keith Jarrett',    'Wynton Marsalis',    'Count Basie',    'Benny Goodman',    'Lionel Hampton',    'Chick Corea',    'Joe Pass',    'George Benson',    'Gil Evans',    'Bud Powell',    'Clifford Brown',    'Max Roach',    'Jimmy Smith',    'Jimmy Heath',    'Johnny Hartman',    'Tony Williams',    'Pharoah Sanders',    'Bill Evans',    'Eddie Palmieri',    'Lee Morgan',    'Horace Silver',    'Cecil Taylor',    'Roy Ayers',    'Gary Burton',    'Joe Henderson',
    ]
song_titles = [
    "Stairway to Heaven",
    "Bohemian Rhapsody",
    "going to the grocery store",
    "riding a bicycle through times square",
    "going to coachella with your friends",
    "working at red robin slinging burgers",
    "teaching at the university of michigan",
    "swimming in the ocean in hawaii",
    "going on vacation",
    "being a college student", 
    "teeth like god's shoeshine",
    "the predatory wasp of the palisades is out to get us",
    "take me in your arms",
    "like minded people",
    "windows futures like minds country roads"
]

def generate_examples():
    training = []
    validation = []
    cnt = 0
    for artist in artists:
        for genre in genres:
            for title in song_titles:
                examples = [f'Please generate a {genre} song in the style of {artist}', 
                            f'Please write a {genre} song in the style of {artist}', 
                            f'write a {genre} song in the style of {artist}',
                            f'make a {genre} song by {artist}',
                            f'create {genre} song lyrics in the style of {artist}',
                            f'generate {genre} lyrics from the perspective of {artist}',
                            f'generate {artist} lyrics in a {genre} genre',
                            f'write {artist} lyrics in a {genre} genre',
                            f'write lyrics by {artist} please',
                            f'write lyrics by {artist} pretty please',
                            f'write lyrics by {artist} in the style of {genre} for me please',
                            f'write a {genre} song',
                            f'write a {genre} song by {artist} um yes',
                            f'would you make a {genre} song by {artist} please',
                            f'generate lyrics to a song by {artist} please in a {genre} genre',
                            f'write {genre} lyrics in the style of {artist} for me',
                            f'write a {genre} song by {artist} um yes',
                            f'would you make a {genre} song by {artist} please',
                            f'generate lyrics to a song by {artist} please in a {genre} genre',
                            f'write {genre} lyrics in the style of {artist} for me',
                            f'I want {genre} lyrics by {artist} for my song titled {title}',
                            f'I want {genre} lyrics by {artist} about {title} NOW!',
                            f'Please generate a {genre} song about {title} in the style of {artist}', 
                            f'Please write a {genre} song with the title {title} in the style of {artist}', 
                            f'write a {genre} song titled {title} in the style of {artist}',
                            f'make a {genre} song by {artist} titled {title}',
                            f'create {genre} song lyrics in the style of {artist} about {title}',
                            f'generate {genre} lyrics about {title} from the perspective of {artist}',
                            f'generate {artist} lyrics titled {title} in a {genre} genre',
                            f'write {artist} lyrics in a {genre} genre and the title is {title} please',
                            f'write lyrics by {artist} please about {title}',
                            f'please generate a song about {title} but the lyrics are by {artist} pretty please',
                            f'write lyrics about {title} by {artist} in the style of {genre} for me please',
                            f'write a {genre} song about {title}',
                            f'write a song about {title} and it is a {genre} song by {artist} um yes',
                            f'would you make a {genre} song by {artist} please and the title is something like {title}',
                            f'generate lyrics to a song about {title}',
                            f'write a song with the title {title}',
                            f'write a song titled {title} in a {genre} style',
                            f'would you make a song about {title} by {artist} please',
                            f'generate lyrics to a song about {title} please in the style of {artist}',
                            f'write lyrics in the style of {artist} for me with the title {title}',
                            f'I want lyrics by about {title} for my song'
                            ]
                for example in examples:
                    entities_list = []
                    try:
                        artist_start = example.index(artist)
                        artist_end = artist_start + len(artist)
                        entities_list.append((artist_start, artist_end, 'ARTIST'))
                    except:
                        pass
                    try:
                        genre_start = example.index(genre)
                        genre_end = genre_start + len(genre)
                        entities_list.append((genre_start, genre_end, 'GENRE'))
                    except:
                        pass
                    try:
                        title_start = example.index(title)
                        title_end = genre_start + len(title)
                        entities_list.append((title_start, title_end, 'TITLE'))
                    except:
                        pass


                    if cnt < 400000: # TODO
                        training.append((example, {'entities': entities_list}))
                        cnt = cnt + 1
                    else:
                        validation.append((example, {'entities': entities_list}))     
                        cnt = cnt + 1  

    print("NUM EXAMPLES\n")
    print(cnt)

    return training, validation

# artists = [x.lower() for x in artists]
song_titles = [x.lower() for x in song_titles]

training, validation = generate_examples()

training_output = {'classes': ['GENRE', 'ARTIST'], 'annotations': training}
validation_output = {'classes': ['GENRE', 'ARTIST'], 'annotations': validation}

with open('val_dataset.json', 'w') as f:
    json.dump(validation_output, f)

with open('train_dataset.json', 'w') as f:
    json.dump(training_output, f)


# consider making all user input lowercase for consistency