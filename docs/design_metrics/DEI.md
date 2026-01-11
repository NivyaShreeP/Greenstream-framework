# Design Efficiency Index (DEI)

## 1. Introduction

Design Efficiency Index (DEI) is a design-stage sustainability metric proposed in the GreenStream framework.  
It evaluates how computationally efficient and environmentally sustainable a software system is at the **design phase**, before implementation.

Unlike traditional software design evaluations that focus on correctness, modularity, and maintainability, DEI focuses on estimating the **potential energy and computation efficiency** of a system by analyzing its logical design flows.

---

## 2. Purpose of DEI in GreenStream

The primary objective of DEI is to ensure that sustainability considerations are introduced **early in the software development lifecycle**.

Key goals of DEI:

- Reduce unnecessary logical complexity before coding
- Minimize redundant operations at the design level
- Encourage simple and linear control flows
- Provide a quantitative sustainability indicator at the design stage

DEI serves as the first sustainability checkpoint in the GreenStream framework.

---

## 3. General DEI Formula

The Design Efficiency Index is calculated using the following generalized formula:

DEI = 1 − (W1·NS + W2·DP + W3·RS) / R + SF

Where:

- NS = Number of logical steps in the design flow
- DP = Number of decision points or conditional branches
- RS = Number of redundant or repeated steps
- W1, W2, W3 = Weights for steps, decisions, and redundancy (default value = 1)
- R = Reference maximum value used for normalization (R = 10)
- SF = Simplicity Factor (value between 0 and 1 based on design clarity)

The DEI value is normalized between 0 and 1 and later converted into a percentage.

---

## 4. DEI Calculation Methodology

The DEI calculation is performed using the following steps:

1. Identify the core functional flows of the system
2. Represent each flow as a sequence of logical steps or a flowchart
3. Count the number of steps (NS) in each flow
4. Count the number of decision points (DP)
5. Identify redundant or repeated steps (RS), if any
6. Assign a Simplicity Factor (SF) based on flow linearity
7. Apply the DEI formula to compute the efficiency score
8. Calculate the overall DEI by averaging all flow scores

This procedure is generic and applicable to any software project.

---

## 5. CRUD Application as Benchmark

To validate the applicability of DEI, a CRUD-based Notes application is used as a benchmark.  
CRUD applications are chosen because they have well-defined and easily analyzable control flows.

Each CRUD operation is evaluated independently using the DEI formula.

---

## 6. Detailed DEI Calculation for CRUD Operations

### 6.1 Create Operation

Design Flow:

1. Receive input
2. Validate input
3. Store note
4. Return success response

Parameter Values:

- NS = 4
- DP = 1 (input validation)
- RS = 0
- SF = 1.0

DEI Calculation:
DEI = 1 − (4 + 1 + 0) / 10 + 1.0  
DEI = 1 − 0.5 + 1.0 = 1.5 → capped to 1.0

DEI (Create) = 100%

---

### 6.2 Read Operation

Design Flow:

1. Receive request
2. Retrieve notes
3. Display output

Parameter Values:

- NS = 3
- DP = 0
- RS = 0
- SF = 1.0

DEI Calculation:
DEI = 1 − (3 / 10) + 1.0  
DEI = 1.7 → capped to 1.0

DEI (Read) = 100%

---

### 6.3 Update Operation

Design Flow:

1. Receive input
2. Validate input
3. Fetch existing note
4. Check note existence
5. Update note
6. Return response

Parameter Values:

- NS = 6
- DP = 2 (validation and existence check)
- RS = 0
- SF = 0.8

DEI Calculation:
DEI = 1 − (6 + 2) / 10 + 0.8  
DEI = 1 − 0.8 + 0.8 = 1.0

DEI (Update) = 100%

---

### 6.4 Delete Operation

Design Flow:

1. Receive note ID
2. Check note existence
3. Delete note
4. Return response

Parameter Values:

- NS = 4
- DP = 1
- RS = 0
- SF = 1.0

DEI Calculation:
DEI = 1 − (4 + 1) / 10 + 1.0  
DEI = 1.5 → capped to 1.0

DEI (Delete) = 100%

---

## 7. Overall DEI Calculation

The overall DEI for the system is calculated as the average of all CRUD operation scores:

DEI_overall = (DEI_create + DEI_read + DEI_update + DEI_delete) / 4

DEI_overall = (1.0 + 1.0 + 1.0 + 1.0) / 4  
DEI_overall = 1.0 → 100%

This indicates that the system design is logically simple and energy-efficient at the design stage.

---

## 8. Role of DEI in GreenStream Framework

DEI ensures sustainability considerations are incorporated at the design stage.  
High DEI scores indicate efficient logic flows, which are later validated during the implementation and evaluation stages using Green Coding Rules and Static Green Code Analysis (SCGA).

Thus, DEI forms the foundation for achieving higher Green Code Scores (GCS) in the GreenStream framework.

---
