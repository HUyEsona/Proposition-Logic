import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy.logic.boolalg import Equivalent, Not, Or, And, Implies
from prettytable import PrettyTable

# Khai báo biến logic
P, Q, R = sp.symbols('P Q R')

#danh sách các biểu thức logic tương ứng với từng câu a đén g:
expressions = {
    "Câu a": [
        ("(¬P) ⇔ (¬Q)", Equivalent(~P, ~Q)),
        ("P ⇔ Q", Equivalent(P, Q))
    ],
    "Câu b": [
        ("P ∨ ¬Q", Or(P, Not(Q))),
        ("(P ∨ ¬Q) ⇔ P", Equivalent(Or(P, Not(Q)), P))
    ],
    "Câu c": [
        ("(Q ∨ R)", Or(Q, R)),
        ("(P ∧ (Q ∨ R))", And(P, Or(Q, R))),
        ("¬[P ∧ (Q ∨ R)]", Not(And(P, Or(Q, R))))
    ],
    "Câu d": [
        ("(P ∧ Q)", And(P, Q)),
        ("¬(P ∧ Q)", Not(And(P, Q)))
    ],
    "Câu e": [
        ("P ∧ (¬P)", And(P, Not(P))),
        ("(P ∧ (¬P)) ⇒ Q", Implies(And(P, Not(P)), Q))
    ],
    "Câu f": [
        ("(P ∧ Q)", And(P, Q)),
        ("(P ∧ Q) ⇒ P", Implies(And(P, Q), P))
    ],
    "Câu g": [
        ("(P ∨ Q)", Or(P, Q)),
        ("P ⇒ (P ∨ Q)", Implies(P, Or(P, Q)))
    ]
}

#lặp qua từng bài và in bảng chân trị
for title, expr_list in expressions.items():
    print(f"\n{title}")
    table = PrettyTable()
    
    #xác định số lượng biến cần kiểm tra
    variables = {P, Q, R} if any("R" in str(expr) for _, expr in expr_list) else {P, Q}
    
    #định nghĩa tiêu đề bảng
    headers = ["P", "Q"]
    if R in variables:
        headers.append("R")
    headers.extend([expr_name for expr_name, _ in expr_list])
    table.field_names = headers

    #sinh các giá trị chân trị
    values = [(p, q, r) if R in variables else (p, q) for p in [True, False] for q in [True, False] for r in ([True, False] if R in variables else [None])]
    
    for value in values:
        p, q, *r = value
        substitutions = {P: p, Q: q}
        if r:
            substitutions[R] = r[0]
        
        row = [p, q]
        if r:
            row.append(r[0])

        row.extend([(bool(expr.subs(substitutions))) for _, expr in expr_list])
        table.add_row(row)

    print(table)
