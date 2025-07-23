import QtQuick 2.15
import QtQuick.Controls 2.15
import QtMultimedia


ApplicationWindow {

    visible: true
    flags: Qt.FramelessWindowHint
    width: Screen.width
    height: Screen.height

    title: "HelloApp"
    Item {
    anchors.fill: parent
    MediaPlayer {
        id: mediaplayer
        source: "file/backgorund.mp4"
        audioOutput: AudioOutput {}
        videoOutput: videoOutput
        autoPlay: true
        loops: MediaPlayer.Infinite
    }

    VideoOutput {
        id: videoOutput
        anchors.fill: parent
    }

    Rectangle {
    x: 1000
    y: 900
    width: 200  
    height: 50  
    color: "transparent"  
    border.color: "#FF0000"
    topLeftRadius: 10.0
    

    Row {
        anchors.centerIn: parent  
        spacing: 10

        Button { text: "Высота " + Screen.height }
        Button { text: "test" }
        }
    }

    
    Button{
        id: test_but
        scale: 0.1
        y: Screen.height
        

        background: Rectangle{
            color: "transparent"
        }
        
        contentItem: Image{
            source: "file/power.png"
            fillMode: Image.PreserveAspectFit

        }

        Behavior on scale {
            NumberAnimation { duration: 500 }
        }

        MouseArea{
            anchors.fill: parent
            hoverEnabled: true
            onEntered: test_but.scale = (test_but.scale < 0.2) ? 0.3 : 0.1
            onExited: test_but.scale = (test_but.scale < 0.2) ? 0.3 : 0.1
            onClicked: controller.powers()
        }
    
    }

    Rectangle{
        width: 100
        height: 600
        color: "#FF0000"
    }

    }

}

    

