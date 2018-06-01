"""
Epoch
Get Unix epoch time - seconds since 01/01/1970
By May Hamer
"""

import time  # Time library
import click  # Command line library

def epoch():
    """Return number of seconds since 01/01/1970"""
    floatingPointEpoch = time.time()  # Get epoch as floating point
    integerEpoch = int(floatingPointEpoch)  # Convert floating point to integer
    return floatingPointEpoch, integerEpoch

@click.command()
@click.option("--displayAsFloat", is_flag = True)  # If set, display time in floating point
@click.option("--fullString", is_flag = True)  # If set, display time as full string
def main(displayasfloat, fullstring):
    floatingPointEpoch, integerEpoch = epoch()

    if displayasfloat:  # If the command line parameter to display as a floating point, then use a floating point epoch
        epochTime = floatingPointEpoch
    else:  # Otherwise, use an integer
        epochTime = integerEpoch

    if fullstring:  # If the command line parameter to display a full info string is set, then display it
        print("Seconds since Jan 1 1970: {}".format(epochTime))
    else:  # Otherwise just display the data
        print(epochTime)

main()
