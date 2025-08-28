class Solution {
    public String mergeAlternately(String word1, String word2) {
        String biggerWord = word1.length() > word2.length() ? word1 : word2;
        String result = "";

        int idx;
        int minWordLength = Math.min(word1.length(), word2.length());
        for (idx = 0; idx < minWordLength; idx++) {
            result = result + word1.charAt(idx) + word2.charAt(idx);
        }
        return result + biggerWord.substring(idx);
    }
}