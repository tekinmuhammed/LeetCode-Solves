/*🔫 LeetCode 2125. Number of Laser Beams in a Bank    

**Difficulty:** Medium
**Problem Link:** [LeetCode 2125](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/)


🧠 Problem Description
[Github LeetCode 2125. Number of Laser Beams in a Bank](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2125.%20Number%20of%20Laser%20Beams%20in%20a%20Bank)
*/

class Solution {
  public int numberOfBeams(String[] bank) {
    int prev = 0, ans = 0;

    for (String s: bank) {
      int count = 0;
      for (int i = 0; i < s.length(); i++)
        if (s.charAt(i) == '1') {
          count++;
        }

      if (count > 0) {
        ans += prev * count;
        prev = count;
      }
    }

    return ans;
  }
}