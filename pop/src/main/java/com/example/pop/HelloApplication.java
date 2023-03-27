package com.example.pop;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.chart.Axis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
public class HelloApplication extends Application {
    @Override
    public void start(Stage primaryStage) {
        Pane root = new Pane();
// Массив массивов
        ObservableList<XYChart.Series> seriesList =
                FXCollections.observableArrayList();
// Массив жертв
        ObservableList<XYChart.Data> aList =
                FXCollections.observableArrayList();
// Массив хищников
        ObservableList<XYChart.Data> bList =
                FXCollections.observableArrayList();
        double r = 1; // Коэффицент рождаемости
        double q = 2; // Коэффицент смертности
        double a = 1;
        double f = 0.6;
        double dt = 0.1;
        double b = 0.1;
        double t = 0,dN,dC;
        double N = 100; // Численность жертвы
// Create axes
        Axis yAxis = new NumberAxis("N", 0, 2000, 200);
        Axis xAxis = new NumberAxis("t", 0, 3, 0.2);
        while (t<3000) {
            t+=dt;
            //dN=(r*N-a*N*C)*dt; // быстрота увелечения зайцев
            dN = (N*r) / (1 + Math.pow(a*N, b));
            N+=dN;  t+=dt;
            aList.add(new XYChart.Data(t,N));
        }
        seriesList.add(new XYChart.Series("Численность жертв", aList));
        seriesList.add(new XYChart.Series("Численность хищников", bList));
        LineChart chart = new LineChart(xAxis, yAxis, seriesList);
        chart.setPrefHeight(768);
        chart.setMinHeight(768);
        chart.setMaxHeight(768);
        chart.setPrefWidth(1024);
        chart.setMinWidth(1024);
        chart.setMaxWidth(1024);
        chart.setPrefSize(1024, 768);
        chart.setMinSize(1024, 768);
        chart.setMaxSize(1024, 768);
        root.getChildren().add(chart);
        Scene scene = new Scene(root);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Моделирование динамики численности популяции");
                primaryStage.show();
    }
    public static void main(String[] args) {
        launch(args);
    }
}