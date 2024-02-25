#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "seriallink.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void updateGUI(QByteArray data);

private slots:
    void on_p_ledOn_clicked();

    void on_p_ledOff_clicked();

    void on_arreter_clicked();

    void on_arreter_clicked(bool checked);

private:
    Ui::MainWindow *ui;

    seriallink *arduino;
};
#endif // MAINWINDOW_H
