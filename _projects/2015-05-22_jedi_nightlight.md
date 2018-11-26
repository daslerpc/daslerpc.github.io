---
title: "Jedi Nightlight"
collection: projects
subcategory: complete
classes: wide
header: 
  teaser: /assets/images/projects/2015-05-22_jedi_nightlight.png
date: 2015-05-22
---

An interactive 3D printed nighlight that reveals a hidden pattern when turned over.



The 3D model (created in 123D Design) for this project can be found on [Thingiverse](http://www.google.com).
Instructions for building this light can be found at [Instructables](http://www.google.com).

## Overview
This nightlight appears, at first, to be nothing but a simple cube. Written on one side is the word "Off" and on the other is, as one might expect, is the word "On". By turning the cube upside down, you activate the light inside and reveal the cubes secret!

sw_off.jpgsw_lit2.jpg
Hidden within the cube are the emblems of four factions from the Star Wars universe. These emblems are inset on the inside faces of the four side panels of the cube, making the plastic thinner and allowing the light to shine through.sw_inside.jpg

A simple circuit consisting mainly of a tilt switch and four LEDs is all there is to this simple nightlight.sw_mounted_circuit.jpg


## Materials and Parts
| Part |  The Part's Role |  Count  |  Cost  |  Total Cost  |
|---|---|---|---|---|
3D Printing Filament, PLA | Used for printing the case of the nightlight | 132 | $0.20/gram | $26.40
[LEDs](https://eu.mouser.com/ProductDetail/Cree-Inc/C503D-WAN-CCbEb151/?qs=%2fha2pyFaduioseTUwega4f7QNFIxkmiPpTYJtecMwRYMRUl7rUkX86TpIVdXPQIk) | For the light part of "nightlight" | 4 | $0.24 | $0.92
[Tilt Switch](http://www.mouser.com/ProductDetail/E-Switch/TM1000/?qs=sGAEpiMZZMtCWdKUURnHj1%252bkvdiUuPvDlfB2tFt2oBI%3d) | Activates nightlight. | 1 | $1.25 | $1.25
150 Ohm Resistors | For current limiting the LEDs | 2 | $0.02 | $0.04
Perfboard | For soldering all of the components to | 1 | $1.00 | $1.00
Battery Connector | For connecting power to the circuit | 1 | $1.25 | $1.25
9v Battery | Powers the LEDs | 1 | $1.95 | $1.95
Hook up wires | Used to hook everything up | 4 | $0.05 | $0.20
Screws | For closing up the box and securing the circuitry |  | $0.08 | $0.64
||||Total Cost:|$33.65|

starwars_nightlight_parts.png

3D-Model and Electronic Schematic
Screen Shot 2015-04-13 at 11.36.51 PM.png

Screen Shot 2015-04-13 at 11.45.39 PM.png


starwars_nightlight_schematic.png


## Challenges

    I found that printing such large flat surfaces without a raft would cause them to cool unevenly and buckle. This in turn cause the panel to pull away from the print bed, leaving me with a ruined mass of plastic as the printer went on about its business. Adding the raft fixed this.
    Despite being modeled perfectly square, the panels to my nightlight did not print square, making the assembly of my cube a little dicey. Luckily, with enough screws, tape, and patience, I was able to get the nightlight into a relatively stable and relatively cubic shape. Then, using a combination of hot and super glues, I secured all but the top panels to each other. Fortunately, the panels were not so warped that they pulled apart when the tape was removed and the glues held everything in place as hoped.
    Using a ball bearing based tilt switch for this project was probably a mistake. It's very sensitive to the slightest vibrations and causes the nightlight to flicker. If I were to redo the project, I might use a mercury switch (though this seems like a bad idea for something that is meant for a child's room) or a reed switch activated by a magnet in a vertical track.


## Brainstorming
My first several ideas for a nightlight were fairly standard, drawing inspiration from common light sources I am familiar with. These ideas, falling into the pragmatic category, include what is essentially the business end of a flashlight, a lightbulb shaped nightlight, and a lighthouse.

sw_parabolic_idea.jpgsw_bulb_idea.jpg
sw_lighthouse_idea.jpg

Continuing my inspiration from familiar light sources while straying slightly more into the whimsical are the UFO and Plumbob nightlights. The UFO just seemed like a cute idea for something that would glow with an internal light. The Plumbob is an object from The Sims, a video game about managing the life and happiness of simulated people. In this game the Plumbob hovers above characters' heads, slowly spinning and changing color to reflect their moods. This light would spin and change colors at random, although it did occur to me that one could integrate it with a system that would monitor a Twitter feed, perform some simple sentiment analysis, and change the lights color to reflect one's mood. This was beyond the scope of this project, but seemed like a neat idea.
sw_ufo_idea.jpgsw_bob_idea.jpg
I next extended the idea of motion in a nightlight to that of interaction. It occurred to me that if one were to wake up in the middle of the night it would be fairly difficult to turn on your nightlight. It's dark, you're groggy and disoriented, and you're quite possibly in the grips of terror as you try and figure out if that shape in the corner is your jacket on a chair or a ravenous beast of the night. Having to find a tiny switch on your nightlight should be the least of your worries. Given all of this, I came up with the [Weeble](https://www.youtube.com/watch?v=dFzhjnjXc2o) nightlight, inspired by the toy of the same name from the early 1970s which purports to wobble, yet not fall down. To activate the nightlight, you simply bat it to one side, it pops back up, and turns on.
sw_weeble_idea.jpg

Next I decided to try and push my ideas further into the realm of the whimsical. I wanted to try to incorporate another bit of playful interaction with this one. I began by thinking of sources of light that are well known, if not mainstream, and eventually hit upon the Eye of Sauron. To activate this nightlight, one would need to put on the One Ring, alerting Sauron to your presence and lighting up his giant, ever present eye. In the end, I decided that this may have been a little too whimsical and creating a model that would print well seemed like a nightmare.
sw_sauron_idea.jpg

I also wanted to consider some ideas that involved procedurally generating nightlights from interesting data. I wanted the data to be contextually relevant, dealing with sleep or the night. To that end, I came up with two ideas: a nightlight generated from one's sleep patterns and one generated from maps of the Moon.

The first nightlight would simply use data gathered from a Fitbit, detailing periods of sleep, restlessness, and wakefulness to create a decorative pattern. The second one would use the albedo (or reflectiveness) of the Moon to control the thickness of the front plate of the nightlight. More reflective portions of the Moon would result in thinner sections and, with an LED placed behind the front plate, would result in more light getting through and a brighter spot on the nightlight.

sw_fitbit_idea.jpgsw_moon_idea.jpg

Finally, I thought that maybe I would combine several aspects of previous ideas. My final design has a little bit of interaction in the form of a switch that requires more than pushing a button. It's practical, in the sense that it is a very simple shape, making it easy to model and print. Also, there is a little bit of whimsy as the nightlight appears to be a boring cube at first, but houses a surprise: as the light turns on a hidden pattern is revealed.
sw_cube_idea.jpg

## Thoughts about Project

    Sketching out ideas first was great. I found it very helpful to have this semi-guided exercise.
    3D printing is a lot of fun. It's still crazy to me that something that exists purely in my brain can exist in the real world within a day.


## References
I found either resources or inspiration from the following:

    [Holocron Cube](http://starwars.wikia.com/wiki/Holocron)
    Emblem graphics from [Wookiepedia](http://starwars.wikia.com/wiki/Main_Page)
    [Weebles](http://en.wikipedia.org/wiki/Weeble)
    [Eye of Sauron](http://en.wikipedia.org/wiki/Sauron#Eye_of_Sauron)
    The Plumbob from [The Sims](http://www.thesims.com/)