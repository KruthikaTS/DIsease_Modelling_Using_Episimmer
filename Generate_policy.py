# Generate_policy.py
"""
Defines a simple lockdown policy.

Lockdown is active on:
- Monday (0)
- Thursday (3)
- Saturday (5)

Rule used:
    if time_step % 7 in [0, 3, 5] → lockdown
"""

class FullLockdown:
    def __init__(self, decision_fn):
        self.fn = decision_fn

    def apply(self, time_step):
        return self.fn(time_step)


def monday_thursday_saturday_lockdown_Aplus():
    policy_list = []

    def lockdown_fn(time_step):
        # based on weekly cycle: 0=Mon ... 6=Sun
        if time_step % 7 in [0, 3, 5]:
            return True
        return False

    policy_list.append(FullLockdown(lockdown_fn))
    return policy_list


def generate_policy():
    return monday_thursday_saturday_lockdown_Aplus()
