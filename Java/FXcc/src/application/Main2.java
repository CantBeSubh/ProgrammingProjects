package application;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.text.Text;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;
import javafx.scene.layout.StackPane;
import javafx.scene.Group;

public class Main2 extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        Text text = new Text();
        text.setText("DA2 CSE1007");
        text.setX(300);
        text.setY(20);
        text.setFont(Font.font("Abyssinica SIL", FontWeight.BOLD, FontPosture.REGULAR, 20));
        Button btn1 = new Button("Say, Hello World");
        btn1.setOnAction(new EventHandler<ActionEvent>() {

            @Override
            public void handle(ActionEvent arg0) {
                System.out.println("hello world");
            }
        });
        Group root = new Group();
        root.getChildren().add(text);
        root.getChildren().add(btn1);
        Scene scene = new Scene(root, 600, 400);
        primaryStage.setTitle("First JavaFX Application");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}