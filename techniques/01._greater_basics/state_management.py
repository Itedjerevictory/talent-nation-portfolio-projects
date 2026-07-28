class StateTracker:
    def run_events(self):
        # Starting State
        tube_level = 100
        brush_state = "DRY"
        
        # Event 1: Wet the toothbrush
        brush_state = "WET"
        
        # Event 2: Squeeze toothpaste (uses 5%)
        tube_level = tube_level - 5
        
        # Event 3: Squeeze again by mistake (uses another 5%)
        tube_level = tube_level - 5
        
        # Do not change the return statement
        return tube_level, brush_state


def test_tracker():
    # Do not modify this testing wrapper
    tracker = StateTracker()
    # This automatically converts the result into a list for the JSON grader!
    return list(tracker.run_events())

def solution():
    return test_tracker()