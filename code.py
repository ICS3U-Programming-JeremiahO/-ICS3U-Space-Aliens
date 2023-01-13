#!/usr/bin/env python3

# Created by: Jeremiah omoike
# Created on: Dec. 12, 2022
# This program displays a playable space alien game on a  PyBadge

import ugame
import stage

import constants

def menu_scene():
    # main menu scene 

    #image bank for the pybadge
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("JJ Traps studios")
    text.append(text1)
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(30, 60)
    text2.text("Space alien game")
    text.append(text2)
    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(40, 110)
    text3.text("Press start")
    text.append(text3)
#set the background to image 0 in the image bank and the size (10x8 tiles of size 16)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    #create a stage for the background to show on
    #and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = text + [background]
    #render all sprites
    game.render_block()

    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()


        if keys & ugame.K_START:
            game_scene()



        game.tick()

def game_scene():
    # game scene 

    #image bank for the pybadge
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")
    # buttons to keep state info in 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # sound bank for the pybadge game
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
#set the background to image 0 in the image bank and the size (10x8 tiles of size 16)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    #my sprite 
    ship = stage.Sprite(image_bank_sprite, 5, 75, 66)

    #create a stage for the background to show on
    #and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = [ship]+[background]
    #render all sprites
    game.render_block()

    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()

       #A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B button has not been set yet 
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        #input to make the sprite move
        # if right button is pressed the sprites moves to the right + 1

        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
        # catch to make sure that the sprite cannot go past its boundaries
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # if right button is pressed the sprites moves to the left - 1
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
        # catch to make sure that the sprite cannot go past its boundaries
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
 
 
        #update game logic
        # refreshes the sprite forever ( forever loop)
        # play the pew sound if the a button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # refreshes the sprite every 1 60th of a second to maintain the 60 fps refresh rate
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
       menu_scene()
 
 

