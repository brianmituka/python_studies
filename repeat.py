#!/usr/bin/env python

def repeat(s, exclaim):

    result = s * 3

    if exclaim:
        result = result + '!!!'
    return result

def main():
    print repeat('yay ', False)
    print repeat('woo hoo', True)
if __name__ == '__main__':
    main()
