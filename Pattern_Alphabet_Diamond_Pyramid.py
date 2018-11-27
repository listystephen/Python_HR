from string import ascii_lowercase as alphabet

def print_rangoli(size):
    frmt = '{{0:-^{width}}}'.format(width=size*4-3)
    print '\n'.join(
      frmt.format('-'.join([alphabet[size - s] for s in cal_range(in_size)]))
        for in_size in cal_range(size)
    )

def cal_range(size):
    return range(1, size) + range(size, 0, -1)
        
if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)