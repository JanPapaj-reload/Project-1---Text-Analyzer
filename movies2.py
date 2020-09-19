
films_dictionary = [
{'NAME': 'Shawshank Redemption', 'RATING': '93/100', 'YEAR': 1994, 'DIRECTOR': 'Frank Darabont', 'LENGTH': 144, 'ACTORS': ('Tim Robbins', 'Morgan Freeman', 'Bob Gunton', 'William Sadler', 'Clancy Brown', 'Gil Bellows', 'Mark Rolston', 'James Whitmore', 'Jeffrey DeMunn', 'Larry Brandenburg')},
{'NAME': 'The Godfather', 'RATING': '92/100', 'YEAR': 1972, 'DIRECTOR': 'Francis Ford Coppola', 'LENGTH': 175, 'ACTORS': ('Marlon Brando', 'Al Pacino', 'James Caan', 'Richard S. Castellano', 'Robert Duvall', 'Sterling Hayden', 'John Marley', 'Richard Conte')},
{'NAME': 'The Dark Knight', 'RATING': '90/100', 'YEAR': 2008, 'DIRECTOR': 'Christopher Nolan', 'LENGTH': 152, 'ACTORS': ('Christian Bale', 'Heath Ledger', 'Aaron Eckhart', 'Michael Caine', 'Maggie Gyllenhaal', 'Gary Oldman', 'Morgan Freeman', 'Monique Gabriela', 'Ron Dean', 'Cillian Murphy')},
{'NAME': 'The Prestige', 'RATING': '85/100', 'YEAR': 2006, 'DIRECTOR': 'Christopher Nolan', 'LENGTH': 130, 'ACTORS': ('Hugh Jackman', 'Christian Bale', 'Michael Caine', 'Piper Perabo', 'Rebecca Hall', 'Scarlett Johansson', 'Samantha Mahurin', 'David Bowie')},
]

selected_film = input("Which film from our database are you after? ")
if selected_film == "Shawshank Redemption":
    print("The following are the film's details:", films_dictionary[0])
elif selected_film == "The Godfather":
    print("The following are the film's details:", films_dictionary[1])
elif selected_film == "The Dark Knight":
    print("The following are the film's details:", films_dictionary[2])
else:
    print("The following are the film's details:", films_dictionary[3]

