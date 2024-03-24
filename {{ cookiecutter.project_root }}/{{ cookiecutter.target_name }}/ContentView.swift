//
//  ContentView.swift
//  {{ cookiecutter.target_name }}
//
//  Created by {{ cookiecutter.full_name }} on {{ cookiecutter.date }}.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundStyle(.tint)
            Text("Hello, world!")
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
