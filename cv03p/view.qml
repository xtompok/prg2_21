import QtQuick 2.14
import QtQuick.Controls 2.14

Rectangle {
	width: 500
	height: 500

	Component {
		id: rowComponent
		Item {
			height: childrenRect.height
			Text {
				text: display
			}
		}
	}

	ListView {
		anchors.fill: parent

		model:numberListModel
		delegate: rowComponent

	}
}