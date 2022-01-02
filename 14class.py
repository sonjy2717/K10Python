'''
인스턴스 변수 (JAVA에서의 멤버변수)
    : 메소드 안에 정의되는 변수

 ⇀ 클래스 내부에서는 self.변수명 형태로 접근
 ⇀ 클래스 외부에서는 객체변수.인스턴스변수 형태로 접근
 
인스턴스 메소드 (JAVA에서의 멤버메소드)
    : 인스턴스 변수에 항상 접근할 수 있도록
      메소드의 첫번째 파라미터에 항상 객체 자신을 의미하는 self를 선언해야 한다.
'''
# 클래스 선언
class FourCalculator:
    # setter()메소드는 초기화 담당
    def setdata(self, first, second):
        # self.인스턴스변수 = 매개변수      형태로 기술
        self.first = first
        self.second = second
    # 사칙연산을 수행하는 인스턴스 메소드 정의.
    # 인스턴스 변수에 접근하기 위해 첫번째 파라미터는 self를 반드시 사용
    def addition(self):
        result = self.first + self.second
        return result
    def subtraction(self):
        result = self.first - self.second
        return result
    def multiplication(self):
        result = self.first * self.second
        return result
    def division(self):
        result = self.first / self.second
        return result

# 객체생성. Python에서는 new를 사용하지 않는다.
a = FourCalculator()
b = FourCalculator()

# 각 객체의 setter() 메소드를 통해 인스턴스 변수를 초기화
a.setdata(4, 2)
b.setdata(3, 8)

# 각 객체의 인스턴스 메소드를 호출
print("객체a 덧셈", a.addition())
print("객체a 곱셈", a.multiplication())
print("객체b 뺄셈", b.subtraction())
print("객체b 나눗셈", b.division())


'''
생성자 (initializer)
    : 클래스로부터 객체를 만들 때 인스턴스 변수를 초기화한다.
      init 양쪽에 언더바 2개를 붙여서 정의.

정적메소드 (static method)
    : 클래스명으로 바로 접근할 수 있는 메소드.
      @staticmethod 라는 데코레이터를 사용.
    
클래스메소드
    : 정적메소드와 비슷한데, 객체 인스턴스를 의미하는 self대신
      클래스를 의미하는 cls라는 파라미터를 전달받는다.
      cls를 통해 클래스변수에 엑세스 가능.
      @classmethod 라는 데코레이터를 사용.

'''
class CalculatorInit:
    
    # 클래스 변수 (클래스 전체에서 접근가능한 전역변수)
    count = 0
    
    '''
    파이썬에서는 생성자 오버로딩은 지원하지 않는다.
    
    def __init__(self):
        self.first = 1
        self.second = 2
    '''
    # 생성자 메소드 정의. 인스턴스변수의 초기화를 위해 첫번째 파라미터에 self를 기술.
    def __init__(self, first, second):
        self.first = first
        self.second = second
        # 생성자에서 클래스변수에 접근가능
        CalculatorInit.count += 1
    
    # 일반적인 인스턴스 메소드 정의
    def addition(self):
        result = self.first + self.second
        return result
    
    # 정적메소드 정의. 클래스명으로 즉시 호출가능.
    @staticmethod
    def staticArea(pFirst, pSecond):
        result = pFirst * pSecond
        print("static메소드", result)
    
    # 클래스메소드 정의. cls를 통해 클래스변수에 접근가능.
    @classmethod
    def showInfo(cls):
        print('class메소드', cls.count)

# fCal2 = CalculatorInit() -> 인자가 없는 기본생성자는 정의되지 않음.
# 2개의 인자를 전달해서 객체생성
fCal = CalculatorInit(2010, 43)
# 일반적인 인스턴스 메소드 호출
print(fCal.addition())
# 클래스 메소드 호출1 : 인스턴스변수를 통한 호출
fCal.showInfo()
# 클래스 메소드 호출2 : 클래스명을 통한 호출
CalculatorInit.showInfo()
# 정적메소드 호출
CalculatorInit.staticArea(5, 8)


'''
상속
    : 파이썬에서는 별도의 키워드없이
      클래스 정의시 매개변수 형태로 상속한다.
'''
class MoreCalculator(CalculatorInit):
    # 자식쪽에서 확장한 인스턴스메소드
    def pow(self):
        # first를 second만큼 거듭제곱
        result = self.first ** self.second
        return result
    # 오버라이딩 : 부모의 기능을 자식쪽에서 재정의함
    def addition(self):
        return (self.first + self.second) * 2

# 자식객체 생성 및 호출
moreCal = MoreCalculator(4, 3)
print("상속후", moreCal.pow())  # 4의 3승의 결과출력

# 부모객체 및 자식객체 생성
p1 = CalculatorInit(100, 200)
p2 = MoreCalculator(100, 200)
# 오버라이딩 결과확인
print("부모객체로호출", p1.addition())  # 결과 : 300
print("자식객체로호출", p2.addition())  # 결과 : 600

'''
정보은닉
    : 인스턴스 변수를 비공개속성(private)으로 설정
'''
class Person:
    # 생성자 메소드 정의
    def __init__(self, n, a, pw):
        self.name = n
        self.age = a
        # 인스턴스변수 앞에 언더바를 2개 붙이면 private이 된다.
        self.__passwd = pw  # 생성자에서 초기화
    # 해당 메소드가 getter()의 역할을 하고있다.
    def secret_info(self):
        return self.__passwd
    
p1 = Person('my', 22, 'qwer1234')
print("이름", p1.name)
print("나이", p1.age)
## private 변수이므로 클래스 외부에서 접근할 수 없어서 에러발생
#print("비밀번호1", p1.__passwd)
## passwd 형태의 변수가 선언된 적이 없으므로 에러발생
#print("비밀번호2", p1.passwd)
# private 변수는 메소드를 통해 간접적으로 접근가능
print("비밀번호", p1.secret_info())