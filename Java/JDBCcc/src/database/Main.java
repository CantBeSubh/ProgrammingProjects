package database;

import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String url = "";
        String uname = "root";
        String pass = "19293949";

        // Class.forName("com.mysql.jdbc.Driver");
        Connection con = DriverManager.getConnection(url, uname, pass);
    }
}
