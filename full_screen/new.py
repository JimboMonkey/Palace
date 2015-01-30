
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import QExtendedLabel2   
import QExtendedPixmap
import QExtendedGroup
import GraphicsScene 
from Dealer import *
from Player import *
from ComputerPlayer import *
from Table import *
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot

class TableView(QtGui.QGraphicsView):
    
    def __init__(self):
        super(TableView, self).__init__()
        
       # self.setGeometry(300, 300, 300, 300)
        
        policy = QtCore.Qt.ScrollBarAlwaysOff
        self.setVerticalScrollBarPolicy(policy)
        self.setHorizontalScrollBarPolicy(policy)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        #self.origPixmap = QtGui.QPixmap('KingHearts.png')
        self.InitialiseView()      
        
    def InitialiseView(self):
          
        self.group = None  
        self.scene = TableScene()
        self.setScene(self.scene)
        #self.setSceneRect(QRectF(self.viewport().rect()))
        self.setSceneRect(0, 0, 1000, 700)    

        for item in self.scene.items():
            if type(item) == QExtendedGroup.MyGroup:
                pass#print item.getName()

    def action(self, Player):
        #print QtGui.QDesktopWidget().screenGeometry()
        #print self.geometry()
        faceups = Player.UpdateGUIFaceups()
        print len(self.scene.items())
        i = 0
        for card in faceups:
            print card.Name + card.Suit
            self.TestPixmap = QtGui.QPixmap('/home/jimbo/Dropbox/PyQtProjects/Palace/Cards/' + card.Name + card.Suit + '.png')
            self.TestPixmap = self.TestPixmap.scaled(self.geometry().width()/10,self.geometry().height()/6,Qt.KeepAspectRatio,  Qt.SmoothTransformation)
            self.scene.items()[i].setPixmap(self.TestPixmap)
            i += 1
        print "ok now!"


    def resizeEvent(self, ev):
        #print "RESIZE EVENT"
        for obj in self.scene.items():
            #print type(obj)
            if type(obj) == QExtendedGroup.MyGroup:
                #print obj.getName()
                if obj.getName() == "dealer":
                    size = ev.size()
                    i = (size.height() / 4) - (pixmap.height() / 3)#-(size.height() / 3)
                    z = 0
                    num = size.height() / 6
                    wnum = size.width() / 10

                    #print "size: ", size.height()
                    #print "pos: ", (size.height() / 2)
               
                    #print "length: ", len(self.items())
                    count = 0
                    for item in obj.childItems():
                        if type(item) == QExtendedPixmap.ExtendedQPixmap:
                            count += 1
                            #print type(item)
                            #pixmap = item.pixmap()
                            pixmap = item.getOriginal()
                            #pixmap = pixmap.scaledToHeight(num, Qt.SmoothTransformation)
                            pixmap = pixmap.scaled(wnum,num,Qt.KeepAspectRatio,  Qt.SmoothTransformation)
                            if count == 4:
                                # Pile
                                item.setPos((self.width() /2)+(pixmap.width() /4), (size.height() / 4) - (pixmap.height() / 3) )#-(size.height() / 3))
                            elif count == 5:
                                # Deck
                                item.setPos((self.width() /2)-(pixmap.width() *2), (size.height() / 4) - (pixmap.height() / 3))#-(size.height() / 3))
                            else:
                                item.setPos(self.width() /2, i)
                                i += pixmap.height() / 4
                            #self.centerOn(1.0, 1.0)
                            item.setPixmap(pixmap)
                            item.setZValue(z)
                            z += 1
                elif obj.getName() == "player":
                    #print "player"
                    size = ev.size()
                    i = 0
                    j = size.height() / 2
                    z = 0
                    num = size.height() / 6
                    wnum = size.width() / 10
               
                    #print "length: ", len(self.items())
                    count = 0
                    card_num = 0
                    for item in obj.childItems():
                        count += 1
                        card_num += 1
                        pixmap = item.getOriginal()
                        #pixmap = pixmap.scaledToHeight(num, Qt.SmoothTransformation)
                        pixmap = pixmap.scaled(wnum,num,Qt.KeepAspectRatio,  Qt.SmoothTransformation)
                        #print "count = ", count
                        if ((count % 14) == 0):
                            #print "helloooo"
                            j += 40
                            count = 1
                        item.setPos((self.width() /2)-(pixmap.width() *2.75)+ count * (pixmap.width()/3), j)#-(size.height() / 3))
                        #item.setPos((pixmap.width()*2.75) + count * (pixmap.width()/3), j)
                        self.centerOn(1.0, 1.0)
                        item.setPixmap(pixmap)
                        item.setZValue(z)
                        z += 1
                elif obj.getName() == "computer1":
                    #print "computer1"
                    size = ev.size()
                    i = 0
                    j = size.height() / 2
                    z = 0
                    num = size.height() / 6
                    wnum = size.width() / 10
               
                    #print "length: ", len(self.items())
                    count = 0
                    for item in obj.childItems():
                        count += 1
                        pixmap = item.getOriginal()
                        #pixmap = pixmap.scaledToHeight(num, Qt.SmoothTransformation)
                        pixmap = pixmap.scaled(wnum,num,Qt.KeepAspectRatio,  Qt.SmoothTransformation)
                        #print "count = ", count
                        item.setPos(0 + ( pixmap.width() *count),0)# + (count * pixmap.width()), 0)
                        self.centerOn(1.0, 1.0)
                        item.setPixmap(pixmap)
                        item.setZValue(z)
                        z += 1 
                elif obj.getName() == "computer2":
                    #print "computer2"
                    size = ev.size()
                    i = 0
                    j = size.height() / 2
                    z = 0
                    num = size.height() / 6
                    wnum = size.width() / 10
               
                    #print "length: ", len(self.items())
                    count = 5
                    for item in obj.childItems():
                        count -= 1
                        pixmap = item.getOriginal()
                        #pixmap = pixmap.scaledToHeight(num, Qt.SmoothTransformation)
                        pixmap = pixmap.scaled(wnum,num,Qt.KeepAspectRatio,  Qt.SmoothTransformation)
                        #print "count = ", count
                        item.setPos(size.width() - ( pixmap.width() *count),0)# + (count * pixmap.width()), 0)
                        self.centerOn(1.0, 1.0)
                        item.setPixmap(pixmap)
                        item.setZValue(z)
                        z += 1
