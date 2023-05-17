package com.example.demo;

/*import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}*/

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
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class HelloApplication extends Application {
    @Override
    public void start(Stage primaryStage) {
        Pane root = new Pane();
// Массив массивов
        ObservableList<XYChart.Series> seriesList =
                FXCollections.observableArrayList();
// Массив
        ObservableList<XYChart.Data> aList =
                FXCollections.observableArrayList();
        List<Double> lambda = new ArrayList<>();
        int Tn=100;
        int t=0;
        int N = 0;
        double temp = 0;
        while (t<=Tn) {
            double r = 0+Math.random()*1.0;;
            if (t>=0 || t<=50){
                temp =0.02*t;
            }
            if (t>=50 || t<=100){
                temp =0.5;
            }
            //double temp =0.2*t;
            //double temp =0.5;
            //double temp = 1.1-Math.pow(t-50,2)/2500;
            lambda.add(temp);
            double ro = -1/temp*Math.log(r);
            t+=ro;
            N++;
            aList.add(new XYChart.Data(t,N));
        }
// Create axes
        double fxMax = Collections.max(lambda);
        double fxMin = Collections.min(lambda);
// Create axes
        Axis yAxis = new NumberAxis("Count", 0, N, N/10);
        Axis xAxis = new NumberAxis("t", 0, Tn, 10);
        seriesList.add(new XYChart.Series("Graphic", aList));
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
        primaryStage.setTitle("Моделирование потока случайных событий");
        primaryStage.show();
    }
    public static void main(String[] args) {
        launch(args);
    }
}
