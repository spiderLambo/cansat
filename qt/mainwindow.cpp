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

void MainWindow::updateGUI(QByteArray data){
    ui->lc_byte_received->display(ui->lc_byte_received->value() + data.size());
}


void MainWindow::on_arreter_clicked()
{
    if (arduino->isWritable())
        arduino->write("s");

    else
        qDebug() << "Couldn't write to serial";
}