#        self.action()




class TableScene(QGraphicsScene):
    def __init__(self):
        super(TableScene, self).__init__()        
        self.InitialiseScene()
        
        self.mygroup = None

    def InitialiseScene(self):    
        
        x = 0
        z = 0
        self.mygroup = QExtendedGroup.MyGroup("dealer")

        for i in xrange(0, 3):
            card = QExtendedPixmap.ExtendedQPixmap(self)
            self.origPixmap = QtGui.QPixmap('KingHearts.png')
            card.setOriginal(self.origPixmap)
            self.mygroup.addToGroup(card)
            #print type(card)
            card.SetID(i)
            #print "hmm", type(res)
            card.setPixmap(self.origPixmap)
            #card.setPos(self.width()/3, x)
            #card.setOrigPos(self.width()/3, x)
            z += 1
            x += self.origPixmap.height() / 12
            #print "x=", x
            #print "poo", x
            flag1 = QtGui.QGraphicsItem.ItemIsMovable
            flag2 = QtGui.QGraphicsItem.ItemIsSelectable
            #res.setFlag(flag1, True)
            #res.setFlag(flag2, True)
            #res.setPos(20, 30+i*60, 191, 250)
            #res = self.addItem(card)
        
        card = QExtendedPixmap.ExtendedQPixmap(self)
        self.mygroup.addToGroup(card)
        #self.addItem(mygroup)
        card.setOriginal(self.origPixmap)
        card.setPixmap(self.origPixmap)
        #card.setPos(625, 0)
        card.SetID(3)
        #card.setOrigPos(625, 0)
        #res = self.addItem(card)
        z = 0
        for item in self.mygroup.childItems():
            item.setZValue(z)
            z += 1
            #print "monkey:", item"""

        card = QExtendedPixmap.ExtendedQPixmap(self)
        self.mygroup.addToGroup(card)
        self.addItem(self.mygroup)
        print "adding dealer"
        card.setOriginal(self.origPixmap)
        card.setPixmap(self.origPixmap)
        #card.setPos(self.width()/0.5, 0)
        card.SetID(4)
        #card.setOrigPos(self.width()/0.5, 0)
        #res = self.addItem(card)

        self.mygroup2 = QExtendedGroup.MyGroup("player")
        self.origPixmap = QtGui.QPixmap('CardBack.png')
        for j in range(0, 4):
            for i in range(0,13):
                card = QExtendedPixmap.ExtendedQPixmap(self)
                card.setOriginal(self.origPixmap)
                card.SetID(i)
                card.setPos(i * 40, j)
                #res = self.addItem(card)
                self.mygroup2.addToGroup(card)
                #res = self.addPixmap(self.origPixmap)
                flag1 = QtGui.QGraphicsItem.ItemIsMovable
                flag2 = QtGui.QGraphicsItem.ItemIsSelectable
                #res.setFlag(flag1, True)
                #res.setFlag(flag2, True)
        self.addItem(self.mygroup2)
        print "adding player"

        self.mygroup3 = QExtendedGroup.MyGroup("computer1")
        self.origPixmap = QtGui.QPixmap('CardBack.png')
        for j in range(0, 3):
                card = QExtendedPixmap.ExtendedQPixmap(self)
                card.setOriginal(self.origPixmap)
                card.SetID(i)
                card.setPos(j * 40, 0)
                #res = self.addItem(card)
                self.mygroup3.addToGroup(card)
                #res = self.addPixmap(self.origPixmap)
                flag1 = QtGui.QGraphicsItem.ItemIsMovable
                flag2 = QtGui.QGraphicsItem.ItemIsSelectable
                #res.setFlag(flag1, True)
                #res.setFlag(flag2, True)
        self.addItem(self.mygroup3)
        print "adding computer player 1"

        self.mygroup4 = QExtendedGroup.MyGroup("computer2")
        self.origPixmap = QtGui.QPixmap('CardBack.png')
        for j in range(0, 3):
                card = QExtendedPixmap.ExtendedQPixmap(self)
                card.setOriginal(self.origPixmap)
                card.SetID(i)
                card.setPos(400 + j * 40, 0)
                #res = self.addItem(card)
                self.mygroup4.addToGroup(card)
                #res = self.addPixmap(self.origPixmap)
                flag1 = QtGui.QGraphicsItem.ItemIsMovable
                flag2 = QtGui.QGraphicsItem.ItemIsSelectable
                #res.setFlag(flag1, True)
                #res.setFlag(flag2, True)
        self.addItem(self.mygroup4)
        print "adding computer player 2"

