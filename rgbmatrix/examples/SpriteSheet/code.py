import displayio
import framebufferio
import rgbmatrix
import board
import adafruit_imageload
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

# Load the sprite sheet (bitmap)
bitmap, palette = adafruit_imageload.load("/cp_sprite_sheet.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create a sprite (tilegrid)
tileGrid = displayio.TileGrid(bitmap, pixel_shader=palette,
                            width = 3,
                            height = 1,
                            tile_width = 16,
                            tile_height = 16)

numOfTiles = bitmap.width // 16 * bitmap.height // 16

tileGrid[0, 0] = 0
tileGrid[1, 0] = 1
tileGrid[2, 0] = 2

# Create a Group to hold the sprite
group = displayio.Group(scale=1)

# Add the sprite to the Group
group.append(tileGrid)

# Assign the Group as the root display Group
# This is the Group that is displayed
display.root_group = group

display.refresh()

while True:
    for i in range(tileGrid.width):
        for j in range(tileGrid.height):
            tileGrid[i, j] = (tileGrid[i, j] + 1) % numOfTiles
    display.refresh()
    time.sleep(1)