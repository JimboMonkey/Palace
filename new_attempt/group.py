#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import QExtendedLabel2   
import QExtendedPixmap
import GraphicsScene       
            
class MyGroup(QtGui.QGraphicsItemGroup):
    
    def __init__(self):
        super(MyGroup, self).__init__()
        
        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, 
            True)
    
    def paint(self, painter, option, widget):
    
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        brush = QtGui.QBrush(QtGui.QColor("#333333"))
        pen = QtGui.QPen(brush, 0.5)
        pen.setStyle(QtCore.Qt.DotLine)
        painter.setPen(pen)
        
        if self.isSelected():
            boundRect = self.boundingRect()
            painter.drawRect(boundRect)        

    def mousePressEvent(self,event):
        print "hello"
            

class DealersScene(QGraphicsScene):
    def __init__(self):
        super(DealersScene, self).__init__()        
        self.InitialiseScene()

    def InitialiseScene(self):    
        self.origPixmap = QtGui.QPixmap('KingHearts.png')
        x = 0
        z = 0
        mygroup = QGraphicsItemGroup()

        for i in xrange(0, 3):
            card = QExtendedPixmap.ExtendedQPixmap(self)
            #mygroup.addToGroup(card)
            card.setOriginal(self.origPixmap)
            #print type(card)
            card.SetID(i)
            #print "hmm", type(res)
            card.setPixmap(self.origPixmap)
            card.setPos(400, x)
            card.setOrigPos(400, x)
            z += 1
            x += self.origPixmap.height() / 12
            #print "x=", x
            #print "poo", x
            flag1 = QtGui.QGraphicsItem.ItemIsMovable
            flag2 = QtGui.QGraphicsItem.ItemIsSelectable
            #res.setFlag(flag1, True)
            #res.setFlag(flag2, True)
            #res.setPos(20, 30+i*60, 191, 250)
            res = self.addItem(card)
        
        card = QExtendedPixmap.ExtendedQPixmap(self)
        #mygroup.addToGroup(card)
        #self.addItem(mygroup)
        card.setOriginal(self.origPixmap)
        card.setPixmap(self.origPixmap)
        card.setPos(625, 0)
        card.SetID(3)
        card.setOrigPos(625, 0)
        res = self.addItem(card)
        z = 0
        for item in mygroup.childItems():
            item.setZValue(z)
            z += 1
            #print "monkey:", item"""

        card = QExtendedPixmap.ExtendedQPixmap(self)
        #mygroup.addToGroup(card)
        #self.addItem(mygroup)
        card.setOriginal(self.origPixmap)
        card.setPixmap(self.origPixmap)
        card.setPos(625, 0)
        card.SetID(4)
        card.setOrigPos(625, 0)
        res = self.addItem(card)

class DealersView(QtGui.QGraphicsView):
    
    def __init__(self):
        super(DealersView, self).__init__()
        
        self.setGeometry(300, 300, 300, 300)
        
        policy = QtCore.Qt.ScrollBarAlwaysOff
        self.setVerticalScrollBarPolicy(policy)
        self.setHorizontalScrollBarPolicy(policy)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        #self.origPixmap = QtGui.QPixmap('KingHearts.png')
        self.InitialiseView()
        
        
    def InitialiseView(self):
          
        self.group = None  
        self.scene = DealersScene()
        self.setSceneRect(0, 0, 600, 600)    
        self.setScene(self.scene)  

    def resizeEvent(self, ev):
        size = ev.size()
        i = 0
        z = 0
        ratio = 676.0 / size.width()
        #print "ratio: ", ratio
        num = size.height() / 2.3
   
        #print "length: ", len(self.items())
        count = 0
        for item in self.items():
            if type(item) == QExtendedPixmap.ExtendedQPixmap:
                count += 1
                #print type(item)
                #pixmap = item.pixmap()
                pixmap = item.getOriginal()
                pixmap = pixmap.scaledToHeight(num, Qt.SmoothTransformation)
                if count == 4:
                    item.setPos((self.width() /2)+(pixmap.width() /4), 0)
                elif count == 5:
                    item.setPos((self.width() /2)-(pixmap.width() *2), 0)
                else:
                    item.setPos(self.width() /2, i)
                    i += pixmap.height() / 4
                self.centerOn(1.0, 1.0)
                item.setPixmap(pixmap)
                item.setZValue(z)
                z += 1  
                
        #print "TYPE: ", type(self.items()[-1])


