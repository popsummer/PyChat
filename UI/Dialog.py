# 重写closeEvent方法，实现dialog窗体关闭时执行一些代码
from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(QtWidgets.QMainWindow):

    def get_thread(self, main_thread):
        self.main_thread = main_thread

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
