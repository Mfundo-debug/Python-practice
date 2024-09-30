"""
suppose you have a tip calculator that calculates the tip based on the total amount of the bill and the service level.
The tip calculator has the following methods:
- set_total(total: float) -> None: sets the total amount of the bill
- set_service_level(service_level: str) -> None: sets the service level
- calculate_tip() -> float: calculates the tip based on the total amount of the bill and the service level
The service level can be one of the following: "good", "great", "excellent"
The tip percentage is based on the service level:
- good: 10%
- great: 15%
- excellent: 20%
Implement the tip calculator.
"""

import math
import numpy as np

def calculate_tip(total: float, service_level: str) -> float:
    if service_level == 'good':
        return total * 0.1
    elif service_level == 'great':
        return total * 0.15
    elif service_level == 'excellent':
        return total * 0.2
    else:
        return 0
    
if __name__ == '__main__':
    total = 100
    service_level = 'good'
    print(calculate_tip(total, service_level))  # 10.0
    service_level = 'great'
    print(calculate_tip(total, service_level))  # 15.0
    service_level = 'excellent'
    print(calculate_tip(total, service_level))  # 20.0