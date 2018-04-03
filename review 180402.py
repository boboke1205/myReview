# coding=utf-8
##########################################
# [문제 풀이] 중간점검 문제(함수, 클래스)#
##########################################

#문제 5-1
#두 개의 정수 값을 받아 두 값의 평균을 구하는 함수 (getAvg)
#
# def getAvg(a, b):
#     return (a + b)/2
# print getAvg(5, 7)
#
# #문제 5-2
# #함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정수 값에 대한 최대값과 최소값을 반환하는 함수(getMaxMin)를 작성하세요.
# #이건 틀린건가? def getMaxMin([]):
# def getMaxMin(list):
#     max = 0
#     min = 99999999999999999999
#     for i in list:
#         if i <= min:
#             min = i
#         elif i > max:
#             max = i
#     return (max, min)
#
#
# print getMaxMin([3, 56, 6, 7, 8, 90])

#문제 5-3
#체질량 지수(Body Mass Index, BMI)는 인간의 비만도를 나타내는 지수로서 체중과 키의 관계로 아래의 수식을 통해 계산됩니다.
# #여기서 중요한 점은 체중의 단위는 킬로그램(kg)이고 신장의 단위는 미터(m)라는 점입니다.
#
# def showMyBmi(weight, height):
#     bmi = weight / (height ^ 2)
#
#     if bmi < 18.5:
#         return "마른체형"
#     elif 18.5 <= bmi < 25.0:
#         return "표준"
#     elif 25.0 <= bmi < 30.0:
#         return "비만"
#     else:
#         return "고도비만"
#
# while (True):
#     height = input("키를 입력해주세요")
#     weight = input("몸무게를 입력해주세요")
#
#     print "당신은 %s 입니다 " % showMyBmi(weight, height)
#     print "-------------------------------"
#
#
# # 문제 5-7
#함수의 인자로 시작과 끝 숫자를 받아 시작부터 끝까지의 모든 정수값의 합을 반환하는 함수(getTotalSum)를 작성하세요(시작값과 끝값을 포함). (Hint - range() 함수 이용)


# def getTotlaSum(start, end):
#     sum = 0
#     for i in range(start, end + 1):
#         sum = sum + i
#
#     return sum
#
# print getTotlaSum(1, 100)


# 문제 6-1
#다음의 조건을 만족하는 Point라는 클래스를 작성하세요.
	# * Point 클래스는 생성자를 통해 (x, y) 좌표를 입력받는다.
	# * setx(x), sety(y) 메서드를 통해 x 좌표와 y 좌표를 따로 입력받을 수도 있다.
	# * get() 메서드를 호출하면 튜플로 구성된 (x, y) 좌표를 반환한다.
	# * move(dx, dy) 메서드는 현재 좌표를 dx, dy만큼 이동시킨다.


class Point:

    def setter(self,):
        x = 0
        y = 0
        while (True):
            self.x = input("X 좌표를 입력하세요 : ")
            self.y = input("Y 좌표를 입력하세요 : ")
            print "당신의 현재 좌표는 %s, %s입니다" % (self.x, self.y)
            return self.x, self.y

    def get(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self.x, self.y

boke = Point()
boke.setter()
boke.move(5, 5)
print boke.get()