class PlayersView(QtGui.QGraphicsView):
    
    def __init__(self):
        super(PlayersView, self).__init__()
        
        self.setGeometry(300, 300, 300, 300)
        
        policy = QtCore.Qt.ScrollBarAlwaysOff
        self.setVerticalScrollBarPolicy(policy)
        self.setHorizontalScrollBarPolicy(policy)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.origPixmap = QtGui.QPixmap('CardBack.png')
        self.InitialiseView()

        
        
    def InitialiseView(self):
          
        self.group = None  
        self.scene = PlayersScene()
        self.setSceneRect(0, 0, 600, 600)    
        self.setScene(self.scene)  
        

    def resizeEvent(self, ev):
        size = ev.size()
        i = 0
        j = 0
        z = 0
        ratio = 676.0 / size.width()
        #print "ratio: ", ratio
        num = size.height() / 2.3
   
        #print "length: ", len(self.items())
        count = 0
        for item in self.items():
            count += 1
            pixmap = item.getOriginal()
            pixmap = pixmap.scaledToHeight(num, Qt.SmoothTransformation)
            #print "count = ", count
            if ((count % 14) == 0):
                #print "helloooo"
                j += 40
                count = 1
            item.setPos(count * 40, j)
            self.centerOn(1.0, 1.0)
            item.setPixmap(pixmap)
            item.setZValue(z)
            z += 1 

class PlayersScene(QGraphicsScene):
    def __init__(self):
        super(PlayersScene, self).__init__()        
        self.InitialiseScene()
        self.prevItem = []
        #self.setBackgroundBrush(QBrush(QColor(50,50,50) , Qt.SolidPattern))
        

    def InitialiseScene(self):    

        self.origPixmap = QtGui.QPixmap('CardBack.png')
        for j in range(0, 4):
            for i in range(0,13):
                card = QExtendedPixmap.ExtendedQPixmap(self)
                card.setOriginal(self.origPixmap)
                card.SetID(i)
                card.setPos(i * 40, j)
                res = self.addItem(card)
                #res = self.addPixmap(self.origPixmap)
                flag1 = QtGui.QGraphicsItem.ItemIsMovable
                flag2 = QtGui.QGraphicsItem.ItemIsSelectable
                #res.setFlag(flag1, True)
                #res.setFlag(flag2, True)

    def mouseReleaseEvent(self, event):
        #self.origPixmap = QtGui.QPixmap('Mushroom.png')
        items = self.selectedItems()
        for myitem in items:
            pass#print myitem

        item = self.itemAt(event.lastScenePos ().x(), event.lastScenePos ().y())
        if item:
            if not item.isSelected():
                print "anything?"
                item.setSelected(True)
                #item.setPixmap(self.origPixmap)
                #item.setSelected(1)
            else:
                pass
                #print "something"

        QtGui.QGraphicsScene.mouseReleaseEvent(self, event)



    def mousePressEvent(self, event):
        #self.origPixmap = QtGui.QPixmap('Mushroom.png')
        item = self.itemAt(event.scenePos ().x(), event.scenePos ().y())
        if item:
            if item.getState() == 1:
                item.setState(0)
            else:
                item.setState(1)
            print item.getState()
            if item.isSelected():
                
                #self.origPixmap2 = QtGui.QPixmap('CardBack.png')
                #item.setPixmap(self.origPixmap2)
                #print "card"
                item.setSelected(False)
            else:
                #print "mushroom"
                #item.setPixmap(self.origPixmap)
                item.setSelected(True)

        QtGui.QGraphicsScene.mousePressEvent(self, event)
        #super(GraphicsScene, self).mousePressEvent(event)