class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(Player)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def setup(self):
        James = Player("James")
        Phil = ComputerPlayer("Phil")
        Nash = ComputerPlayer("Nash")

        self.MyTable = Table()
        self.MyTable.AddPlayer(James)
        self.MyTable.AddPlayer(Phil)
        self.MyTable.AddPlayer(Nash)

        self.MyTable.ListPlayers()

        self.MyDealer = Dealer()

        for i in xrange(0, 6):
            for xPlayer in self.MyTable.Players:		
                xPlayer.InitialTakeCard(self.MyDealer.DeckDeal())

        for i in xrange(0, 3):
            for xPlayer in self.MyTable.Players:
                xPlayer.TakeCard(self.MyDealer.DeckDeal())

        for xPlayer in self.MyTable.Players:
           xPlayer.ListHand()

        self.stored_player = James

    def run(self):
        time.sleep(random.random()*5)  # random sleep to imitate working
        self.trigger.emit(self.stored_player)

class Game(QtGui.QWidget):
    
    def __init__(self):
        super(Game, self).__init__()
        
        self.initUI()
        

        #for xPlayer in self.MyTable.Players:
         #   xPlayer.ListHand()

        #self.viewmid.action(James)

        #self.MyDealer.ListDeck()
        #self.MyDealer.mysignal.connect(self.viewmid.action())
        #self.MyDealer.PlayCardValue().connect(self.viewmid.action())
        #self.viewmid.action()
        #bag = PunchingBag()
        # Connect the bag's punched signal to the say_punched slot
 #       self.MyDealer.punched.connect(self.viewmid.action)

        # Punch the bag 10 times
        #for i in range(10):
#        self.MyDealer.punch()

        thread = MyThread(self)    # create a thread
        thread.trigger.connect(self.viewmid.action)  # connect to it's signal
        thread.setup()  
        thread.start()             # start the thread


    def initUI(self):
        
        middlerow = QtGui.QHBoxLayout()
        self.viewmid = TableView()    
        middlerow.addWidget(self.viewmid)

        self.setLayout(middlerow)
        self.setWindowTitle("Shithead")
        self.setGeometry(150, 150, 1000, 700)
        

app = QtGui.QApplication([])
ex = Game()
ex.show()
sys.exit(app.exec_())

