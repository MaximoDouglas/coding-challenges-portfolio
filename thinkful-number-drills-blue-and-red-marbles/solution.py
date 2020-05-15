def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    total_blue = blue_start - blue_pulled
    total_red  = red_start - red_pulled
    
    return total_blue/(total_blue+total_red)