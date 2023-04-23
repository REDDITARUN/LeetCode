class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        if (ransomNote.length() > magazine.length())
        return false;

        // creating a counter
        int [] counter = new int[26];

        // Converting into array

        for (char c : magazine.toCharArray())
        {
            counter [c-'a']++;

        }

        // checking if ransomNote can be constructed by using the letters from magazine
        for (char c : ransomNote.toCharArray())
        {
            if (counter [c-'a'] == 0)
            return false;

            counter [c-'a']--;
        }
        return true;


    }
}