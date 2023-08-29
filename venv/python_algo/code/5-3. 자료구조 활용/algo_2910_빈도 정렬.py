# 아까 풀었던 영단어 암기 문제랑 똑같아여
# 근데 이번에는 빈도가 같을시 먼저 나왔던 얘를 기준으로 하라는데
# 쓰스읍 먼저 나왔던 놈을 기준으로 어떻게 하지??
# 파이썬 너무 사기네
# 난 무슨 클래스를 선언해서 그걸로 정렬을 해야하나 했는데
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, c = map(int, input().split())
    numbers = {}
    idx = 1
    for x in list(map(int, input().split())):
        if x in numbers:
            numbers[x][0] += 1
        else:
            numbers[x] = [1, idx]
            idx += 1


    sortedArr = sorted(numbers.items(), key=lambda x: (-x[1][0], x[1][1]))
    # print(sortedArr)
    res = ''
    for x, order in sortedArr:
        for _ in range(order[0]):
            res += str(x) + " "

    print(res)
    
# 자바 코드로 클래스를 이용해서 한 방식


# class WordInfo implements Comparable<WordInfo> {
#     int value;
#     int freq;
#     int order;
# 
#     public WordInfo(int value, int freq, int order) {
#         this.value = value;
#         this.freq = freq;
#         this.order = order;
#     }
# 
#     @Override
#     public int compareTo(WordInfo other) {
#         if (this.freq == other.freq) {
#             return Integer.compare(this.order, other.order);
#         }
#         return Integer.compare(other.freq, this.freq);
#     }
# }
# 
# public class Main {
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         String[] nc = br.readLine().split(" ");
#         int n = Integer.parseInt(nc[0]);
#         int c = Integer.parseInt(nc[1]);
# 
#         List<WordInfo> words = new ArrayList<>();
#         int idx = 1;
#         String[] inputArr = br.readLine().split(" ");
#         for (String s : inputArr) {
#             int x = Integer.parseInt(s);
#             boolean found = false;
#             for (WordInfo word : words) {
#                 if (word.value == x) {
#                     word.freq++;
#                     found = true;
#                     break;
#                 }
#             }
#             if (!found) {
#                 words.add(new WordInfo(x, 1, idx));
#                 idx++;
#             }
#         }
# 
#         Collections.sort(words);
# 
#         StringBuilder res = new StringBuilder();
#         for (WordInfo word : words) {
#             for (int i = 0; i < word.freq; i++) {
#                 res.append(word.value).append(" ");
#             }
#         }
# 
#         System.out.println(res);
#     }
# }