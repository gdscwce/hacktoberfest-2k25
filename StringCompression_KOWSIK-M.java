public class StringCompression {
    public static void main(String[] args) {
      // Test Case
        String input = "aaabbccddd";
        System.out.println("Original: " + input);
        System.out.println("Compressed: " + compressString(input));
    }

    public static String compressString(String str) {
        if (str == null || str.isEmpty()) return str;

        StringBuilder compressed = new StringBuilder();
        int count = 1;

        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) == str.charAt(i - 1)) {
                count++;
            } else {
                compressed.append(str.charAt(i - 1)).append(count);
                count = 1;
            }
        }

        // Append the last character and its count
        compressed.append(str.charAt(str.length() - 1)).append(count);

        // Return compressed only if it's shorter
        return compressed.length() < str.length() ? compressed.toString() : str;
    }
}
