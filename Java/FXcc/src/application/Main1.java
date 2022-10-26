package application;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
// import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.control.ProgressBar;

public class Main1 extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {

        GridPane root = new GridPane();
        Button btn = new Button("Click ME!");
        btn.setWrapText(true);
        btn.setOnAction(new EventHandler<ActionEvent>() {

            @Override
            public void handle(ActionEvent arg0) {
                System.out.println("Button clicked");

            }
        });
        ProgressBar progress = new ProgressBar();
        Label user_id = new Label("User ID");
        Label password = new Label("Password");
        TextField tf1 = new TextField();
        TextField tf2 = new TextField();
        Button b = new Button("Submit");
        b.setOnAction(e -> System.out
                .println("User_ID: " + tf1.getText() + "" + " || Password: " + tf2.getText()));

        root.addRow(0, user_id, tf1);
        root.addRow(1, password, tf2);
        root.addRow(2, b, btn);
        root.addRow(3, progress);
        Scene scene = new Scene(root, 300, 300);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Button Class Example");
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}