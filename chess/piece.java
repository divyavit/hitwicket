package divyavit.hitwicket.chess;
import divyavit.hitwicket.chess.*;
public class Piece {
    private boolean available;
    private int x;
    private int y;

    public Piece(boolean available, int x, int y) {
        super();
        this.available = available;
        this.x = x;
        this.y = y;
    }


    public boolean isAvailable() {
        return available;
    }
    public void setAvailable(boolean available) {
        this.available = available;
    }
    public int getX() {
        return x;
    }
    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }
    public void setY(int y) {
        this.y = y;
    }

    public boolean isValid(Board board, int fromX, int fromY, int toX, int toY){
        if(toX == fromX && toY == fromY)
            return false; //cannot move nothing
        if(toX < 0 || toX > 5 || fromX < 0 || fromX > 5 || toY < 0 || toY > 5 || fromY <0 || fromY > 5)
            return false;
        return true;
    }

}
