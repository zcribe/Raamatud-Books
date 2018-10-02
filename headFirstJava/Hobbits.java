public class Hobbits {
    String name;

    public static String toCamelCase(String string) {
        StringBuffer sb = new StringBuffer(string);
        sb.replace(0, 1, string.substring(0, 1).toUpperCase());
        return sb.toString();
    }

    public static void main(String[] args){
        Hobbits[] h = new Hobbits[3];
        int z = -1;

        while(z < 2){
            z = z +1;
            h[z] = new Hobbits();
            h[z].name = "bilbo";
            if (z == 0){
                h[z].name = "frodo";
            }
            if (z == 1){
                h[z].name = "sam";
            }
            System.out.print(toCamelCase(h[z].name) + " is a ");
            System.out.print("good Hobbit name. \n");
        }
    }

}


