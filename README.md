# Intelligent Routing Engine

A foundational graph search and path optimization engine built from scratch in Python. This project simulates enterprise network infrastructure routing, comparing search algorithms across a 10-node transit hub matrix.

Developed locally using **Anaconda** and **JupyterLab** as part of my AI/ML internship engineering milestones.

---

## 🚀 Features
* **Custom Topology Setup:** Map of 10 linked transit hubs utilizing precise distance paths.
* **Algorithm Benchmarking Matrix:** Compares performance across:
  * **Breadth-First Search (BFS):** Pure topological layer tracking.
  * **Uniform Cost Search (UCS):** Exact mathematical path cost minimization.
  * **A\* Search:** High-efficiency path discovery utilizing custom straight-line heuristics.
* **Performance Analytics:** Instant output showing exact paths chosen, total travel costs, and processing effort (total nodes explored).

---

## 🛠️ Tech Stack & Environment
* **Language:** Python 3
* **Libraries Used:** `heapq` (Standard Library)
* **Environment:** Anaconda Navigator & JupyterLab

---

## 🖥️ How to Run
1. Open **JupyterLab** or any terminal environment via **Anaconda**.
2. Run the script cell.
3. Input your origin and destination hubs on a single line separated by a space (e.g., `S H`)
