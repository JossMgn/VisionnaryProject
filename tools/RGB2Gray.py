from tools.Tool import Tool
import numpy as np
import skimage as sk
import skimage.io as skio
import skimage.color as color
import matplotlib.pyplot as plt

class RGB2Gray(Tool):
    def __init__(self, img):
        super().__init__(img)
        
    def applyTool(self, param):
        """
        Verify if the image has 3 or more channels and turns it into a 1 channel image
        Input:  -param (str): Precise the way of doing the transformation
                                'r', 'g' or 'b': Retrieve respectively only the red, green or blue channel
                                'rg', 'rb', 'gb': Do a mean of the two selected channels
                                'mean': Do a mean of the three channels
                                'lum': Convert the image in CIE L*a*b* to get the luminance
        """
        ch_name = ['r', 'g', 'b']
        if len(self.img_.shape) < 3:
            return "The image is already in gray scale."
        else:
            img = sk.img_as_float(self.img_)
        
        if len(param) == 1 and param in ch_name:
               idx_ch = ch_name.index(param)
               gray_img = img[:,:, idx_ch]

               self.pr_img_ = sk.img_as_ubyte(gray_img)
            #    self.pr_img_ = gray_img
               return None
        
        elif len(param) == 2:
             ch1, ch2 = param[0], param[1]
             if ch1 not in ch_name or ch2 not in ch_name:
                return f"Error, you chose as parameters {param} which is not managed. Please chose an defined parameter."
             else:
                idx_ch1 = ch_name.index(ch1)
                idx_ch2 = ch_name.index(ch2)

                gray_img = (img[:, :, idx_ch1]+img[:, :, idx_ch2]) / 2
                self.pr_img_ = sk.img_as_ubyte(gray_img)
                # self.pr_img_ = gray_img
                return None
             
        elif param == 'mean':
            gray_img = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
            self.pr_img_ = sk.img_as_ubyte(gray_img)
            # self.pr_img_ = gray_img
            return None
        
        elif param == "lum":
            lab_img = color.rgb2lab(self.img_)
            gray_img = lab_img[:, :, 0]
            gray_img = (gray_img / 100 * 255).astype(np.uint8)
            self.pr_img_ = gray_img
            return None
        
        else:
             return f"Error, you chose as parameters {param} which is not managed. Please chose an defined parameter."
             

# if __name__ == "__main__":
#      path = "assets\I0001.png"
#      img = skio.imread(path)
#     #  plt.imshow(img)
#     #  plt.show()
#      tool = RGB2Gray(img)
#      status = tool.applyTool('lum')
#      pr_img = tool.getProcessedImg()
#      plt.imshow(pr_img, cmap='gray')
#      plt.show()

