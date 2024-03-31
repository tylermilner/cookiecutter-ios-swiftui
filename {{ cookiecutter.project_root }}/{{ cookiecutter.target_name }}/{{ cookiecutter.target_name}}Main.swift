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
            {{ cookiecutter.target_name }}TestsApp.main()
        } else {
            {{ cookiecutter.target_name }}App.main()
        }
        #else
        {{ cookiecutter.target_name }}App.main()
        #endif
    }
}
