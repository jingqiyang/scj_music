import pygame

# hard-coded hash of all key names : pygame key
# ripped from pygame website (converted with minor program i didn't push)
keys = {
    "\b": pygame.K_BACKSPACE,
    "\t": pygame.K_TAB,
    "clear": pygame.K_CLEAR,
    "\r": pygame.K_RETURN,
    "pause": pygame.K_PAUSE,
    "^[": pygame.K_ESCAPE,
    "space": pygame.K_SPACE,
    "!": pygame.K_EXCLAIM,
    "\"": pygame.K_QUOTEDBL,
    "#": pygame.K_HASH,
    "$": pygame.K_DOLLAR,
    "&": pygame.K_AMPERSAND,
    "quote": pygame.K_QUOTE,
    "(": pygame.K_LEFTPAREN,
    ")": pygame.K_RIGHTPAREN,
    "*": pygame.K_ASTERISK,
    "+": pygame.K_PLUS,
    ",": pygame.K_COMMA,
    "-": pygame.K_MINUS,
    ".": pygame.K_PERIOD,
    "/": pygame.K_SLASH,
    "0": pygame.K_0,
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9,
    ":": pygame.K_COLON,
    ";": pygame.K_SEMICOLON,
    "<": pygame.K_LESS,
    "=": pygame.K_EQUALS,
    ">": pygame.K_GREATER,
    "?": pygame.K_QUESTION,
    "@": pygame.K_AT,
    "[": pygame.K_LEFTBRACKET,
    "\\": pygame.K_BACKSLASH,
    "]": pygame.K_RIGHTBRACKET,
    "^": pygame.K_CARET,
    "_": pygame.K_UNDERSCORE,
    "`": pygame.K_BACKQUOTE,
    "a": pygame.K_a,
    "b": pygame.K_b,
    "c": pygame.K_c,
    "d": pygame.K_d,
    "e": pygame.K_e,
    "f": pygame.K_f,
    "g": pygame.K_g,
    "h": pygame.K_h,
    "i": pygame.K_i,
    "j": pygame.K_j,
    "k": pygame.K_k,
    "l": pygame.K_l,
    "m": pygame.K_m,
    "n": pygame.K_n,
    "o": pygame.K_o,
    "p": pygame.K_p,
    "q": pygame.K_q,
    "r": pygame.K_r,
    "s": pygame.K_s,
    "t": pygame.K_t,
    "u": pygame.K_u,
    "v": pygame.K_v,
    "w": pygame.K_w,
    "x": pygame.K_x,
    "y": pygame.K_y,
    "z": pygame.K_z,
    "delete": pygame.K_DELETE,
    "keypad": pygame.K_KP0,
    "keypad": pygame.K_KP1,
    "keypad": pygame.K_KP2,
    "keypad": pygame.K_KP3,
    "keypad": pygame.K_KP4,
    "keypad": pygame.K_KP5,
    "keypad": pygame.K_KP6,
    "keypad": pygame.K_KP7,
    "keypad": pygame.K_KP8,
    "keypad": pygame.K_KP9,
    ".": pygame.K_KP_PERIOD,
    "/": pygame.K_KP_DIVIDE,
    "*": pygame.K_KP_MULTIPLY,
    "-": pygame.K_KP_MINUS,
    "+": pygame.K_KP_PLUS,
    "\r": pygame.K_KP_ENTER,
    "=": pygame.K_KP_EQUALS,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "right": pygame.K_RIGHT,
    "left": pygame.K_LEFT,
    "insert": pygame.K_INSERT,
    "home": pygame.K_HOME,
    "end": pygame.K_END,
    "page": pygame.K_PAGEUP,
    "page": pygame.K_PAGEDOWN,
    "F1": pygame.K_F1,
    "F2": pygame.K_F2,
    "F3": pygame.K_F3,
    "F4": pygame.K_F4,
    "F5": pygame.K_F5,
    "F6": pygame.K_F6,
    "F7": pygame.K_F7,
    "F8": pygame.K_F8,
    "F9": pygame.K_F9,
    "F10": pygame.K_F10,
    "F11": pygame.K_F11,
    "F12": pygame.K_F12,
    "F13": pygame.K_F13,
    "F14": pygame.K_F14,
    "F15": pygame.K_F15,
    "numlock": pygame.K_NUMLOCK,
    "capslock": pygame.K_CAPSLOCK,
    "scrollock": pygame.K_SCROLLOCK,
    "right": pygame.K_RSHIFT,
    "left": pygame.K_LSHIFT,
    "right": pygame.K_RCTRL,
    "left": pygame.K_LCTRL,
    "right": pygame.K_RALT,
    "left": pygame.K_LALT,
    "right": pygame.K_RMETA,
    "left": pygame.K_LMETA,
    "left": pygame.K_LSUPER,
    "right": pygame.K_RSUPER,
    "mode": pygame.K_MODE,
    "help": pygame.K_HELP,
    "print": pygame.K_PRINT,
    "sysrq": pygame.K_SYSREQ,
    "break": pygame.K_BREAK,
    "menu": pygame.K_MENU,
    "power": pygame.K_POWER,
    "Euro": pygame.K_EURO
}

def get_key(key):
    return keys[key]
