//
//  ViewController.swift
//  230427_Combine_Example
//
//  Created by gaeng on 2023/04/27.
//

import Combine
import UIKit

class ViewController: UIViewController {
    lazy var textField: UITextField = {
        let tf = UITextField()
        tf.borderStyle = .roundedRect
        return tf
    }()
    
    lazy var label: UILabel = {
        let label = UILabel()
        label.textAlignment = .center
        return label
    }()
    
    @Published var text = AnyPublisher<String, Never>(<#T##publisher: Publisher##Publisher#>)
    
    private var cancellables = Set<AnyCancellable>()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        self.view.backgroundColor = .white
        
        // textfield 붙이기
        self.view.addSubview(self.textField)
        self.textField.translatesAutoresizingMaskIntoConstraints = false
        [
            self.textField.centerXAnchor.constraint(equalTo: self.view.centerXAnchor),
            self.textField.centerYAnchor.constraint(equalTo: self.view.centerYAnchor),
            self.textField.widthAnchor.constraint(equalToConstant: 200),
            self.textField.heightAnchor.constraint(equalToConstant: 50)
        ].forEach {
            $0.isActive = true
        }
        
        // UITextFeid text가 바뀌면 NotificationCenter를 통해 값을 방출하도록 하는 publisher를 만드는 과정
        let publisher = NotificationCenter.default
            .publisher(for: UITextField.textDidChangeNotification, object: self.textField)
            .compactMap { $0.object as? UITextField }
            .map { $0.text ?? "" }
            .eraseToAnyPublisher()
        
        // 해당 publisher를 구독하는 과정
        let subscriber = publisher
            .sink(receiveCompletion: {
                print("receiveCompletion: \($0)")
            }, receiveValue: {
                print("receiveValue: \($0)")
                self.text = $0
            })
        subscriber.store(in: &self.cancellables)
        
        // textfield 붙이기
        self.view.addSubview(self.label)
        self.label.translatesAutoresizingMaskIntoConstraints = false
        [
            self.label.topAnchor.constraint(equalTo: self.textField.bottomAnchor, constant: -30),
            self.label.widthAnchor.constraint(equalToConstant: 200),
            self.label.heightAnchor.constraint(equalToConstant: 50)
        ].forEach {
            $0.isActive = true
        }
        
        self.$text
            .receive(on: DispatchQueue.main)
            .assign(to: \.text, on: self.label)
    }
}
