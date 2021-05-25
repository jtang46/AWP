def create_baseline_boxes(width, height):
    baseline_boxes = [None] * 5
    # Top-left box
    baseline_boxes[0] = [0, int(height * 0.9), int(width * 0.1), height]
    # Top-right box
    baseline_boxes[1] = [int(width  * 0.9), int(height * 0.9), width, height]
    # Bottom-left box
    baseline_boxes[2] = [0, 0, int(width * 0.1), int(height * 0.1)]
    # Bottom-right box
    baseline_boxes[3] = [int(width * 0.9), 0, width, int(height * 0.1)]
    # Middle box
    mid_x, mid_y = width // 2, height // 2
    off_x, off_y = int(width * 0.05), int(height * 0.05)
    baseline_boxes[4] = [mid_x - off_x, mid_y - off_y, mid_x + off_x, mid_y + off_y]
    return baseline_boxes
