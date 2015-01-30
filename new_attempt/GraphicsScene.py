
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GraphicsScene(QGraphicsScene):
    def __init__(self, parent):
        super(GraphicsScene, self).__init__(parent)
        self.parent = parent
        self.prevItem = []
        self.ns = ns
        self.setBackgroundBrush(QBrush(QColor(50,50,50) , Qt.SolidPattern))


    def mouseReleaseEvent(self, event):
        if event.button() == 2: #Right mouse click
            #Set previous selections selected
            for item in self.prevItem:
                item.setSelected(1)

            item = self.itemAt(event.lastScenePos ().x(), event.lastScenePos ().y())
            if item:
                item.setSelected(1)

        if event.button() == 1: # Left mouse click
            #Get selected item
            items = self.selectedItems()

            #Shift click
            if event.modifiers() & Qt.ShiftModifier: 
                #Set previous items selected
                for item in self.prevItem:
                    item.setSelected(1)

                for item in items:
                    self.prevItem.append(item)

                item = self.itemAt(event.scenePos ().x(), event.scenePos ().y())
                if item == None:
                    self.clearSelection()

            else:
                self.prevItem = []
                for item in items:
                    self.prevItem.append(item)

        super(GraphicsScene, self).mouseReleaseEvent(event)

    def mousePressEvent(self, event):
        if event.modifiers() & Qt.ShiftModifier:
            item = self.itemAt(event.scenePos ().x(), event.scenePos ().y())
            if item:
                item.setSelected(1)

        super(GraphicsScene, self).mousePressEvent(event)

