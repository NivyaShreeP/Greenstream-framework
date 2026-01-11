# Green Coding Rules – GreenStream Framework

## 1. Introduction

Green Coding Rules define the implementation-stage guidelines of the GreenStream framework.  
These rules translate sustainable design principles into concrete coding practices that reduce unnecessary computation, resource waste, and logical complexity.

Unlike traditional coding guidelines that focus mainly on correctness or performance, Green Coding Rules emphasize **environmental sustainability** by minimizing energy-intensive operations at the code level.

---

## 2. Purpose of Green Coding Rules

The objectives of Green Coding Rules are:

- To ensure that efficient design decisions (validated by DEI) are preserved during implementation
- To reduce computational overhead in application code
- To minimize unnecessary control-flow complexity
- To encourage reuse and optimization patterns
- To enable measurable sustainability improvements validated by SCGA

These rules are applied during the development of the `greenstream_app`.

---

## 3. List of Green Coding Rules

### Rule 1: Minimize Computational Instructions

**Description:**  
Avoid redundant calculations, repeated function calls, and unnecessary operations inside request handlers.

**Applied In:**

- Optimized logic in `greenstream_app` routes
- Reduced repeated data processing

**Validated By SCGA Metric:**

- CIC (Computational Instruction Count)

**Sustainability Impact:**  
Lower CPU utilization and reduced energy consumption.

---

### Rule 2: Keep Control Flow Simple

**Description:**  
Design functions with minimal nesting, fewer conditional branches, and linear execution paths wherever possible.

**Applied In:**

- Simplified if-else structures in CRUD handlers

**Validated By SCGA Metric:**

- NHC (Nesting Hierarchy Complexity)

**Sustainability Impact:**  
Reduced branching improves execution predictability and efficiency.

---

### Rule 3: Avoid Dead or Long-Running Loops

**Description:**  
Prevent infinite loops and unnecessary iterations that can lead to excessive CPU usage.

**Applied In:**

- No infinite or unbounded loops in GreenStream implementation

**Validated By SCGA Metric:**

- DLW (Dead Loop Weight)

**Sustainability Impact:**  
Avoids wasteful CPU cycles and potential system hangs.

---

### Rule 4: Limit Function Calls Inside Loops

**Description:**  
Avoid calling expensive functions repeatedly inside loops; compute values once and reuse them.

**Applied In:**

- Refactored logic to prevent repeated calls inside iterations

**Validated By SCGA Metric:**

- FCL (Function Call Load)

**Sustainability Impact:**  
Reduces repeated computation and improves runtime efficiency.

---

### Rule 5: Optimize Resource Usage

**Description:**  
Ensure resources such as database connections or file handles are used efficiently and not repeatedly reinitialized.

**Applied In:**

- Controlled database access patterns
- Avoided unnecessary reconnections

**Validated By SCGA Metric:**

- RSI (Resource State Inefficiency)

**Sustainability Impact:**  
Reduces overhead associated with frequent resource initialization.

---

### Rule 6: Encourage Code Optimization and Reuse

**Description:**  
Reuse logic, avoid duplicate code, and use efficient access patterns such as selective data retrieval.

**Applied In:**

- Shared utility functions
- Avoidance of duplicate CRUD logic

**Validated By SCGA Metric:**

- COI (Code Optimization Index)

**Sustainability Impact:**  
Improves overall code efficiency and reduces long-term maintenance cost.

---

## 4. Mapping Green Coding Rules to SCGA Metrics

| Green Coding Rule         | SCGA Metric | Expected Effect           |
| ------------------------- | ----------- | ------------------------- |
| Minimize computation      | CIC         | Lower instruction count   |
| Simple control flow       | NHC         | Reduced nesting           |
| Avoid dead loops          | DLW         | Zero dead loop weight     |
| Reduce function calls     | FCL         | Lower function load       |
| Efficient resource use    | RSI         | Stable resource usage     |
| Code reuse & optimization | COI         | Higher optimization score |

---

## 5. Role of Green Coding Rules in GreenStream

Green Coding Rules serve as the bridge between design-stage sustainability (DEI) and evaluation-stage validation (SCGA and GCS).

By enforcing these rules during implementation, the GreenStream framework ensures that:

- Efficient designs are not degraded during coding
- Sustainability improvements are measurable
- Higher Green Code Scores (GCS) are achieved

---

## 6. Summary

Green Coding Rules operationalize sustainability in software development by embedding environmentally conscious decisions directly into coding practices.  
When combined with DEI and SCGA, these rules enable GreenStream to provide a complete lifecycle-based green coding framework.

---
