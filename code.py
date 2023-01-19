#!/usr/bin/env python3

# Created by: Jeremiah omoike
# Created on: Dec. 12, 2022
# This program displays a playable space alien game on a  PyBadge

import ugame
import stage

import constants
import time
import random
import supervisor
def splash_scene():
    # this is a splash scene
    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    #image bank for the pybadge
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
   # text that is to be shown in splash scene
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 110)
    text1.text("JJ Traps studios")
    text.append(text1)

    #set the background to image 0 in the image bank and the size (10x8 tiles of size 16)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # used this program to split the game into tiles:
    background.tile(2, 2, 0)
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)

    background.tile(2, 3, 0)
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)

    background.tile(2, 4, 0)
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)

    background.tile(2, 5, 0)
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)


    #set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = text + [background]
    #render all sprites
    game.render_block()

    #repeat forever game loop
    while True:
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # main menu scene
    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    #image bank for the pybadge
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # buttons to keep state info in
    start_button = constants.button_state["button_up"]
    # text that is to be shown in menu scene
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Space alien game")
    text.append(text1)
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(30, 60)
    text2.text("Press Start")
    text.append(text2)

    #set the background to image 0 in the image bank and the size (10x8 tiles of size 16)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    #set the frame rate to 60 fps
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
            if start_button == constants.button_state["button_up"]:
                start_button = constants.button_state["button_just_pressed"]
            elif start_button == constants.button_state["button_just_pressed"]:
                start_button = constants.button_state["button_still_pressed"]
        else:
            if start_button == constants.button_state["button_still_pressed"]:
                start_button = constants.button_state["button_released"]
            else:
                start_button = constants.button_state["button_up"]
    # play the coin sound if the a button is pressed
        if start_button == constants.button_state["button_just_pressed"]:
            sound.play(coin_sound)
            game_scene()
        game.tick()

def game_scene():
    # for score
    score = 0

    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))
    # game scene
    def show_alien():
        for alien_number in range(len(alien)):
            if alien[alien_number].x < 0:
                alien[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                       constants.SCREEN_X - constants.SPRITE_SIZE),
                                         constants.OFF_TOP_SCREEN)
                break

    #image bank for the pybadge
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # buttons to keep state info in
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # sound bank for the pybadge game
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
#set the background to image 0 in the image bank and the size (10x8 tiles of size 16)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    #my sprites
    ship = stage.Sprite(image_bank_sprites, 4, 75, 110)
    # enemy aliens
    alien = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        alien.append(a_single_alien)
    # place one alien
    show_alien()

    # lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    #create a stage for the background to show on
    #and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = [score_text] + lasers + [ship] + alien + [background]
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
        # fire laser if we have not used all of them
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # each frame moves the lasers that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                          constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
        # each frame moves the aliens down, that are on screen
        for alien_number in range(len(alien)):
            if alien[alien_number].x > 0:
                alien[alien_number].move(alien[alien_number].x,
                                          alien[alien_number].y +
                                          constants.ALIEN_SPEED)
                if alien[alien_number].y > constants.SCREEN_Y:
                    alien[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))
        # check if any of the lasers are touching any of the aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(alien)):
                    if alien[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         alien[alien_number].x + 1, alien[alien_number].y,
                                         alien[alien_number].x + 15, alien[alien_number].y + 15):
                            # when a laser hits an enemy
                            alien[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))
        for alien_number in range(len(alien)):
            if alien[alien_number].x > 0:
                if stage.collide(alien[alien_number].x + 1, alien[alien_number].y,
                                 alien[alien_number].x + 15,alien[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    #alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)
        # refreshes the sprite every 1 60th of a second to maintain the 60 fps refresh rate
        game.render_sprites(lasers + [ship] + alien)
        game.tick()

def game_over_scene(final_score):
    # This is the game over scene
    # image banks for circuit python
    image_bank_2 = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    # add text object
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text = []
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text = []
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the background to show up on 
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set layers so that text will shou on top of background
    game.layers = text + [background]
    #render the background and initial location of sprite list
    game.render_block()
    #repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # Select button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

    # update game logic
        game.tick()# wait until rate finishes



if __name__ == "__main__":
       splash_scene()

 