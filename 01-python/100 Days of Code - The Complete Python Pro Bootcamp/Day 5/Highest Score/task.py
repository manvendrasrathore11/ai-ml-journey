student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
# sum = 0
# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# for score in student_scores:
#     sum = sum + score
#
# print(sum)

print(max(student_scores))
lar = 0
for num  in student_scores:
    if  num > lar:
        lar = num
print(lar)
