import random
import json

genres = ['rock', 'rap', 'metal', 'jazz', 'pop', 'country', 'r&b', 'rhythm and blues']
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
    'The Clash',
    'Radiohead',
    'Pearl Jam',
    'Foo Fighters',
    'Green Day',
    'The Killers',
    'Arctic Monkeys',
    'Red Hot Chili Peppers',
    'Oasis',
    'Coldplay',
    'Blur',
    'The Strokes',
    'The White Stripes',
    'Linkin Park',
    'Nine Inch Nails',
    'System of a Down',
    'Kings of Leon',
    'The Black Keys',
    'Muse',
    'Queens of the Stone Age',
    'Tool',
    'Alice in Chains',
    'Soundgarden',
    'Stone Temple Pilots',
    'The Smashing Pumpkins',
    'The Pixies',
    'R.E.M.',
    'Weezer',
    'Bon Jovi',
    'Notorious B.I.G.',    'Tupac',    'Nas',    'Jay-Z',    'Eminem',    'Kendrick Lamar',    'Drake',    'Kanye West',    'Outkast',    'Wu-Tang Clan',    'Public Enemy',    'Run-DMC',    'Beastie Boys',    'LL Cool J',    'Ice Cube',    'Snoop Dogg',    '50 Cent',    'Lil Wayne',    'Missy Elliott',    'Busta Rhymes',    'A Tribe Called Quest',    'Mos Def',    'Common',    'Chance the Rapper',    'Cardi B',    'J. Cole',    'Travis Scott',    'Migos',    'Post Malone',    'Tyler, The Creator',    'Childish Gambino',    'Lauryn Hill',    'The Roots',    'Gang Starr',    'Rakim',    'KRS-One',    'Big Daddy Kane',    'Grandmaster Flash and the Furious Five',    'De La Soul',    'Fugees',    'N.W.A.',    'Scarface',    'DMX',    'Ludacris',    'Big L',    'Ghostface Killah',    'Raekwon',    'GZA',    'MF DOOM',    'Black Star',    'Run the Jewels',    'Danny Brown',
    'Louis Armstrong',    'Duke Ellington',    'Miles Davis',    'Charlie Parker',    'John Coltrane',    'Ella Fitzgerald',    'Billie Holiday',    'Thelonious Monk',    'Dave Brubeck',    'Art Blakey',    'Chet Baker',    'Herbie Hancock',    'Sonny Rollins',    'Ornette Coleman',    'Dizzy Gillespie',    'Stan Getz',    'Cannonball Adderley',    'Charles Mingus',    'Oscar Peterson',    'Wes Montgomery',    'Django Reinhardt',    'Pat Metheny',    'Sarah Vaughan',    'Coleman Hawkins',    'Lester Young',    'Keith Jarrett',    'Wynton Marsalis',    'Count Basie',    'Benny Goodman',    'Lionel Hampton',    'Chick Corea',    'Joe Pass',    'George Benson',    'Gil Evans',    'Bud Powell',    'Clifford Brown',    'Max Roach',    'Jimmy Smith',    'Jimmy Heath',    'Johnny Hartman',    'Tony Williams',    'Pharoah Sanders',    'Bill Evans',    'Eddie Palmieri',    'Lee Morgan',    'Horace Silver',    'Cecil Taylor',    'Roy Ayers',    'Gary Burton',    'Joe Henderson',
    'Metallica',    'Iron Maiden',    'Black Sabbath',    'Judas Priest',    'Slayer',    'Pantera',    'Megadeth',    'AC/DC',    'Motorhead',    'Guns N\' Roses',    'Ozzy Osbourne',    'System of a Down',    'Disturbed',    'Korn',    'Lamb of God',    'Tool',    'Dream Theater',    'Opeth',    'Mastodon',    'Gojira',    'Deftones',    'Meshuggah',    'Cannibal Corpse',    'Behemoth',    'Cradle of Filth',    'Children of Bodom',    'Arch Enemy',    'In Flames',    'Killswitch Engage',    'Trivium',    'Avenged Sevenfold',    'Slipknot',    'Metal Church',    'Testament',    'Anthrax',    'Overkill',    'Exodus',    'Sepultura',    'Machine Head',    'Death',    'Morbid Angel',    'Carcass',    'At The Gates',    'Dark Tranquility',    'Dio',    'Rainbow',    'Saxon',    'Venom',    'Mercyful Fate',    'King Diamond'
]
song_titles = [
    "Stairway to Heaven",
    "Bohemian Rhapsody",
    "Imagine",
    "Billie Jean",
    "Hey Jude",
    "Let it Be",
    "Thriller",
    "Like a Rolling Stone",
    "I Will Always Love You",
    "Sweet Child O' Mine",
    "Hotel California",
    "Born to Run",
    "Smells Like Teen Spirit",
    "God Save the Queen",
    "What's Going On",
    "Purple Rain",
    "The Times They Are A-Changin'",
    "Yesterday",
    "Good Vibrations",
    "My Girl",
    "Every Breath You Take",
    "Rolling in the Deep",
    "Hallelujah",
    "All Along the Watchtower",
    "Purple Haze",
    "London Calling",
    "Layla",
    "A Day in the Life",
    "Livin' on a Prayer",
    "Nothing Compares 2 U",
    "I Heard It Through the Grapevine",
    "Billie Holiday",
    "In My Life",
    "Imagine",
    "The Twist",
    "Tutti Frutti",
    "Johnny B. Goode",
    "Jailhouse Rock",
    "I Want to Hold Your Hand",
    "A Hard Day's Night",
    "Help!",
    "Yesterday",
    "Can't Buy Me Love",
    "I Feel Fine",
    "All You Need Is Love",
    "Hey Jude",
    "Get Back",
    "Let It Be",
    "Come Together",
    "Something",
    "Here Comes the Sun",
    "I Want You (She's So Heavy)",
    "Abbey Road",
    "Meet the Beatles!",
    "Please Please Me",
    "With the Beatles",
    "Rubber Soul",
    "Revolver"

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
                    
                    if cnt < 17271: # TODO
                        training.append((example, {'entities': entities_list}))
                        cnt = cnt + 1
                    else:
                        validation.append((example, {'entities': entities_list}))     
                        cnt = cnt + 1  

    return training, validation

artists = [x.lower() for x in artists]

training, validation = generate_examples()

training_output = {'classes': ['GENRE', 'ARTIST'], 'annotations': training}
validation_output = {'classes': ['GENRE', 'ARTIST'], 'annotations': validation}

with open('val_dataset.json', 'w') as f:
    json.dump(validation_output, f)

with open('train_dataset.json', 'w') as f:
    json.dump(training_output, f)


# consider making all user input lowercase for consistency