#! python

#converts a likert scale to match another scale
#equation from IBM article: https://www.ibm.com/support/pages/transforming-different-likert-scales-common-scale

import numpy as np


def likert_convert(main_scale_min, main_scale_max, scale2convert_min, scale2convert_max):
    '''
    Converts a likert scale to a common scale. Returns the new values of the scale being converted (smaller scale).
        Parameters:
                main_scale_min: minimum value of the main (larger) scale
                main_scale_max: maximum value of the main (larger) scale
                scale2convert_min: minimum value of the scale you are converting (smaller scale)
                scale2convert_max: maximum value of the scale you are converting (smaller scale) 
        Returns:
            The values to which the scale2convert will be reassigned to match the main scale.
        Notes:
            Dayforce report must be a V2 report.
            Row Limit: 5000
    '''
    convert_scale= np.arange(scale2convert_min, scale2convert_max+1) #generates the range for the scale givin the min and max

    return [((main_scale_max-main_scale_min)*(i-scale2convert_min)/(scale2convert_max-scale2convert_min)+main_scale_min) for i in convert_scale]


#convert a 3 point scale to a 5 point scale
print(likert_convert(1, 5, 1, 3))