class ComputerPlayersView(QtGui.QGraphicsView):
    
    def __init__(self):
        super(ComputerPlayersView, self).__init__()
        
        self.setGeometry(300, 300, 300, 300)
        
        policy = QtCore.Qt.ScrollBarAlwaysOff
        self.setVerticalScrollBarPolicy(policy)
        self.setHorizontalScrollBarPolicy(policy)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.origPixmap = QtGui.QPixmap('CardBack.png')
        self.InitialiseView()
        
        
    def InitialiseView(self):
          
        self.group = None  
        self.scene = ComputerPlayersScene()
        self.setSceneRect(0, 0, 600, 600)    
        self.setScene(self.scene)  
        

    def resizeEvent(self, ev):
        size = ev.size()
        i = 0
        #num = size.width() / len(self.items())
        num = size.width() / 5.5
        
        for item in self.items():
            pixmap = self.origPixmap
            pixmap = pixmap.scaledToWidth(num, Qt.SmoothTransformation)
            self.centerOn(1.0, 1.0)
            item.setPixmap(pixmap)
            #print i
            item.setPos(i, 0)
            i += pixmap.width()



class ComputerPlayersScene(QGraphicsScene):
    def __init__(self):
        super(ComputerPlayersScene, self).__init__()        
        self.InitialiseScene()
        self.prevItem = []
        #self.setBackgroundBrush(QBrush(QColor(50,50,50) , Qt.SolidPattern))
        

    def InitialiseScene(self):    

        self.origPixmap = QtGui.QPixmap('CardBack.png')
        for i in range(0,3):
            card = QExtendedLabel2.ExtendedQLabel(self)
            card.SetID(i)
            res = self.addItem(card)
            #res = self.addPixmap(self.origPixmap)
            flag1 = QtGui.QGraphicsItem.ItemIsMovable
            flag2 = QtGui.QGraphicsItem.ItemIsSelectable
            #res.setFlag(flag1, True)
            #res.setFlag(flag2, True)

    def mouseReleaseEvent(self, event):
        #self.origPixmap = QtGui.QPixmap('Mushroom.png')
        items = self.selectedItems()
        for myitem in items:
            pass#print myitem

        item = self.itemAt(event.lastScenePos ().x(), event.lastScenePos ().y())
        if item:
            if not item.isSelected():
                print "anything?"
                item.setSelected(True)
                #item.setPixmap(self.origPixmap)
                #item.setSelected(1)
            else:
                pass
                #print "something"

        QtGui.QGraphicsScene.mouseReleaseEvent(self, event)



    def mousePressEvent(self, event):
        #self.origPixmap = QtGui.QPixmap('Mushroom.png')
        item = self.itemAt(event.scenePos ().x(), event.scenePos ().y())
        if item:
            if item.getState() == 1:
                item.setState(0)
            else:
                item.setState(1)
            print item.getState()
            if item.isSelected():
                
                #self.origPixmap2 = QtGui.QPixmap('CardBack.png')
                #item.setPixmap(self.origPixmap2)
                #print "card"
                item.setSelected(False)
            else:
                #print "mushroom"
                #item.setPixmap(self.origPixmap)
                item.setSelected(True)

        QtGui.QGraphicsScene.mousePressEvent(self, event)
        #super(GraphicsScene, self).mousePressEvent(event)
        
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        middlerow = QtGui.QHBoxLayout()
        bottomrow = QtGui.QHBoxLayout()
        
        self.view = ComputerPlayersView()
        self.view2 = ComputerPlayersView()       
        #self.view3 = ComputerPlayersView()       
        hbox.addWidget(self.view)
        hbox.addWidget(self.view2)
        #hbox.addWidget(self.view3)

        self.viewmid = DealersView()       
        middlerow.addWidget(self.viewmid)


        self.view4 = PlayersView()
        #self.view5 = ComputerPlayersView()       
        #self.view6 = ComputerPlayersView()       
        bottomrow.addWidget(self.view4)
        #bottomrow.addWidget(self.view5)
        #bottomrow.addWidget(self.view6)
        
        vbox.addLayout(hbox)
        vbox.addLayout(middlerow)
        vbox.addLayout(bottomrow)

        self.setLayout(vbox)
        self.setWindowTitle("Shithead")
        self.setGeometry(150, 150, 700, 700)
        

app = QtGui.QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
