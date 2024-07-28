class Tool:
    def __init__(self, img):
        self.img_ = img
        self.pr_img_ = None

    def applyTool(self):
        pass

    def getProcessedImg(self):
        return self.pr_img_
    
    def getImg(self):
        return self.img_