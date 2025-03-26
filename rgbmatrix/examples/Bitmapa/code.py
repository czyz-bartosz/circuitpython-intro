import displayio
import framebufferio
import rgbmatrix
import board
import time

#  Releases any actively used displays so their buses and pins can be used again.
# This should be called before initializing a display
displayio.release_displays()

#  Initialize a RGBMatrix, it also initializes framebuffer if not passed:
matrix = rgbmatrix.RGBMatrix(
    width=64,
    bit_depth=4,
    rgb_pins=[
        board.MTX_R1,
        board.MTX_G1,
        board.MTX_B1,
        board.MTX_R2,
        board.MTX_G2,
        board.MTX_B2
    ],
    addr_pins=[
        board.MTX_ADDRA,
        board.MTX_ADDRB,
        board.MTX_ADDRC,
        board.MTX_ADDRD
    ],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE
)

# Create Display object to manage framebuffer created by RGBMatrix
# auto_refresh=False so that we can manually refresh the display
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

bitmap = displayio.Bitmap(10, 10, 3)
palette = displayio.Palette(3)

palette[0] = 0x0000FF
palette[1] = 0xFF0000
palette[2] = 0x00FF00

# Create "fake" tile grid, tilegrid displays al bitmap 
tileGrid = displayio.TileGrid(
    bitmap=bitmap,
    pixel_shader=palette,
)

# Create a Group to hold the tilegrid
group = displayio.Group()

# Add the sprite to the Group
group.append(tileGrid)

# Assign the Group as the root display Group
# This is the Group that is displayed
display.root_group = group

# set (0,0) cell in bitmap to palette[1] = 0xFF0000
bitmap[0,0] = 1

# set (1,1) cell in bitmap to palette[2] = 0x00FF00
bitmap[1,1] = 2

display.refresh()

while True:
    pass