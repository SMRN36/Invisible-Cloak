# Harry's Invisible Cloak

## Algorithm / Project Flow :
1. At first the background is captured in the initial frame from camera 
2. Color of the cloak is identified. To identify that original color space is converted to HSV color space 
3. Subtract that color from the current frame and augment the initial frame on the cloak. This will create an invisible effect. 
Current frame - cloak + initial frame = Invisible 

## Concepts used in this project :
1. Color space conversion 
2. Color tracking 
3. Image Masking 

**Color space conversion :** The original RGB (Red,  Green, Blue) color space  is converted to HSV (Hue, Saturation, Value) color space.

**Color Tracking :** Here we are dealing with the inRange() function which takes HSV image and applies the lower and upper bound ranges of the desired color.

**Image Masking :** The detected color region will be extracted using bitwise operations (AND & OR). After detecting the region of the background frame is placed in that place.
