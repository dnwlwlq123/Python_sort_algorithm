# def solution(A, B):
#     return [(a, b) for a, b in zip(A,B)]
# result = solution([1,2,3], [3,4,5])
# print(result)
#
#
#
# def hello(num):
#     if num < 1 :
#         return
#     print('zzzzzzzzzz')
#     hello(num - 1)
# hello(5)

# def sierpinsi_triangle(n):
#     return '\n'.join(s(n))
#
# def triangle():
#     res = [
#         '   *    ',
#         '  * *   ',
#         ' *   *  ',
#         '* * * * ',
#     ]
#     return res
# def s(n):
#     if n == 1:
#         return triangle()
#     t = s(n-1)
#     l = len(t[0])
#     print(type(l))
#     margin = ' ' * (l // 2)
#
#     res = []
#     for line in t:
#         res.append(margin + line + margin)
#     for line in t:
#         res.append(line + line)
#     return res
# for i in range(5):
#     print(sierpinsi_triangle(i+1))
import code

def calculate_sum(a, b):
    result = a + b

    return result

x = 10
y = 20
sum_result = calculate_sum(x, y)
print(f"The sum is: {sum_result}")