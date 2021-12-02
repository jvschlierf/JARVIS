class BoundingBox:
    def __init__(self, filename,label, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label

def overlap(x1, w1, x2, w2):
    l1 = x1
    l2 = x2
    left = max(l1,l2)
    r1 = x1 + w1
    r2 = x2 + w2
    right = min(r1,r2)
    return right - left

def box_intersection(a, b):
    w = overlap(a.x, a.w, b.x, b.w)
    h = overlap(a.y, a.h, b.y, b.h)
    if w>0 and h> 0:
        area = w*h
        return area
    else:
        return 0

def box_union(a, b):
    i = box_intersection(a, b)
    u = a.w*a.h + b.w*b.h - i
    return u

def box_iou(a,  b):
    return box_intersection(a, b)/ box_union(a, b)


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"