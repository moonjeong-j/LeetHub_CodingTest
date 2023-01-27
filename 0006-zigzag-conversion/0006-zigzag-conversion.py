class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: #예외 처리 - 한 줄이면 그대로 반환
            return s
        
        """
        이부분@@@!!store = [[] for _ in range(numRows)] -> 나는 Dictionary로 접근하려고 했음, 이런 방법이 있다는걸 알았더라면!
        """
        store = [[] for _ in range(numRows)] # numRows만큼 재배치할 행을 초기화
        answer = ''

        i = 0 # 문자 넣어 줄 행의 값
        toggleDown = True

        for x in s:
            store[i].append(x)
            if i == 0: # 현재 위치가 첫 번째 행이면 아래로 
                toggleDown = True
            elif i == numRows - 1: # 현재 위치가 끝 행이면 위로
                toggleDown = False
            if toggleDown:
                i += 1
            else:
                i -= 1

        for i in range(numRows):
            answer += ''.join(store[i])

        return answer
    # 출처 : https://piaflu.tistory.com/112
