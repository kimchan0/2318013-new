# 고객이 상품을 장바구니에 담으면 결제까지 진행되는 코드입니다.
# 준비된 상품보다 더 많은 수량을 담으면 무슨 상품이 부족한지, 소지한 돈이 부족하다면 돈이 부족하다고 출력합니다.
# 코드를 입력하면 장바구니에 상품 무엇을 얼마나 담았는지 확인할 수 있습니다.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    # 재고 수량을 업데이트
    def update_quantity(self, amount):
        self.quantity += amount
    # 총 가격을 반환
    def total_price(self):
        return self.price * self.quantity
    # 상품 정보를 문자로 반환
    def __str__(self):
        return f'{self.name}: {self.price}원, {self.quantity}개'


class ShoppingCart:
    def __init__(self):
        self.items = [] # 장바구니에 담긴 상품 리스트
    # 상품을 장바구니에 추가
    def add(self, product):
        self.items.append(product)
    # 장바구니에 담긴 상품들의 가격을 계산
    def total(self):
        return sum(item.total_price() for item in self.items)
    # 장바구니에 담긴 상품 목록 출력
    def list_products(self):
        for item in self.items:
            print(item)


class Customer:
    def __init__(self, name, money):
        self.name = name # 이름
        self.money = money # 소지한 돈
        self.cart = ShoppingCart() # 장바구니

    def add_to_cart(self, product):
        if product.quantity > 0:
            self.cart.add(product)
            product.update_quantity(-1) # 상품 재고 감소
            print(f'{product.name} 추가.')
        else:
            print(f'{product.name} 품절.')
    # 결제를 진행
    def checkout(self):
        total = self.cart.total()
        if total <= self.money:
            self.money -= total
            print(f'결제 완료: {total}원.')
            self.cart.items.clear() # 장바구니 비우기
        else:
            print(f'소지한 돈 부족: 잔여 {self.money}원.')
# 상품들을 생성(사과, 바나나)
apple = Product('사과', 1000, 3)
banana = Product('바나나', 800, 5)
# 고객 생성(홍길동, 5000)
a = Customer('김찬영', 5000)
# 고객이 장바구니에 상품을 담음
a.add_to_cart(apple)
a.add_to_cart(banana)
# 장바구니에 담긴 상품들 출력
print('-------장바구니-------')
a.cart.list_products()
# 결제 진행
a.checkout()