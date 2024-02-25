#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    arduino = new seriallink;

    arduino->openConnection();

    connect(arduino, &seriallink::gotNewData, this, &MainWindow::updateGUI);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_stopTransmition_clicked()
{
    if (arduino->isWritable())
        arduino->write("s");

    else
        qDebug() << "Couldn't write to serial";

}


void MainWindow::on_servomoteur_clicked()
{
    if (arduino->isWritable())
        arduino->write("s");

    else
        qDebug() << "Couldn't write to serial";

}

