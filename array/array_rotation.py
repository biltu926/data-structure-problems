import argparse

def rotate(arr, k):
    ''' Rotate the given array arr by k positions on the left '''
    a = [arr[i%len(arr)] for i in range(k%len(arr), len(arr) + k%len(arr))]
    return a

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--l', nargs="*", type=int)
    parser.add_argument('--k', type=int)
    args = parser.parse_args()

    print(rotate(args.l, args.k))