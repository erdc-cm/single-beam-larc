"""
A module for processing survey data

This module collects implements algorithms for  reading and  processing surveys.
"""
import numpy as np

class Survey:
    """
    A survey of a specific site with multiple survey lines
    """
    def __init__(self,fname):
        import numpy as np
        self.lines = {}
        self.lines_ll = {}
        self.csvArray = csvArray = np.genfromtxt(fname=fname,delimiter=',',skip_header=0,
                                            names=('id'    ,'line_number' ,'lon'      ,'lat'    ,'x'       ,'y'       ,'z'),
                                            dtype=(np.uint ,np.uint       ,np.double, np.double ,np.double ,np.double ,np.double),
                                            usecols=(0,1,3,4,7,8,9))
        for line_number in set(self.csvArray['line_number']):
            self.lines[line_number] = np.transpose(np.vstack([self.csvArray['x'][csvArray['line_number'] == line_number],
                                                              self.csvArray['y'][csvArray['line_number'] == line_number],
                                                              self.csvArray['z'][csvArray['line_number'] == line_number]]))
            self.lines_ll[line_number] = np.transpose(np.vstack([self.csvArray['lon'][csvArray['line_number'] == line_number],
                                                                 self.csvArray['lat'][csvArray['line_number'] == line_number],
                                                                 self.csvArray['z'][csvArray['line_number'] == line_number]]))
    def  plot_lines(self,line_numbers=None):
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(12,12))
        ax = fig.add_subplot(111, projection='3d')
        if line_numbers==None:
            line_numbers = self.lines.keys()
        for  ln in line_numbers:
            ax.scatter(self.lines[ln][:,0],self.lines[ln][:,1],self.lines[ln][:,2],c=self.lines[ln][:,2])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        return plt

    def plot_surface(self):
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import cm
        import matplotlib.pyplot as plt
        import numpy as np
        fig = plt.figure(figsize=(12,12))
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(self.csvArray['x'],self.csvArray['y'],self.csvArray['z'], cmap=cm.jet, linewidth=0.0)
        return plt

    def plot_contours(self):
        import matplotlib.pyplot as plt
        import numpy as np
        plt.figure(figsize=(12,12))
        plt.tricontourf(self.csvArray['x'],self.csvArray['y'],self.csvArray['z'])
        return plt
    
    def kml(self,fname):
        import simplekml
        kml = simplekml.Kml()
        for x,y,z in zip(self.csvArray['lon'],self.csvArray['lat'],self.csvArray['z']):
            kml.newpoint(coords=[(x,y,z)])  # lon, lat, optional height
        kml.save(fname+".kml")

class SurveySite:
    """
    A specific site with (overlapping) surveys through time
    """
    def __init__(self,dirname):
        """
        Read all the csv files in a directory
        """
        import glob,os
        self.surveys=[]
        for f in glob.glob(os.path.join(dirname,"*.csv")):
            self.surveys.append(Survey(fname=f))
    def contourAnimation(self):
        for si,s in enumerate(self.surveys):
            contour_plot = s.plot_contours()
            contour_plot.savefig("contour%3.3d"  % (si,))
