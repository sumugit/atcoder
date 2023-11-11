N = int(input())
S = list(input())

# S2 = ["W" for _ in range(len(S))]
# S3 = ["W" for _ in range(len(S))]
# # 左から
# for i in range(len(S2) - 2):
#     if S[i] == "R":
#         S2[i] = "R"
#         S2[i + 1] = "R"
#         S2[i + 2] = "R"
#     elif S[i] == "B":
#         S2[i] = "B"
#         S2[i + 1] = "B"
#         S2[i + 2] = "B"

# if "".join(S2) == "".join(S):
#     print("Yes")
#     exit()

# # 右から
# for i in range(len(S3)-1, 1, -1):
#     if S[i] == "R":
#         S3[i] = "R"
#         S3[i - 1] = "R"
#         S3[i - 2] = "R"
#     elif S[i] == "B":
#         S3[i] = "B"
#         S3[i - 1] = "B"
#         S3[i - 2] = "B"

# if "".join(S3) == "".join(S):
#     print("Yes")
#     exit()

# print(S2)
# print(S3)
# print("No")

# 最後の一手で決まる
for i in range(len(S) - 2):
    if S[i] == "R" and S[i + 1] == "R" and S[i + 2] == "R":
        print("Yes")
        exit()
    elif S[i] == "B" and S[i + 1] == "B" and S[i + 2] == "B":
        print("Yes")
        exit()
print("No")
