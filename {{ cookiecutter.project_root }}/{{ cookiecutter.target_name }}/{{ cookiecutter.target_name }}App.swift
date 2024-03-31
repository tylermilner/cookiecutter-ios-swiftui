//
//  {{ cookiecutter.target_name }}App.swift
//  {{ cookiecutter.target_name }}
//
//  Created by {{ cookiecutter.full_name }} on {{ cookiecutter.date }}.
//

import SwiftUI

@main
struct {{ cookiecutter.target_name }}App: App {
    var body: some Scene {
        WindowGroup {
            if isTesting {
                Text("Running tests...")
            } else {
                ContentView()
            }
        }
    }
}

// MARK: - Private

extension {{ cookiecutter.target_name }}App {
    private var isTesting: Bool {
        #if DEBUG
        return NSClassFromString("XCTestCase") != nil
        #else
        return false
        #endif
    }
}
