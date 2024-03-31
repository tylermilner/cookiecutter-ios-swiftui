//
//  {{ cookiecutter.target_name }}Main.swift
//  {{ cookiecutter.target_name }}
//
//  Created by {{ cookiecutter.full_name }} on {{ cookiecutter.date }}.
//

import SwiftUI

@main
struct {{ cookiecutter.target_name }}Main {
    static func main() {
        #if DEBUG
        if NSClassFromString("XCTestCase") != nil {
            MyAppTestsApp.main()
        } else {
            MyAppApp.main()
        }
        #else
        MyAppApp.main()
        #endif
    }
}
