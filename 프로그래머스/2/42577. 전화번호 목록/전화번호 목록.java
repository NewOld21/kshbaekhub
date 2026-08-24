import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Trie trie = new Trie();
        int size = phone_book.length;
        Arrays.sort(phone_book);
        for(int i = 0; i < size; i++){
            trie.insert(phone_book[i]);
        }

        for(int i = 0; i < size; i++){
            if(trie.search(phone_book[i])){
                answer = false;
                break;
            }
        }
        return answer;
    }
}

class Node{
    Map<Character, Node> child = new HashMap<Character, Node>();
    boolean end;
}

class Trie{
    Node root = new Node();

    void insert(String s){
        Node node = this.root;
        int size = s.length();
        for(int i = 0; i < size; i++){
            char key = s.charAt(i);

            // 현재 문자에 해당하는 자식 노드가 있는지 확인
            if (!node.child.containsKey(key)) {
                // 없으면 새로운 Node를 추가
                node.child.put(key, new Node());
            }

            // 해당 자식 노드로 이동
            node = node.child.get(key);
        }

        // 전화번호 끝 노드에 end를 true로 변경
        node.end = true;
    }

    boolean search(String s){
        Node node = this.root;

        int size = s.length();
        for(int i = 0; i < size; i++){
            char key = s.charAt(i);
            
            //해당 노드에 자식이 있는지 확인
            if (node.child.containsKey(key)) {
                node = node.child.get(key);
            } 
            
            // end가 true인데 전화번호가 마지막 숫자가 아닌 경우 접두어로 판단
            if (node.end && i < s.length() - 1) {
                return true;
            }
        }

        return false;
    }
}