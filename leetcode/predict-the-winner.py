class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        left  = 0
        right = len(nums) - 1
        turn = True
        def solve(left , right , turn):
            if left == right:
                if turn :
                    return [nums[left] , 0]
                else:
                    return [0 , nums[right]]

            if turn:
                left_score = solve(left + 1, right , not turn)
                right_score = solve(left , right-1 , not turn)
                left_score[0] += nums[left]
                right_score[0] += nums[right]
                if left_score[0] > right_score[0]:
                    return left_score
                else:
                    return right_score

            else:
                left_score = solve(left + 1, right , not turn)
                right_score = solve(left , right-1 , not turn)
                left_score[1] += nums[left]
                right_score[1] += nums[right]
                if left_score[1] > right_score[1]:
                    return left_score
                else:
                    return right_score

        answer = solve(left , right , turn)
        
        return answer[0] >= answer[1]

