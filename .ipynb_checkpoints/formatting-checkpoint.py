#Define color pallete
redBar = '#ECCFC2'
oneWeekDecreaseColor = '#ABEDC0'
borderColor = '#D9B596'
increaseColor = '#D93B3B'
decreaseColor = '#577A36'
titleColor = '#364959'
labelColor = '#706D65'

#Color scale pallette
dark = '#85595C'
medDark = '#FFD9D4'
light = '#FAF2ED'
medLight = '#FDE3C3'
medium = '#F5D8C4'

#Sets each spine to a more subtle color and width
def formatBorder(ax):
    for spineName in ax.spines:
        ax.spines[spineName].set_color(borderColor)
        ax.spines[spineName].set_linewidth(2)
        
#Returns a tuple that pairs two contrasting colors for the face and data display respectively
def getContrastingColors(weeksClimbing):
    if(weeksClimbing >= 4):
        return (medDark, dark)
    if(weeksClimbing >= 3):
        return (medium, dark)
    if(weeksClimbing >= 2):
        return (medLight, dark)
    return (light, dark)

# Returns the difference between the most recent increase and the prevous day's
def getLastIncreaseChange(state, df):
    return int(df[state][0]) - int(df[state][1])

# Returns a positive sign string if increase >= 0 (for annotation strings)
def getIncreaseSign(increase):
    if(increase >= 0):
        return '+'
    else:
        return ''

#Returns a color based on the sign of the relative increase (green=less, red=more)
def getIncreaseColor(increase):
    if(increase >= 0):
        return increaseColor
    else:
        return increaseColor

#Annotations to help read the charts
guideArrow = dict(arrowstyle='wedge',
                        connectionstyle="angle3", color=medium, relpos = (1, 0.5))

def createLabelGuide(ax, text, xy, xycoords, textypos):
    ax.annotate(s=text,xy=xy, xytext=(-.3, textypos), 
                            textcoords='axes fraction', xycoords=xycoords, fontsize=11,
                            color=labelColor, horizontalAlignment='right',
                            arrowprops=guideArrow)