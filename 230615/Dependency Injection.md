# Dependency

```swift
class A {
    var name: String = "A"
}

class B {
    var name: String = "B"
}

class C {
    var a: A = .init()

    func printName() {
        print(a.name)
    }
}
```

`C는 A를 의존한다.` 라고 한다.

## 주입(Injection)

생성자를 통해 저장속성을 외부에서 주입한다.

```swift
class Person {
    var name: String

    init(name: String) {
        self.name = name
    }
}

// 외부에서 값을 주입해서 인스턴스 생성
let p1 = Person(name: "뉴진스")
```

위 예제를 주입으로 바꿔보자.

```swift
class C {
    var a: A

    init(a: A) {
        self.a = a
    }

    func printName() {
        print(a.name)
    }
}
```

### C를 만드는 방법 2

```swift
let coolA = A()
coolA.name = "멋진 A"

// 주입 방식만 개선
// 외부에서 주입하도록 만들었으나, 여전히 의존한다.
let c = C(a: coolA)
```

## 의존성 주입(DI)

* (개선된) 의존성: 프로토콜을 사용해서 의존성 분리 및 의존관계 역전시킴(IOC)
* 주입: 쿨한C완성품이 의존성을 가지는 클래스(A, B)를 쿨한C완성품 밖에서 생성자를 통해 주입 (언제든지 교체 가능해져, 확장성이 늘어남)
* 의존성 분리 및 의존관계 역전(Inversion of control)
* 프로토콜 사용의 장점 / 추상화의 장점

기존의 의존성을 개선하여 **(개선된) 의존성을 외부에서 주입할 수 있는 방식**으로 바꾸는 것 

즉, 프로토콜을 통해 생성자에 주입

**의존성**: 서로 다른 객체 사이에 의존 관계가 있다는 것

**주입**: 외부에서 객체(또는 데이터)를 생성해서 넣는 것 (생성자를 통해)

**의존성 주입**

프로그램 디자인이 결합도를 느슨하게 되도록하고 의존관계 역전 원칙과 단일 책임 원칙을 따 르도록 클라이언트 생성에 대한 의존성을 클라이언트의 행위로 부터 분리하는 것

기존의 의존성을 개선하여 **(개선된) 의존성을 외부에서 주입할 수 있는 방식**으로 바꾸는 것 

**(개선된) 의존성**: 프로토콜을 사용해서 의존성을 분리시키고  의존관계를 역전(Inversion Of Control) 시킴

**주입**: 생성자를 통해서 외부에서 값을 주입한다. (생성시 값 할당 가능 / 언제든지 교체 가능해져 확장성이 늘어남)

