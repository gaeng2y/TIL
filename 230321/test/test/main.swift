//
//  main.swift
//  test
//
//  Created by gaeng on 2023/03/13.
//

import Foundation

var gaeng = 0
let start = CFAbsoluteTimeGetCurrent()

let group = DispatchGroup()

for i in 0...1000000 {
    group.enter()
    DispatchQueue.global().async {
        gaeng = i
        group.leave()
    }
    group.wait()
}


//let semaphore = DispatchSemaphore(value: 0)
//
//for i in 0...1000000 {
//    DispatchQueue.global().async {
//        gaeng = i
//        semaphore.signal()
//    }
//    semaphore.wait()
//}

print(gaeng)
let end = CFAbsoluteTimeGetCurrent()
print(end - start)

