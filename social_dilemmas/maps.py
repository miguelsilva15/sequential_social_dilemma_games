# Scheme heavily adapted from https://github.com/deepmind/pycolab/
# '@' means "wall"
# 'P' means "player" spawn point
# 'A' means apple spawn point
# ' ' is empty space

APPLE_AGENT_POSITON = [(6, 12), (5, 6), (10, 5), (9, 10), (12, 9), (5, 12), (7, 5), (8, 12), (5, 9), (13, 6)]
ORANGE_AGENT_POSITON = [(12, 4), (10, 9), (4, 11), (10, 6), (10, 8), (9, 7), (8, 4), (8, 5), (6, 11), (7, 7)]
APPLE_RESOURCE_POSITION = [(8, 6), (11, 5), (12, 6), (11, 6), (11, 4), (4, 10), (11, 7), (12, 5), (6, 7), (13, 4)]

NORMAL_HARVEST = [
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@OOAP  A  A         AA               @',
    '@  A   OOO O O    O A L  A         A @',
    '@   P    O A O           A    A O    @',
    '@  A  A A      A   O     A      O   A@',
    '@ OO              O     A            @',
    '@L O  A  O PL   A  A O    A    P    P@',
    '@     OO A    OOOLO   A AO     L     @',
    '@ A      O   O OA O O  OA    O   A   @',
    '@    O            O  LO O           P@',
    '@ O AAA            AA         A    O @',
    '@     A AAO  A A L       O   A P   P @',
    '@O P      A A O A    O               @',
    '@    O    OL       O   O      LA     @',
    '@  A           OA   A OAAO  A LOOA   @',
    '@               O A O        P   A   @',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
 ]
BIGGEST_HARVEST =[
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@           A    A                   @@@@',
    '@@@@   O                   A            @@@@',
    '@@@@      POP       O A          L      @@@@',
    '@@@@  P                   O         A   @@@@',
    '@@@@             A  P     O             @@@@',
    '@@@@                  P            A    @@@@',
    '@@@@    A   A       O  A                @@@@',
    '@@@@              L    L L L            @@@@',
    '@@@@                           A A      @@@@',
    '@@@@         P       P  O           O  O@@@@',
    '@@@@        A O        L          O     @@@@',
    '@@@@      O         L          P        @@@@',
    '@@@@         P           P O            @@@@',
    '@@@@     L           L  O       A       @@@@',
    '@@@@        OA    L                     @@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    ]

BATTLE_MAP = [
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@   AAAAA   @@@@',
    '@@@@    AAA    @@@@',
    '@@@@   AAAAA   @@@@',
    '@@@@    AAA    @@@@',
    '@@@@     A     @@@@', 
    '@@@@           @@@@',
    '@@@@           @@@@',
    '@@@@           @@@@',
    '@@@@           @@@@',
    '@@@@ P L       @@@@',
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@',
    '@@@@@@@@@@@@@@@@@@@',
    ]


HARVEST_MAP = [
    "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
    "@ P   P  L   A    P AAAOO    P  A P  @",
    "@  P   L A P AA    P  L AAAO   A  A  @",
    "@    OA AAA  AAO    A L  A AA OAAAO  @",
    "@ A  OAA A    A  A AAA  A  A   A A   @",
    "@AAA  A A  L A  OAA A  AOO   L    A P@",
    "@ A A  AAA  AOO  A A    A AAO  AA AA @",
    "@L A A  AAO    A A  AAA L  AAA  A    @",
    "@   AAA  A  L   AAA  A    OAAA  L    @",
    "@ P  A  OOO  A  A AOA L  A  A      P @",
    "@A  OOO  A  A  AAA A    AAOO  L  P   @",
    "@    A A   AAA  A A  L   A AA   A  P @",
    "@    OOAA   A A  AAOO     AA   OAA P @",
    "@ A L  A    OAAA  A  P    L     A    @",
    "@ L     P   OOA    L    P  P P     P @",
    "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
]

CLEANUP_MAP = [
    "@@@@@@@@@@@@@@@@@@",
    "@RRRRRR     BBBBB@",
    "@HHHHHH      BBBB@",
    "@RRRRRR     BBBBB@",
    "@RRRRR  P    BBBB@",
    "@RRRRR    P BBBBB@",
    "@HHHHH       BBBB@",
    "@RRRRR      BBBBB@",
    "@HHHHHHSSSSSSBBBB@",
    "@HHHHHHSSSSSSBBBB@",
    "@RRRRR   P P BBBB@",
    "@HHHHH   P  BBBBB@",
    "@RRRRRR    P BBBB@",
    "@HHHHHH P   BBBBB@",
    "@RRRRR       BBBB@",
    "@HHHH    P  BBBBB@",
    "@RRRRR       BBBB@",
    "@HHHHH  P P BBBBB@",
    "@RRRRR       BBBB@",
    "@HHHH       BBBBB@",
    "@RRRRR       BBBB@",
    "@HHHHH      BBBBB@",
    "@RRRRR       BBBB@",
    "@HHHH       BBBBB@",
    "@@@@@@@@@@@@@@@@@@",
]


# 'S' means turned-on switch
# 's' means turned-off switch
# 'D' means closed door
# 'd' means opened door
class SwitchMapElements:
    top_row = "@@@D@@@"
    empty_row = "@     @"
    one_switch_row = "@s    @"
    two_switch_row = "@s   s@"
    bottom_row = "@@@@@@@"
