from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2 import QtCore
import typing
import sys
import json

VIEW_URL = "view.qml"  


class NumberListModel(QAbstractListModel):
    """ Class for maintaining list of cities"""

    def __init__(self):
        QAbstractListModel.__init__(self)
        self.number_list = [1,2,3,4]

    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        return len(self.number_list)

    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        """ For given index and DisplayRole return name of the selected number"""
        # Return None if the index is not valid
        if not index.isValid():
            return None
        # If the role is the DisplayRole, return the number
        if role == QtCore.Qt.DisplayRole:
            return self.number_list[index.row()]


app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
numberlist_model = NumberListModel()
ctxt = view.rootContext()
ctxt.setContextProperty('numberListModel',numberlist_model)
view.setSource(url)
view.show()
app.exec_()