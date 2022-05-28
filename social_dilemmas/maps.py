# Scheme heavily adapted from https://github.com/deepmind/pycolab/
# '@' means "wall"
# 'P' means "player" spawn point
# 'A' means apple spawn point
# ' ' is empty space

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
