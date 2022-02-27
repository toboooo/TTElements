import socket, random, time

headersize = 10

class Player:
    """A class to represent the players of the game."""
    
    def __init__(self, name, conn, index):
        self.name = name
        self.conn = conn
        self.index = index
        self.elements = []


class Game:
    def __init__(self, num_players):
        """Initialise."""
        self.num_players = num_players
        self.elements = ['Hydrogen', 'Helium', 'Lithium', 'Boron',
                 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',
                 'Neon', 'Sodium', 'Magnesium', 'Aluminium',
                 'Silicon', 'Phosphorus', 'Sulphur', 'Chlorine',
                 'Potassium', 'Calcium', 'Iron', 'Copper',
                 'Arsenic', 'Bromine', 'Silver', 'Cadmium',
                 'Caesium', 'Europium', 'Osmium', 'Gold',
                 'Mercury', 'Lead']
        self.symbols = {'Hydrogen': 'H 1', 'Helium': 'He 2', 'Lithium': 'Li 3',
                               'Boron': 'B 5',
                 'Carbon': 'C 6', 'Nitrogen': 'N 7', 'Oxygen': 'O 8',
                               'Fluorine': 'F 9',
                 'Neon': 'Ne 10', 'Sodium': 'Na 11', 'Magnesium': 'Mg 12',
                        'Aluminium': 'Al 13',
                 'Silicon': 'Si 14', 'Phosphorus': 'P 15', 'Sulphur': 'S 16',
                               'Chlorine': 'Cl 17',
                 'Potassium': 'K 19', 'Calcium': 'Ca 20', 'Iron': 'Fe 26',
                        'Copper': 'Cu 29',
                 'Arsenic': 'As 33', 'Bromine': 'Br 35', 'Silver': 'Ag 47',
                        'Cadmium': 'Cd 48',
                 'Caesium': 'Cs 55', 'Europium': 'Eu 63', 'Osmium': 'Os 76',
                        'Gold': 'Au 79',
                 'Mercury': 'Hg 80', 'Lead': 'Pb 84'}
        self.melting_points = {'Hydrogen': -259, 'Helium': -271, 'Lithium': 181,
                               'Boron': 2077,
                 'Carbon': 4489, 'Nitrogen': -210, 'Oxygen': -219,
                               'Fluorine': -220,
                 'Neon': -249, 'Sodium': 98, 'Magnesium': 650, 'Aluminium': 660,
                 'Silicon': 1414, 'Phosphorus': 579, 'Sulphur': 115,
                               'Chlorine': -102,
                 'Potassium': 64, 'Calcium': 842, 'Iron': 1538, 'Copper': 1085,
                 'Arsenic': 817, 'Bromine': -7, 'Silver': 962, 'Cadmium': 321,
                 'Caesium': 29, 'Europium': 822, 'Osmium': 3033, 'Gold': 1064,
                 'Mercury': -39, 'Lead': 327}
        self.densities = {'Hydrogen': 0.1, 'Helium': 0.2, 'Lithium': 534,
                        'Boron': 2340,
                 'Carbon': 2260, 'Nitrogen': 1.1, 'Oxygen': 1.3,
                        'Fluorine': 1.6,
                 'Neon': 0.8, 'Sodium': 971, 'Magnesium': 1738,
                        'Aluminium': 2698,
                 'Silicon': 2329, 'Phosphorus': 2200, 'Sulphur': 2070,
                        'Chlorine': 2.9,
                 'Potassium': 862, 'Calcium': 1550, 'Iron': 7874,
                        'Copper': 8960,
                 'Arsenic': 5780, 'Bromine': 3122, 'Silver': 10500,
                        'Cadmium': 8650,
                 'Caesium': 1873, 'Europium': 5243, 'Osmium': 22590,
                        'Gold': 19320,
                 'Mercury': 13546, 'Lead': 11350}
        self.prices = {'Hydrogen': 68, 'Helium': 48, 'Lithium': 110,
                      'Boron': 150,
                 'Carbon': 1.2, 'Nitrogen': 13, 'Oxygen': 7.6, 'Fluorine': 99,
                 'Neon': 140, 'Sodium': 7, 'Magnesium': 3.3, 'Aluminium': 2.6,
                 'Silicon': 16, 'Phosphorus': 5.3, 'Sulphur': 1.3,
                      'Chlorine': 18,
                 'Potassium': 190, 'Calcium': 20, 'Iron': 1.9, 'Copper': 4.7,
                 'Arsenic': 11000, 'Bromine': 2.6, 'Silver': 310, 'Cadmium': 24,
                 'Caesium': 3400, 'Europium': 15000, 'Osmium': 16000,
                      'Gold': 8600,
                 'Mercury': 11, 'Lead': 2.6}
        self.discovery_dates = {'Hydrogen': 1766, 'Helium': 1895,
                               'Lithium': 1817, 'Boron': 1808,
                 'Carbon': -30000, 'Nitrogen': 1772, 'Oxygen': 1774,
                               'Fluorine': 1886,
                 'Neon': 1898, 'Sodium': 1807, 'Magnesium': 1755,
                               'Aluminium': 1825,
                 'Silicon': 1824, 'Phosphorus': 1669, 'Sulphur': -2000,
                               'Chlorine': 1774,
                 'Potassium': 1807, 'Calcium': 1808, 'Iron': -2500,
                               'Copper': -9000,
                 'Arsenic': 1250, 'Bromine': 1826, 'Silver': -3000,
                               'Cadmium': 1817,
                 'Caesium': 1860, 'Europium': 1901, 'Osmium': 1803,
                               'Gold': -3000,
                 'Mercury': -1500, 'Lead': -1000}
        self.atom_sizes = {'Hydrogen': 220, 'Helium': 280, 'Lithium': 364,
                          'Boron': 384,
                 'Carbon': 340, 'Nitrogen': 310, 'Oxygen': 304, 'Fluorine': 294,
                 'Neon': 308, 'Sodium': 454, 'Magnesium': 346, 'Aluminium': 368,
                 'Silicon': 420, 'Phosphorus': 360, 'Sulphur': 360,
                          'Chlorine': 350,
                 'Potassium': 550, 'Calcium': 462, 'Iron': 408, 'Copper': 392,
                 'Arsenic': 370, 'Bromine': 370, 'Silver': 422, 'Cadmium': 436,
                 'Caesium': 686, 'Europium': 470, 'Osmium': 432, 'Gold': 428,
                 'Mercury': 446, 'Lead': 404}
        self.categories = {'mel': self.melting_points, 'den': self.densities,
                           'pri': self.prices, 'dis': self.discovery_dates,
                           'siz': self.atom_sizes}
        self.category_names = {'mel': 'Melting Point', 'den': 'Density',
                           'pri': 'Price', 'dis': 'Discovery Date',
                           'siz': 'Size of Atom'}

    def make_card(self, element):
        """For a given element, make a string of the top trumps data."""
        if element in self.elements:
            card = '-' * 32 + '\n' +\
                  element + ' ' + self.symbols[element] +\
                  '\n\nMelting Point (oC)\t' +\
                  str(self.melting_points[element]) + '\nDensity (kg/m^3)\t' +\
                  str(self.densities[element]) + '\nPrice (per 100g)\t£' +\
                  str(self.prices[element]) + '\nDiscovery Date\t\t' +\
                  str(self.discovery_dates[element]) +\
                  '\nSize of Atom (pm)\t' + str(self.atom_sizes[element]) +\
                  '\n' + '-' * 32 + '\n'
        return card

    def deal_elements(self, players):
        elements_list = self.elements.copy()
        random.shuffle(elements_list)
        for i in range(len(elements_list)):
            players['active'][i%self.num_players].elements\
                                                 .append(elements_list[i])

    def send_msg(self, content, conn):
        msg = f'{len(content):<{headersize}}' + content
        conn.send(bytes(msg, 'utf-8'))

    def send_to_all(self, content, players):
        for player in players:
            self.send_msg(content, player.conn)

    def recv_msg(self, conn):
        header = conn.recv(headersize)
        msg_len = int(header.decode())
        msg = conn.recv(msg_len)
        return msg.decode()

    def run(self, port):
        """Handle connections and play the game."""
        s = socket.socket()
        s.bind((socket.gethostname(), port))
        s.listen(self.num_players)
        players = {'active': [], 'eliminated': []}
        index = 0
        while True:
            conn, addr = s.accept()
            self.send_msg('Connected to TTElements. Please enter your name:',\
                                                                        conn)
            name = self.recv_msg(conn)
            self.send_msg('Please wait for other players to connect.', conn)
            player = Player(name, conn, index)
            players['active'].append(player)
            index += 1
            if len(players['active']) == self.num_players:
                break
        
        self.deal_elements(players)
        self.send_to_all("When it is your turn enter 'melting point', " +\
                         "'density', 'price', 'discovery date' or 'size' to " +\
                         "choose a category.", players['active'])

        time.sleep(3)
        # Give one player the turn.
        turn_player = random.choice(players['active'])

        element_pot = []

        while True:
            current_elements = []
            time.sleep(1)
            
            # Show each active player their top card.
            for player in players['active']:
                card = self.make_card(player.elements[0])
                # Send a "this is a card" message to the player.
                self.send_msg('card', player.conn)
                self.send_msg(card, player.conn)
                while True:
                    msg = self.recv_msg(player.conn)
                    try:
                        if msg == 'card received':
                            break
                    except ValueError:
                        continue

            # Send a wait message to all other players.            
            for player in players['active']:
                if player != turn_player:
                    self.send_msg('wait', player.conn)
                    wait_confirmation = self.recv_msg(player.conn)
                    if wait_confirmation == 'wait received':
                        self.send_msg(f'Waiting for {turn_player.name}...',\
                                  player.conn)

            # Get the category from the turn player.
            self.send_msg('request', turn_player.conn)
            while True:
                category = self.recv_msg(turn_player.conn)
                if category[:3] in self.categories.keys():
                    break
            category = category[:3].lower()

            # Send a message to other players saying which category
            # turn_player has chosen and with what value.
            for player in players['active']+players['eliminated']:
                if player != turn_player:
                    self.send_msg('turn choice', player.conn)
                    self.send_msg(f'{turn_player.name} has chosen ' +\
                                  f'"{self.category_names[category]}" ' +\
                                  f'of {turn_player.elements[0]} with ' +\
                                  f'value ' +\
                       f'{self.categories[category][turn_player.elements[0]]}',\
                                  player.conn)

            # Pause for effect
            time.sleep(2)
           
            for player in players['active']:
                current_elements.append([player, player.elements[0]])

            # Append the category value of each element to each player's
            # current_elements list.
            for element in current_elements:
                element.append(self.categories[category][element[1]])

            # Sort the category values in the list of lists current_elements.
            current_elements.sort(key=lambda x: x[2], reverse=True)

            # Need to account for draws.
            if current_elements[0][2] == current_elements[1][2]:
                self.send_to_all('result', players['active']+players['eliminated'])
                self.send_to_all(f'{current_elements[0][0].name} and ' +\
                    f'{current_elements[1][0].name} have tied with ' +\
                    f'{current_elements[0][1]} and {current_elements[1][1]}',\
                                 players['active']+players['eliminated'])
                element_pot = [current_elements[i][0].elements.pop(0) \
                               for i in range(len(current_elements))]
                
                if turn_player not in [current_elements[0][0],
                                       current_elements[1][0]]:
                    turn_player = random.choice([current_elements[0][0],
                                                 current_elements[1][0]])

                time.sleep(0.5)

                for player in players['active']:
                    if len(player.elements) == 0:
                        players['eliminated'].append(player)
                        players['active'].remove(player)
                        self.send_msg('eliminated', player.conn)
                        
                # Let each player know how many cards they have left.
                for player in players['active']:
                    self.send_msg('result', player.conn)
                    self.send_msg(f'You have {len(player.elements)} elements', player.conn)

                if len(players['active']) == 1:
                    self.send_to_all('winner', players['active'])
                    break

            elif current_elements[0][2] == current_elements[1][2] ==\
                 current_elements[2][2]:
                self.send_to_all('result', players['active']+players['eliminated'])
                self.send_to_all(f'{current_elements[0][0].name}, ' +\
                    f'{current_elements[1][0].name} and ' +\
                    f'{current_elements[2][0].name} have tied with elements '+\
                    f'{current_elements[0][1]}, {current_elements[1][1]} and '+\
                    f'{current_elements[2][1]}', players['active']+players['eliminated'])
                element_pot = [current_elements[i][0].elements.pop(0) \
                               for i in range(len(current_elements))]
                
                if turn_player not in [current_elements[0][0],
                                       current_elements[1][0],
                                       current_elements[2][0]]:
                    turn_player = random.choice([current_elements[0][0],
                                                 current_elements[1][0],
                                                 current_elements[2][0]])

                time.sleep(0.5)

                for player in players['active']:
                    if len(player.elements) == 0:
                        players['eliminated'].append(player)
                        players['active'].remove(player)
                        self.send_msg('eliminated', player.conn)
                
                # Let each player know how many cards they have left.
                for player in players['active']:
                    self.send_msg('result', player.conn)
                    self.send_msg(f'You have {len(player.elements)} elements', player.conn)

                if len(players['active']) == 1:
                    self.send_to_all('winner', players['active'])
                    break
                
            else:
                winning_player = current_elements[0][0]
                # Send message to all players saying the winner.
                self.send_to_all('result', players['active']+players['eliminated'])
                self.send_to_all(f'{winning_player.name} has won with ' +\
                                 f'{winning_player.elements[0]}, ' +\
                                 f'{self.category_names[category]} = ' +\
                    f'{self.categories[category][winning_player.elements[0]]}',\
                                 players['active']+players['eliminated'])
                
                # Tell the winning player which elements they've won.
                self.send_msg('result', winning_player.conn)
                element_string = ''
                for element in current_elements[1:]:
                    element_string += element[1] + ' '
                self.send_msg(f'You have won the elements: {element_string}', winning_player.conn)

                time.sleep(0.5)
                
                # Move the first elements in each player's list to the back of
                # that of the winner.
                for player in players['active']:
                    # Make sure the winning player doesn't get their last card back.
                    if player != winning_player:
                        winning_player.elements.append(player.elements.pop(0))
                    # Eliminate any players without any cards.
                    if len(player.elements) == 0:
                        players['eliminated'].append(player)
                        players['active'].remove(player)
                        self.send_msg('eliminated', player.conn)
                
                # Give any tied cards to the winner.
                if element_pot != []:
                    self.send_msg('result', winning_player.conn)
                    element_string = ''
                    for element in element_pot:
                        element_string += element + ' '
                    self.send_msg(f'You have also received the elements: {element_string}from the tie', winning_player.conn)
                    for element in element_pot:
                        winning_player.elements.append(element)
                        element_pot = []
                        
                # Move the winning player's top card to the back of their deck.
                winning_player.elements.append(winning_player.elements.pop(0))

                # If there is only one player left, send a win message to all
                # the active players (which is just the winner)
                if len(players['active']) == 1:
                    self.send_to_all('winner', players['active'])
                    break
                    
                time.sleep(1)
                
                # Let each player know how many cards they have left.
                for player in players['active']:
                    self.send_msg('result', player.conn)
                    self.send_msg(f'You have {len(player.elements)} elements', player.conn)
                
                # The winning player has the turn.
                turn_player = winning_player

                
n_players = input('Number of players: ')
game = Game(int(n_players))
game.run(5555)
