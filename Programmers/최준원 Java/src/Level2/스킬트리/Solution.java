package Level2.스킬트리;

class Solution {
    public static int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int flag;
        for (String tree : skill_trees) {
            flag = 0;
            StringBuilder tmp = new StringBuilder();
            // String tmp = "";
            for (int i=0; i<tree.length(); ++i) {
                char c = tree.charAt(i);
                if (skill.indexOf(c) != -1) {
                    tmp.append(c);
                    // tmp+=c;
                }
            }
            for (int i=0; i<tmp.length(); ++i) {
                if (skill.charAt(i) != tmp.charAt(i)) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0)
                answer++;
        }
        return answer;
    }

    public static void main(String[] args) {
        int i = solution("CBD", new String[]{"BACDE", "CBADF", "AECB", "BDA"});
        System.out.print(i);
    }
}