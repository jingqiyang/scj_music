import pygame

# hard-coded hash of all key names : pygame key
# ripped from pygame website (converted with minor program i didn't push)
keys = {
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "e": pygame.K_e,
    "q": pygame.K_q,
    "r": pygame.K_r,
    "t": pygame.K_t,
    "u": pygame.K_u,
    "w": pygame.K_w,
    "y": pygame.K_y,
}

def get_key(key):
    if key in keys:
        return keys[key]
    else:
        return None
