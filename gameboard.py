import numpy as np


class PropertySpace():
    def __init__(self, name, base_value, mortgage_value, house_price,
                 hotel_price, base_rent, house_rents, hotel_rent, owned=False):
        self.name = name
        self.base_value = base_value
        self.mortgage_value = mortgage_value
        self.house_price = house_price
        self.hotel_price = hotel_price
        self.base_rent = base_rent
        self.house_rents = house_rents
        self.hotel_rent = hotel_rent
        self.owned = owned


class RailRoad():
    # NOTE: Need self. syntax for class attribute?
    multipliers = np.array([2, 4, 8])
    base_value = 200
    mortgage_value = 100
    base_rent = 25
    def __init__(self, name, owned=False):
        self.name = name
        self.owned = owned


class Utility():
    dice_multiplier = np.array([4, 10])
    base_value = 150
    mortgage_value = 75
    def __init__(self, name, owned=False):
        self.name = name
        self.owned = False


class Gameboard():
    def __init__(self, park_pool_amount=0, park_pool_bool=False):
        self.use_park_pool=park_pool_bool
        self.park_pool_amount=park_pool_amount
        self.houses = 9
        self.hotels = 10
        #NOTE: is the board attrib even necessary?
        self.board = np.array(['GO', 'MEDITERRANEAN AVENUE', 'COMMUNITY CHEST',
                               'BALTIC AVENUE', 'INCOME TAX', 
                               'READING RAILROAD', 'ORIENTAL AVENUE', 'CHANCE', 
                               'VERMONT AVENUE', 'CONNECTICUT AVENUE',
                               'JUST VISITING', 'IN JAIL', 'ST. CHARLES PLACE',
                               'ELECTRIC COMPANY', 'STATES AVENUE', 
                               'VIRGINIA AVENUE', 'PENNSYLVANIA RAILROAD', 
                               'ST. JAMES PLACE', 'COMMUNITY CHEST', 
                               'TENNESSEE AVENUE', 'NEW YORK AVENUE', 
                               'FREE PARKING', 'KENTUCKY AVENUE', 'CHANCE', 
                               'INDIANA AVENUE', 'ILLINOIS AVENUE',
                               'B. & O. RAILROAD', 'ATLANTIC AVENUE', 
                               'VENTNOR AVENUE', 'WATER WORKS', 
                               'MARVIN GARDENS', 'GO TO JAIL', 'PACIFIC AVENUE', 
                               'NORTH CAROLINA AVENUE', 'COMMUNITY CHEST',
                               'PENNSYLVANIA AVENUE', 'SHORT LINE', 'CHANCE', 
                               'PIKE PLACE', 'LUXURY TAX', 'BOARDWALK'])
        self.property_spaces = np.array([
                                PropertySpace('MEDITERRANEAN AVENUE', 
                                              60, 30, 50, 50, 2, 
                                              np.array([10, 30, 90, 160]), 
                                              250),
                                PropertySpace('BALTIC AVENUE', 60, 30, 50, 50,
                                              4, np.array([20, 60, 180, 320]),
                                              450),
                                PropertySpace('ORIENTAL AVENUE', 100, 50, 50, 
                                              50, 6, 
                                              np.array([30, 90, 270, 400]),
                                              550),
                                PropertySpace('VERMONT AVENUE', 100, 50, 50,
                                              50, 6,
                                              np.array([30, 90, 270, 400]),
                                              550),
                                PropertySpace('CONNECTICUT AVENUE', 120, 60, 
                                              50, 50, 8,
                                              np.array([40, 100, 300, 450]),
                                              600),
                                PropertySpace('ST. CHARLES PLACE', 140, 70,
                                              100, 100, 10,
                                              np.array([50, 150, 450, 625]),
                                              750),
                                PropertySpace('STATES AVENUE', 140, 70, 100, 
                                              100, 10, 
                                              np.array([50, 150, 450, 625]),
                                              750),
                                PropertySpace('VIRGINIA AVENUE', 160, 80, 100,
                                              100, 12,
                                              np.array([60, 180, 500, 700]),
                                              900),
                                PropertySpace('ST. JAMES PLACE', 180, 90, 100,
                                              100, 14,
                                              np.array([70, 200, 550, 750]),
                                              950),
                                PropertySpace('TENNESSEE AVENUE', 180, 90, 
                                              100, 100, 14,
                                              np.array([70, 200, 550, 750]),
                                              950),
                                PropertySpace('NEW YORK AVENUE', 200, 100, 
                                              100, 100, 16,
                                              np.array([80, 220, 600, 800]),
                                              1000),
                                PropertySpace('KENTUCKY AVENUE', 220, 110, 
                                              150, 150, 18,
                                              np.array([90, 250, 700, 875]),
                                              1050),
                                PropertySpace('INDIANA AVENUE', 220, 110, 150,
                                              150, 18,
                                              np.array([90, 250, 700, 875]),
                                              1050),
                                PropertySpace('ILLINOIS AVENUE', 240, 120, 150,
                                              150, 20,
                                              np.array([100, 300, 750, 925]),
                                              1100),
                                PropertySpace('ATLANTIC AVENUE', 260, 130, 150,
                                              150, 22,
                                              np.array([110, 330, 800, 975]),
                                              1150),
                                PropertySpace('VENTNOR AVENUE', 260, 150, 150,
                                              150, 22,
                                              np.array([110, 330, 800, 975]),
                                              1150),
                                PropertySpace('MARVIN GARDENS', 280, 140, 150,
                                              150, 24,
                                              np.array([120, 360, 850, 1025]),
                                              1200),
                                PropertySpace('PACIFIC AVENUE', 300, 150, 200,
                                              200, 26,
                                              np.array([130, 390, 900, 1100]),
                                              1275),
                                PropertySpace('NORTH CAROLINA AVENUE', 300, 150,
                                              200, 200, 26,
                                              np.array([130, 390, 900, 1100]),
                                              1275),
                                PropertySpace('PENNSYLVANIA AVENUE', 320, 160,
                                              200, 200, 28,
                                              np.array([150, 450, 1000, 1200]),
                                              1400),
                                PropertySpace('PARK PLACE', 350, 175, 200, 200,
                                              35,
                                              np.array([175, 500, 1100, 1300]),
                                              1500),
                                PropertySpace('BOARDWALK', 400, 200, 200, 200,
                                              50,
                                              np.array([200, 600, 1400, 1700]),
                                              2000)])
        self.railroads = np.array([RailRoad('READING RAILROAD'), 
                                   RailRoad('PENNSYLVANIA RAILROAD'),
                                   RailRoad('B. & O. RAILROAD'),
                                   RailRoad('SHORT LINE RAILROAD')])
        self.utilities = np.array([Utility('ELECTRIC COMPANY'), 
                                   Utility('WATER WORKS')])
        #TODO: decide whether comm chest and chance need aliases (aka implement
        # as map)
        self.comunity_chest_cards = np.array(['''YOU HAVE WON SECOND PRIZE IN A BEATUY CONTEST: 
                            COLLECT $100''', '''ADVANCE TO GO (COLLECT $200)''',
                            '''PAY SCHOOL TAX OF$150''', '''FROM SALE OF STOCK 
                            YOU GET $45''', '''LIFE INSURANCE MATURES: COLLECT
                            $100''', '''GRAND OPERA OPENING: COLLECT $50 FROM
                            EVERY PLAYER FOR OPENING NIGHT SEATS''', 
                            '''DOCTOR'S FEE: PAY $50''', '''INCOME TAX REFUND: 
                            COLLECT $200''', '''BANK ERROR IN YOUR FAVOR:
                            COLLECT $200''', '''PAY HOSPITAL $100''', '''XMAS
                            FUND MATURES: COLLECT $100''', '''YOU ARE ASSESSED 
                            FOR STREET REPAIRS: $40 PER HOUSE, $115 PER
                            HOTEL''', '''GET OUT OF JAIL FREE (THIS CARD MAY BE
                            KEPT UNTIL NEEDED OR SOLD)''', '''YOU INHERIT
                            $100''', '''GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT
                            PASS GO. DO NOT COLLECT $200''', '''RECEIVE $25
                            FOR SERVICES'''])
        self.chance_cards = np.array(['''ADVANCE TOKEN TO THE NEAREST RAILROAD AND PAY OWNER TWICE
                   THE RENTAL TO WHICH THEY ARE OTHERWISE ENTITLED. IF RAILROAD
                   IS UNOWNED YOU MAY BUY IT FROM THE BANK''', '''TAKE A WALK
                   ON THE BOARDWALK. ADVANCE TOKEN TO BOARDWALK''', '''ADVANCE
                   TO ST. CHARLES PLACE. IF YOU PASS GO COLLECT $200''',
                   '''YOUR BUILDING AND LOAN MATURES: COLLECT $150''' ,
                   '''ADVANCE TO GO (COLLECT $200)''', '''BANK PAYS YOU
                   DIVIDEND OF $50''', '''GO DIRECTLY TO JAIL. DO NOT PASS GO.
                   DO NOT COLLECT $200''', '''TAKE A RIDE ON THE READING. IF
                   YOU PASS GO COLLECT $200''', '''YOU HAVE BEEN ELECTED
                   CHAIRMAN OF THE BOARD. PAY EACH PLAYER $50''', '''ADVANCE TO
                   ILLINOIS AVE.''', '''MAKE GENERAL REPAIRS ON ALL YOUR
                   PROPERTY. FOR EACH HOUSE PAY $25. FOR EACH HOTEL %100''',
                   '''ADVANCE TOKEN TO NEAREST UTILITY. IF UNOWNED YOU MAY BUY
                   IT FROM THE BANK. IF OWNED THROW DICE AND PAY OWNER A TOTAL
                   TEN TIMES THE AMOUNT THROWN.''', '''GO BACK 3 SPACES'''])
        
