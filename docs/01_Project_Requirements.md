# 1. Project Requirements

## 1.1 Project Overview

GeneWeaver is a Python-based project that aims to develop a GPU-accelerated CRISPR alignment engine for DNA sequence analysis.

The project will explore sequence alignment algorithms, parallel computing, and performance optimization to investigate how GPU acceleration can improve computational efficiency.

## 1.2 Project Objectives

The primary objectives are:

- Understand DNA sequence representation and CRISPR alignment concepts.
- Develop a working CPU-based DNA sequence alignment engine.
- Explore GPU acceleration for computationally intensive alignment operations.
- Compare CPU and GPU execution performance.
- Evaluate alignment accuracy and execution efficiency.
- Develop a user interface for submitting sequences and viewing results.
- Maintain project documentation and version control.

## 1.3 Functional Requirements

The application is expected to support the following functions:

1. Accept DNA sequences as input.
2. Validate DNA sequence characters.
3. Process and compare DNA sequences.
4. Perform sequence alignment using a CPU implementation.
5. Explore GPU-based acceleration of supported alignment operations.
6. Display alignment results and relevant performance metrics.
7. Compare CPU and GPU execution results.

## 1.4 Non-Functional Requirements

- **Accuracy:** Alignment results must be consistent with the selected algorithm.
- **Performance:** Execution time should be measured and evaluated.
- **Reliability:** Invalid sequence inputs should be handled appropriately.
- **Maintainability:** Code should be modular, readable, and documented.
- **Testability:** Important functions should have automated tests.
- **Portability:** The CPU implementation should work independently of GPU availability.

## 1.5 Proposed Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development language |
| NumPy | Numerical operations |
| CUDA | GPU computing platform, if supported |
| CuPy | GPU array operations, if compatible |
| Streamlit | User interface |
| pytest | Automated testing |
| Git and GitHub | Version control |

The final GPU technology will be selected after checking the available hardware and software compatibility.

## 1.6 Development Phases

1. Project setup and environment verification.
2. DNA sequence fundamentals and input validation.
3. CPU-based sequence alignment implementation.
4. Alignment testing and correctness validation.
5. GPU acceleration exploration and implementation.
6. CPU versus GPU performance evaluation.
7. User interface development.
8. Final testing, documentation, and demonstration.

## 1.7 Constraints and Assumptions

- The project is intended for educational and development purposes.
- GPU acceleration depends on compatible hardware and software.
- A working CPU implementation will be established before GPU optimization.
- The exact alignment algorithm and evaluation dataset will be selected during development.
- Performance measurements will depend on the available computer hardware.

## 1.8 Expected Deliverables

- Python source code.
- Automated tests.
- Project documentation.
- CPU and GPU performance evaluation, where GPU execution is supported.
- Project report and presentation.
- Final project demonstration.

## 1.9 Project Information

- **Project:** GeneWeaver
- **Organization:** Infotact Solutions
- **Domain:** Python Development
- **Project Period:** 10 November 2026 – 10 December 2026
- **Status:** Initial Development