<!-- Centered content -->
<div align="center">
  <!-- Image -->
  <img src="https://github.com/user-attachments/assets/aa697654-16be-4b74-9d79-e035dc95833d" alt="Image Description" width="300px">
  
  <!-- Title and Information -->
  <h1><strong>Artificial Intelligence (Lab)</strong></h1>
  <h2>Lab 03: Introduction to Constraint Satisfaction Problems (CSP)</h2>
  <p><strong>Hassaan Ali Bukhari</strong><br>2022654<br><strong>Cyber Security</strong></p>
  <br>
</div>

<!-- Separator -->
<hr>

## Files Overview

- **CS351L_Lab3.pdf**: This file contains the lab task instructions for Lab 03 on Constraint Satisfaction Problems (CSP).
  
- **[Hassaan_Ali_Bukhari_CS351L_Lab03](./Hassaan_Ali_Bukhari_CS351L_Lab03/)**: This directory contains Python implementations for solving CSP-related problems.

  - **color_map.py**: Python script that uses CSP to solve a color map problem.
  
  - **main.py**: Main file to run the lab's CSP task, calling different functions from other scripts.
  
  - **names.py**: Script handling a dataset of names and associated operations within the CSP context.
  
  - **relation.py**: Python script managing the relationships or constraints used in the CSP task.
  
---

## Overview

In this lab, we explored Constraint Satisfaction Problems (CSP), a core concept in AI. We implemented a color map problem where different regions on a map are assigned colors under the constraint that no neighboring regions can share the same color.

- **CSP Problem**: Given a set of variables and constraints, we solved for values that satisfy all constraints. The lab involves creating Python scripts that implement the CSP solution through backtracking and other AI algorithms.

---

## Description of `main.py`

The `main.py` file is responsible for creating a graphical representation of a social network based on predefined nodes and relationships. It uses the `matplotlib` and `networkx` libraries to visualize connections between individuals in the network.

- **Key Features**:
  - Nodes represent individuals with attributes like age.
  - Edges represent relationships between individuals, color-coded based on the type of relationship (using the `color_map.py` script).
  - Users can input a person's name to generate a subgraph of that person and their direct connections.
  - The graph is displayed with nodes, edges, and labels showing the person's name and age.
  - The search person's node is highlighted in the final visualization.
  
The script provides a simple but effective way to visualize relationships in a social network, making it easier to analyze individual connections and their significance.

--- 

The directory contains the lab task which was performed in the lab.
