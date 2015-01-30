from PyQt4 import QtGui as gui

app = gui.QApplication([])

pm = gui.QPixmap("Mushroom.png")

scene = gui.QGraphicsScene()
scene.setSceneRect(0, 0, 100, 100) #set the size of the scene

view = gui.QGraphicsView()
view.setScene(scene)

item1 = scene.addPixmap(pm) #you get a reference of the item just added
#item1.setPos(0,100-item1.boundingRect().height()) #now sets the position
item1.setPos(200,0) #now sets the position

view.show()
app.exec_()
