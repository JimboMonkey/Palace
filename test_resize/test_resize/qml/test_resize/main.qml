// import QtQuick 1.0 // to target S60 5th Edition or Maemo 5
import QtQuick 1.1

Rectangle {
    width: 360
    height: 360
    MouseArea {
        x: 440
        y: 128
        anchors.rightMargin: -440
        anchors.bottomMargin: -128
        anchors.leftMargin: 440
        anchors.topMargin: 128
        anchors.fill: parent
        onClicked: {
            Qt.quit();
        }
    }

    Image {
        id: image1
        x: 87
        y: 96
        width: 187
        height: 169
        source: "../../../../Mushroom.png"
    }

    Row {
        id: row1
        x: 0
        y: 0
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0
        anchors.fill: parent
    }
}
