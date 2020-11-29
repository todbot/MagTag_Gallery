
# Load all the drawings from their individual files in "/drawings"
# equivalent to doing: "from drawings.00default import draw" for all files
# and play each ones 'draw()' function in an array called "drawings[]'


folder = 'drawings'

auto_detect = False

if auto_detect:
    import os
    drawing_names = os.listdir(folder)
    drawing_names = [n.replace('.py','') for n in drawing_names]
    drawing_names.sort()
else:
    # list of drawing programs
    drawing_names = ['00default', 'image1', 'image2', 'image3', 'image4']

# folder containing the drawing programs
import_names = [folder+'.'+d for d in drawing_names]

#import_names = [d for d in drawing_names]
drawings = [__import__(n, locals(),globals(),('draw')) for n in import_names ]




